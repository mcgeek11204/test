import hmac
import time
import json
import hashlib
import requests
import math
from typing import Dict, Tuple, Optional
from datetime import datetime
from urllib.parse import urlencode

class TrubitMarketMaker:
    def __init__(self):
        self.api_key = "6FZLYg8z3Td9o4HoqaV2l7vyI1fXTW4h0AGSDwCA9hjWkD5gJUaAHbVqVNS0fa8A"
        self.api_secret = "Kr7yAxXXhWPcPvFIvE6q9YMdYj6VcixYtDNWVhmCNVJs3ITNtcue8hq7aezuahX4"
        self.base_url = "https://api-spot.trubit.com"
        self.symbol = "USDTMMXN"
        self.price_increment = 0.008
        self.max_order_amount = 1000
        self.check_interval = 0.05
        self.min_notional = 1
        self.fee_rate = 0.01
        self.quantity_precision = 2
        self.price_precision = 4
        self.kline_check_interval = 10
        self.session = requests.Session()
        self.session.headers.update({'X-BH-APIKEY': self.api_key})
        self.last_kline_time = None

    def _generate_signature(self, query_string: str) -> str:
        return hmac.new(self.api_secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

    def _get_timestamp(self) -> int:
        return int(time.time() * 1000)

    def get_order_book(self) -> Optional[Dict]:
        try:
            response = self.session.get(f"{self.base_url}/openapi/quote/v1/depth", params={'symbol': self.symbol, 'limit': 5})
            if response.status_code == 200:
                return response.json()
            return None
        except:
            return None

    def get_my_open_orders(self) -> list:
        timestamp = self._get_timestamp()
        params = {'symbol': self.symbol, 'timestamp': timestamp}
        query_string = urlencode(params)
        signature = self._generate_signature(query_string)
        params['signature'] = signature
        try:
            response = self.session.get(f"{self.base_url}/openapi/v1/openOrders", params=params)
            if response.status_code == 200:
                return response.json()
            return []
        except:
            return []

    def am_i_best_position(self, order_book: Dict) -> bool:
        try:
            open_orders = self.get_my_open_orders()
            if not open_orders:
                return False

            market_best_bid = float(order_book['bids'][0][0])
            market_best_ask = float(order_book['asks'][0][0])
            
            for order in open_orders:
                if order['side'] == 'BUY' and float(order['price']) < market_best_bid:
                    return False
                elif order['side'] == 'SELL' and float(order['price']) > market_best_ask:
                    return False
            
            return True
        except:
            return False

    def get_account_balance(self) -> Tuple[float, float]:
        timestamp = self._get_timestamp()
        query_string = f"timestamp={timestamp}"
        signature = self._generate_signature(query_string)
        try:
            response = self.session.get(f"{self.base_url}/openapi/v1/account", params={'timestamp': timestamp, 'signature': signature})
            if response.status_code == 200:
                data = response.json()
                usdt_balance = 0.0
                mmxn_balance = 0.0
                for balance in data['balances']:
                    if balance['asset'] == 'USDT':
                        usdt_balance = float(balance['free'])
                    elif balance['asset'] == 'MMXN':
                        mmxn_balance = float(balance['free'])
                return usdt_balance, mmxn_balance
            return 0.0, 0.0
        except:
            return 0.0, 0.0

    def calculate_order_quantity(self, side: str, price: float, balance: float) -> float:
        try:
            available_balance = balance * (1 - self.fee_rate)
            if available_balance <= 0:
                return 0

            if side == 'BUY':
                mmxn_amount = min(available_balance, self.max_order_amount * price)
                quantity = mmxn_amount / price
            else:
                quantity = min(available_balance, self.max_order_amount)

            quantity = float(f"{quantity:.{self.quantity_precision}f}")
            if quantity < self.min_notional:
                return 0
                
            if quantity > self.max_order_amount:
                quantity = float(f"{self.max_order_amount:.{self.quantity_precision}f}")
                
            return quantity
        except:
            return 0

    def place_order(self, side: str, price: float, quantity: float) -> bool:
        try:
            if quantity <= 0:
                return False
                
            formatted_quantity = f"{quantity:.{self.quantity_precision}f}"
            formatted_price = f"{price:.{self.price_precision}f}"
            
            timestamp = self._get_timestamp()
            params = {
                'symbol': self.symbol,
                'side': side,
                'type': 'LIMIT',
                'timeInForce': 'GTC',
                'quantity': formatted_quantity,
                'price': formatted_price,
                'timestamp': timestamp
            }
            
            query_string = urlencode(params)
            signature = self._generate_signature(query_string)
            params['signature'] = signature
            
            response = self.session.post(f"{self.base_url}/openapi/v1/order", params=params)
            return response.status_code == 200
        except:
            return False

    def cancel_all_orders(self) -> bool:
        timestamp = self._get_timestamp()
        params = {'symbol': self.symbol, 'timestamp': timestamp}
        query_string = urlencode(params)
        signature = self._generate_signature(query_string)
        params['signature'] = signature
        try:
            response = self.session.delete(f"{self.base_url}/openapi/v1/openOrders", params=params)
            return response.status_code == 200
        except:
            return False

    def get_klines(self, interval='15m', limit=2) -> Optional[list]:
        try:
            params = {'symbol': self.symbol, 'interval': interval, 'limit': limit}
            response = self.session.get(f"{self.base_url}/openapi/quote/v1/klines", params=params)
            if response.status_code == 200:
                kline_data = response.json()
                if kline_data and len(kline_data) == limit:
                    result = []
                    for kline in kline_data:
                        result.append({
                            'open': float(kline[1]),
                            'high': float(kline[2]),
                            'low': float(kline[3]),
                            'close': float(kline[4]),
                            'time': kline[0]
                        })
                    return result
            return None
        except:
            return None

    def run(self):
        print(f"开始运行做市策略 - {self.symbol}")
        print(f"价格增减量: {self.price_increment}")
        print(f"最大下单量: {self.max_order_amount} USDT")
        print(f"最小交易金额: {self.min_notional} USDT")
        print(f"预留手续费率: {self.fee_rate*100}%")
        print(f"数量精度: {self.quantity_precision}位小数")
        print(f"价格精度: {self.price_precision}位小数")
        print(f"K线检查间隔: {self.kline_check_interval} 秒")
        print("=" * 50)

        self.cancel_all_orders()
        
        while True:
            try:
                order_book = self.get_order_book()
                if not order_book or not order_book.get('bids') or not order_book.get('asks'):
                    time.sleep(0.1)
                    continue

                klines = self.get_klines()

                if klines and len(klines) == 2:
                    last_kline = klines[0]
                    current_kline = klines[1]
                    if self.last_kline_time is None or current_kline['time'] != self.last_kline_time:
                        self.last_kline_time = current_kline['time']
                        self.cancel_all_and_reorder(order_book, last_kline)
                    else:
                        open_orders = self.get_my_open_orders()
                        if open_orders:
                            valid_orders = True
                            for order in open_orders:
                                order_price = float(order['price'])
                                if not (last_kline['low'] + self.price_increment <= order_price <= last_kline['high'] - self.price_increment):
                                    valid_orders = False
                                    break
                            if not valid_orders:
                                self.cancel_all_and_reorder(order_book, last_kline)
                        elif not self.am_i_best_position(order_book):
                            self.cancel_all_and_reorder(order_book, last_kline)

                time.sleep(self.check_interval)
                
            except:
                time.sleep(0.1)

    def cancel_all_and_reorder(self, order_book: Dict, kline: Optional[Dict] = None):
        if self.cancel_all_orders():
            best_bid = float(order_book['bids'][0][0])
            best_ask = float(order_book['asks'][0][0])

            if kline:
                target_bid = min(kline['high'] - self.price_increment, best_bid + self.price_increment)
                target_bid = max(kline['low'] + self.price_increment, target_bid)

                target_ask = max(kline['low'] + self.price_increment, best_ask - self.price_increment)
                target_ask = min(kline['high'] - self.price_increment, target_ask)
            else:
                target_bid = best_bid + self.price_increment
                target_ask = best_ask - self.price_increment
            
            usdt_balance, mmxn_balance = self.get_account_balance()
            
            buy_quantity = self.calculate_order_quantity('BUY', target_bid, mmxn_balance)
            if buy_quantity > 0:
                self.place_order('BUY', target_bid, buy_quantity)
            
            sell_quantity = self.calculate_order_quantity('SELL', target_ask, usdt_balance)
            if sell_quantity > 0:
                self.place_order('SELL', target_ask, sell_quantity)

if __name__ == "__main__":
    try:
        market_maker = TrubitMarketMaker()
        market_maker.run()
    except KeyboardInterrupt:
        print("\n程序已手动停止")
    except Exception as e:
        print(f"\n程序异常退出: {e}")
