import hmac
import time
import json
import hashlib
import requests
from typing import Dict, Tuple, Optional, List
from datetime import datetime
from urllib.parse import urlencode

# 5-minute interval in milliseconds
FIVE_MIN_MS = 5 * 60 * 1000

class TrubitMarketMaker:
    def __init__(self):
        self.api_key = "6FZLYg8z3Td9o4HoqaV2l7vyI1fXTW4h0AGSDwCA9hjWkD5gJUaAHbVqVNS0fa8A"
        self.api_secret = "Kr7yAxXXhWPcPvFIvE6q9YMdYj6VcixYtDNWVhmCNVJs3ITNtcue8hq7aezuahX4"
        self.base_url = "https://api-spot.trubit.com"
        self.symbol = "USDTMMXN"
        self.price_increment = 0.008
        self.max_order_amount = 1000
        self.min_notional = 1
        self.fee_rate = 0.004
        self.quantity_precision = 2
        self.price_precision = 4
        self.kline_interval = '5m'
        self.session = requests.Session()
        self.session.headers.update({'X-BH-APIKEY': self.api_key})
        self.monitor_interval = 1  # seconds
        # For clock-based trigger: stores the minute value of the last trigger.
        self.last_trigger_minute: Optional[int] = None

    def _generate_signature(self, query_string: str) -> str:
        return hmac.new(
            self.api_secret.encode('utf-8'),
            query_string.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()

    def _get_timestamp(self) -> int:
        return int(time.time() * 1000)

    def get_order_book(self) -> Optional[Dict]:
        try:
            response = self.session.get(
                f"{self.base_url}/openapi/quote/v1/depth",
                params={'symbol': self.symbol, 'limit': 5}
            )
            if response.status_code == 200:
                return response.json()
            else:
                print(f"获取订单簿失败：{response.text}")
            return None
        except Exception as e:
            print(f"获取订单簿异常：{e}")
            return None

    def get_my_open_orders(self) -> list:
        timestamp = self._get_timestamp()
        params = {'symbol': self.symbol, 'timestamp': timestamp}
        query_string = urlencode(params)
        signature = self._generate_signature(query_string)
        params['signature'] = signature
        try:
            response = self.session.get(
                f"{self.base_url}/openapi/v1/openOrders", params=params
            )
            if response.status_code == 200:
                return response.json()
            else:
                print(f"获取挂单失败：{response.text}")
            return []
        except Exception as e:
            print(f"获取挂单异常：{e}")
            return []

    def cancel_order(self, order_id: str) -> bool:
        timestamp = self._get_timestamp()
        params = {'symbol': self.symbol, 'orderId': order_id, 'timestamp': timestamp}
        query_string = urlencode(params)
        signature = self._generate_signature(query_string)
        params['signature'] = signature
        try:
            response = self.session.delete(
                f"{self.base_url}/openapi/v1/order", params=params
            )
            if response.status_code == 200:
                print(f"成功撤销订单: {order_id}")
                return True
            else:
                print(f"撤销订单 {order_id} 失败: {response.text}")
                return False
        except Exception as e:
            print(f"撤销订单 {order_id} 异常: {e}")
            return False

    def cancel_all_orders(self) -> bool:
        open_orders = self.get_my_open_orders()
        if not open_orders:
            print("没有挂单，无需撤销")
            return True
        all_cancelled = True
        for order in open_orders:
            order_id = order.get("orderId")
            if not order_id:
                print("订单中缺少 orderId 字段，跳过该订单")
                continue
            if not self.cancel_order(order_id):
                all_cancelled = False
        return all_cancelled

    def get_account_balance(self) -> Tuple[float, float]:
        timestamp = self._get_timestamp()
        query_string = f"timestamp={timestamp}"
        signature = self._generate_signature(query_string)
        try:
            response = self.session.get(
                f"{self.base_url}/openapi/v1/account",
                params={'timestamp': timestamp, 'signature': signature}
            )
            if response.status_code == 200:
                data = response.json()
                usdt_balance = 0.0
                mmxn_balance = 0.0
                for balance in data.get('balances', []):
                    if balance.get('asset') == 'USDT':
                        usdt_balance = float(balance.get('free', 0))
                    elif balance.get('asset') == 'MMXN':
                        mmxn_balance = float(balance.get('free', 0))
                return usdt_balance, mmxn_balance
            else:
                print(f"获取账户余额失败：{response.text}")
            return 0.0, 0.0
        except Exception as e:
            print(f"获取账户余额异常：{e}")
            return 0.0, 0.0

    def calculate_order_quantity(self, side: str, price: float, balance: float) -> float:
        try:
            available_balance = balance * (1 - self.fee_rate)
            if available_balance <= 0:
                return 0.0
            if side == 'BUY':
                quantity = available_balance / price
            else:
                quantity = available_balance
            quantity = float(f"{quantity:.{self.quantity_precision}f}")
            if quantity < self.min_notional:
                return 0.0
            if quantity > self.max_order_amount:
                quantity = float(f"{self.max_order_amount:.{self.quantity_precision}f}")
            return quantity
        except Exception as e:
            print(f"计算订单量异常：{e}")
            return 0.0

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
            response = self.session.post(
                f"{self.base_url}/openapi/v1/order", params=params
            )
            if response.status_code == 200:
                print(f"{side}单挂单成功：价格 {formatted_price} 量 {formatted_quantity}")
                return True
            else:
                print(f"{side}单挂单失败：{response.text}")
            return False
        except Exception as e:
            print(f"{side}单挂单异常：{e}")
            return False

    def get_klines(self, limit: int = 5) -> Optional[List[Dict]]:
        try:
            params = {'symbol': self.symbol, 'interval': self.kline_interval, 'limit': limit}
            response = self.session.get(
                f"{self.base_url}/openapi/quote/v1/klines", params=params
            )
            if response.status_code == 200:
                kline_data = response.json()
                if kline_data and len(kline_data) > 0:
                    results = []
                    # Each kline is assumed: [time, open, high, low, close, ...]
                    for kline in kline_data:
                        results.append({
                            'time': int(kline[0]),  # open time in ms
                            'open': float(kline[1]),
                            'high': float(kline[2]),
                            'low': float(kline[3]),
                            'close': float(kline[4])
                        })
                    # Sort by time ascending for easier processing.
                    results.sort(key=lambda x: x['time'])
                    return results
            else:
                print(f"获取K线失败：{response.text}")
            return None
        except Exception as e:
            print(f"获取K线异常：{e}")
            return None

    def get_latest_complete_kline(self) -> Optional[Dict]:
        """
        Returns the latest complete 5-minute candle.
        A complete candle's open time + 5 minutes is less than or equal to the current time.
        """
        klines = self.get_klines(limit=5)
        if not klines:
            print("未能获取K线数据")
            return None
        now = self._get_timestamp()
        complete_candles = [k for k in klines if k['time'] + FIVE_MIN_MS <= now]
        if not complete_candles:
            print("没有完整的K线数据")
            return None
        # Return the latest complete candle.
        return complete_candles[-1]

    def place_orders_based_on_previous_kline(self, previous_kline: Dict):
        amplitude = (previous_kline['high'] - previous_kline['low']) / previous_kline['low']
        if amplitude < self.fee_rate:
            print("上一根K线幅度过窄，利润不足，暂时不挂单")
            return
        print("根据上一根完整K线数据挂单...")
        # Use previous candle's lowest price + increment for BUY, highest price - increment for SELL.
        target_bid = previous_kline['low'] + self.price_increment
        target_ask = previous_kline['high'] - self.price_increment

        usdt_balance, mmxn_balance = self.get_account_balance()
        buy_quantity = self.calculate_order_quantity('BUY', target_bid, mmxn_balance)
        if buy_quantity > 0:
            self.place_order('BUY', target_bid, buy_quantity)
        else:
            print("买单资金不足，未挂单")

        sell_quantity = self.calculate_order_quantity('SELL', target_ask, usdt_balance)
        if sell_quantity > 0:
            self.place_order('SELL', target_ask, sell_quantity)
        else:
            print("卖单资金不足，未挂单")

    def run(self):
        print(f"开始运行做市策略（{self.kline_interval} K线版） - {self.symbol}")
        print(f"价格增减量: {self.price_increment}")
        print(f"最大下单量: {self.max_order_amount} USDT")
        print(f"最小交易金额: {self.min_notional} USDT")
        print(f"Maker费率: {self.fee_rate * 100}%")
        print(f"数量精度: {self.quantity_precision}位小数")
        print(f"价格精度: {self.price_precision}位小数")
        print(f"K线周期: {self.kline_interval}")
        print("=" * 50)

        # At startup, immediately place orders with the latest complete candle.
        print("程序启动时重新挂单...")
        previous_kline = self.get_latest_complete_kline()
        if previous_kline:
            self.cancel_all_orders()
            self.place_orders_based_on_previous_kline(previous_kline)
            now = datetime.now()
            self.last_trigger_minute = now.minute
        else:
            print("未能获取有效的K线数据，启动挂单失败")

        # Continuous monitoring every second.
        while True:
            try:
                now = datetime.now()
                # Check clock-based trigger: at :00-:02 seconds when the minute is a multiple of 5.
                if now.minute % 5 == 0 and now.second < 3:
                    if self.last_trigger_minute != now.minute:
                        print(f"时钟触发：{now.strftime('%H:%M:%S')} 达到整5分钟，重新挂单...")
                        previous_kline = self.get_latest_complete_kline()
                        if previous_kline:
                            self.cancel_all_orders()
                            self.place_orders_based_on_previous_kline(previous_kline)
                        else:
                            print("未能获取有效的K线数据")
                        self.last_trigger_minute = now.minute
                # Additionally, if orders are missing, re-place orders.
                open_orders = self.get_my_open_orders()
                if not open_orders:
                    print("检测到订单全部消失，立即重新挂单...")
                    previous_kline = self.get_latest_complete_kline()
                    if previous_kline:
                        self.cancel_all_orders()
                        self.place_orders_based_on_previous_kline(previous_kline)
                        self.last_trigger_minute = now.minute
                    else:
                        print("未能获取有效的K线数据")
                time.sleep(self.monitor_interval)
            except Exception as e:
                print(f"运行监控异常：{e}")
                time.sleep(self.monitor_interval)

if __name__ == "__main__":
    try:
        market_maker = TrubitMarketMaker()
        market_maker.run()
    except KeyboardInterrupt:
        print("\n程序已手动停止")
    except Exception as e:
        print(f"\n程序异常退出: {e}")
