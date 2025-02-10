# Api Endpoints for TruBit Exchange | TruBit Pro
[![](https://docs-api.trubit.com/~gitbook/image?url=https%3A%2F%2F667726841-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FOcgSwPEO1WP2OtRQfugH%252Ficon%252FnCcAn2TzCmxkC4yXOTIM%252Ffavicon.png%3Falt%3Dmedia%26token%3D11b89f4e-7089-4ecf-8bbe-8999ebe19828&width=32&dpr=4&quality=100&sign=77dd1510&sv=2)![](https://docs-api.trubit.com/~gitbook/image?url=https%3A%2F%2F667726841-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FOcgSwPEO1WP2OtRQfugH%252Ficon%252FnCcAn2TzCmxkC4yXOTIM%252Ffavicon.png%3Falt%3Dmedia%26token%3D11b89f4e-7089-4ecf-8bbe-8999ebe19828&width=32&dpr=4&quality=100&sign=77dd1510&sv=2)

TruBit Pro

](/trubit-pro)

1.  [Spot](https://docs-api.trubit.com/trubit-pro/spot)

Api Endpoints for TruBit Exchange
---------------------------------

[PreviousSpot](https://docs-api.trubit.com/trubit-pro/spot)
[NextError codes](https://docs-api.trubit.com/trubit-pro/spot/errors)

Last updated 8 months ago

Name

base endpoint

rest-api

web-socket-streams

user-data-stream

[**https://api-spot.trubit.com**](https://api-spot.trubit.com/)

[**wss://ws.trubit.com**](wss://ws.trubit.com/)

[**wss://ws.trubit.com**](wss://ws.trubit.com/)

# Error codes | TruBit Pro
1.  [Spot](https://docs-api.trubit.com/trubit-pro/spot)

Error codes
-----------

Errors consist of two parts: an error code and a message. Codes are universal, but messages can vary. Here is the error JSON payload:

```
{
  "code":-1121,
  "msg":"Invalid symbol."
}
```


10xx - General Server or Network issues


-------------------------------------------

*   An unknown error occured while processing the request.
    

*   Internal error; unable to process your request. Please try again.
    

*   You are not authorized to execute this request. Request need API Key included in . We suggest that API Key be included in any request.
    

*   Too many requests; please use the websocket for live updates.
    
*   Too many requests; current limit is %s requests per minute. Please use the websocket for live updates to avoid polling the API.
    
*   Way too many requests; IP banned until %s. Please use the websocket for live updates to avoid bans.
    

*   An unexpected response was received from the message bus. Execution status unknown. OPEN API server find some exception in execute request .Please report to Customer service.
    

*   Timeout waiting for response from backend server. Send status unknown; execution status unknown.
    

### 

\-1014 UNKNOWN\_ORDER\_COMPOSITION

*   Unsupported order combination.
    

*   Reach the rate limit .Please slow down your request speed.
    

*   Too many new orders; current limit is %s orders per %s.
    

### 

\-1016 SERVICE\_SHUTTING\_DOWN

*   This service is no longer available.
    

### 

\-1020 UNSUPPORTED\_OPERATION

*   This operation is not supported.
    

*   Timestamp for this request is outside of the recvWindow.
    
*   Timestamp for this request was 1000ms ahead of the server's time.
    
*   Please check the difference between your local time and server time .
    

*   Signature for this request is not valid.
    

*   Illegal characters found in a parameter.
    
*   Illegal characters found in parameter '%s'; legal range is '%s'.
    

### 

\-1101 TOO\_MANY\_PARAMETERS

*   Too many parameters sent for this endpoint.
    
*   Too many parameters; expected '%s' and received '%s'.
    
*   Duplicate values for a parameter detected.
    

### 

\-1102 MANDATORY\_PARAM\_EMPTY\_OR\_MALFORMED

*   A mandatory parameter was not sent, was empty/null, or malformed.
    
*   Mandatory parameter '%s' was not sent, was empty/null, or malformed.
    
*   Param '%s' or '%s' must be sent, but both were empty/null!
    

*   An unknown parameter was sent.
    
*   In TruBit Open Api , each request requires at least one parameter. {Timestamp}.
    

*   Not all sent parameters were read.
    
*   Not all sent parameters were read; read '%s' parameter(s) but was sent '%s'.
    

*   Parameter '%s' was empty.
    

*   A parameter was sent when not required.
    
*   Parameter '%s' sent when not required.
    

*   Precision is over the maximum defined for this asset.
    

*   No orders on book for symbol.
    

*   TimeInForce parameter sent when not required.
    

*   In the current version, this parameter is either empty or GTC.
    

*   In the current version , ORDER\_TYPE values is LIMIT or MARKET.
    

*   ORDER\_SIDE values is BUY or SELL
    

### 

\-1118 EMPTY\_NEW\_CL\_ORD\_ID

*   New client order ID was empty.
    

### 

\-1119 EMPTY\_ORG\_CL\_ORD\_ID

*   Original client order ID was empty.
    

*   This listenKey does not exist.
    

*   Lookup interval is too big.
    
*   More than %s hours between startTime and endTime.
    

### 

\-1128 OPTIONAL\_PARAMS\_BAD\_COMBO

*   Combination of optional parameters invalid.
    

*   Invalid data sent for a parameter.
    
*   Data sent for paramter '%s' is not valid.
    

### 

\-1132 ORDER\_PRICE\_TOO\_HIGH

### 

\-1133 ORDER\_PRICE\_TOO\_SMALL

*   Order price lower than the minimum,please check general info.
    

### 

\-1134 ORDER\_PRICE\_PRECISION\_TOO\_LONG

*   Order price decimal too long,please check general info.
    

### 

\-1135 ORDER\_QUANTITY\_TOO\_BIG

*   Order quantity too large.
    

### 

\-1136 ORDER\_QUANTITY\_TOO\_SMALL

*   Order quantity lower than the minimum.
    

### 

\-1137 ORDER\_QUANTITY\_PRECISION\_TOO\_LONG

*   Order quantity decimal too long.
    

### 

\-1138 ORDER\_PRICE\_WAVE\_EXCEED

*   Order price exceeds permissible range.
    

### 

\-1140 ORDER\_AMOUNT\_TOO\_SMALL

*   Transaction amount lower than the minimum.
    

### 

\-1143 ORDER\_NOT\_FOUND\_ON\_ORDER\_BOOK

*   Cannot be found on order book
    

### 

\-1145 ORDER\_NOT\_SUPPORT\_CANCELLATION

*   This order type does not support cancellation
    

### 

\-1146 ORDER\_CREATION\_TIMEOUT

### 

\-1147 ORDER\_CANCELLATION\_TIMEOUT

*   Order cancellation timeout
    

*   Invalid API-key, IP, or permissions for action.
    

*   No trading window could be found for the symbol. Try ticker/24hrs instead.
    

Messages for -1010 ERROR\_MSG\_RECEIVED, -2010 NEW\_ORDER\_REJECTED, and -2011 CANCEL\_REJECTED


---------------------------------------------------------------------------------------------------

This code is sent when an error has been returned by the matching engine. The following messages which will indicate the specific error:

The order (by either `orderId`, `clOrdId`, `origClOrdId`) could not be found

The `clOrdId` is already in use

The symbol is not trading

"Account has insufficient balance for requested action."

Not enough funds to complete the action

"Market orders are not supported for this symbol."

`MARKET` is not enabled on the symbol

"Iceberg orders are not supported for this symbol."

`icebergQty` is not enabled on the symbol

"Stop loss orders are not supported for this symbol."

`STOP_LOSS` is not enabled on the symbol

"Stop loss limit orders are not supported for this symbol."

`STOP_LOSS_LIMIT` is not enabled on the symbol

"Take profit orders are not supported for this symbol."

`TAKE_PROFIT` is not enabled on the symbol

"Take profit limit orders are not supported for this symbol."

`TAKE_PROFIT_LIMIT` is not enabled on the symbol

"Price\* QTY is zero or less."

`price`\* `quantity` is too low

"IcebergQty exceeds QTY."

`icebergQty` must be less than the order quantity

"This action disabled is on this account."

Contact customer support; some actions have been disabled on the account.

"Unsupported order combination"

The `orderType`, `timeInForce`, `stopPrice`, and/or `icebergQty` combination isn't allowed.

"Order would trigger immediately."

The order's stop price is not valid when compared to the last traded price.

"Cancel order is invalid. Check origClOrdId and orderId."

No `origClOrdId` or `orderId` was sent in.

"Order would immediately match and take."

`LIMIT_MAKER` order type would immediately match and trade, and not be a pure maker order.

"Filter failure: PRICE\_FILTER"

`price` is too high, too low, and/or not following the tick size rule for the symbol.

"Filter failure: LOT\_SIZE"

`quantity` is too high, too low, and/or not following the step size rule for the symbol.

"Filter failure: MIN\_NOTIONAL"

`price`\* `quantity` is too low to be a valid order for the symbol.

"Filter failure: MAX\_NUM\_ORDERS"

Account has too many open orders on the symbol.

"Filter failure: MAX\_ALGO\_ORDERS"

Account has too many open stop loss and/or take profit orders on the symbol.

"Filter failure: BROKER\_MAX\_NUM\_ORDERS"

Account has too many open orders on the exchange.

"Filter failure: BROKER\_MAX\_ALGO\_ORDERS"

Account has too many open stop loss and/or take profit orders on the exchange.

"Filter failure: ICEBERG\_PARTS"

Iceberg order would break into too many parts; icebergQty is too small.

Last updated 11 months ago

# Options Open API | TruBit Pro
1.  [Spot](https://docs-api.trubit.com/trubit-pro/spot)

Options Open API
----------------

The base url of open API can be found [here](https://github.com/Galactic-Tech/GitBook/blob/main/Spot/endpoint.md)

Current trading rules and symbol information.

0

None

Retrieves the current time on server (in ms).

In the `symbols` field, the endpoint will return information on current actively trading cryptos. You can ignore this section.

In the `options` field: All actively trading options will be displayed.

Underlying asset for the option

Precision of the option quantity

Quote asset for the option

Precision of the option price

Whether iceberg orders are allowed.

For `filters` in `options` field:

Precision of the option price。

Precision of the option price.

Minimal trading quantity of the option

Precision of the option quantity

Precision of the option order size (quantity \* price)

```
{
  'timezone': 'UTC',
  'serverTime': '1555048558151',
  'brokerFilters': [],
  'symbols': [{...}],
  'options': [
        {
          'filters': [
            {
              'minPrice': '0.01',
              'maxPrice': '100000.00000000',
              'tickSize': '0.01',
              'filterType': 'PRICE_FILTER'
            },
            {
              'minQty': '0.01',
              'maxQty': '100000.00000000',
              'stepSize': '0.001',
              'filterType': 'LOT_SIZE'
            },
            {
              'minNotional': '1',
              'filterType': 'MIN_NOTIONAL'
            }
          ],
          'exchangeId': '301',
          'symbol': 'BTC0412PS5100',
          'status': 'TRADING',
          'baseAsset': 'BTC0412PS5100',
          'baseAssetPrecision': '0.001',
          'quoteAsset': 'USDT',
          'quotePrecision': '0.01',
          'icebergAllowed': False
          },...
        ]
      }      
```


Retrieves available trading and expired options. Expired options will be returned if `expired` is set `true`.

1

```
GET /openapi/v1/getOptions
```


Set to `true` to show expired options instead of active ones. This can be useful for retrieving historic data.

Name of the option. 'underlying - expiration date - option type(CS is call spread and PS is put spread) - strike'

The strike price of the option.

Unix timestamp when the option was first created (ms).

Unix timestamp when the option will expire (ms)

`1`\=Call Spread, `0`\= Put Spread

The maximum payoff of the option.

The underlying price index name of the option

```
[
  {'symbol': 'BTC0412PS5100',
  'strike': '5100.0',
  'created': '1554710400000',
  'expiration': '1555055400000',
  'optionType': 0,
  'maxPayOff': '500.0',
  'underlying': 'BTCUSDT',
  'settlement': 'weekly'
},...
      ]
```


Retrieves the current index price and EDP. This API endpoint does not take any Parameters.

0

```
GET /openapi/quote/v1/option/index
```


None

The currency index price.

Estimated delivery price (Average index price in the last 10 minutes).

```
{
  'BTCUSDT':{
    'index':3795.77,
    'edp': 3652.81
  },
  ...
}
```


Retrieves the options order book.

Adjusted based on the limit:

```
GET /openapi/quote/v1/option/depth
```


The option name for which to retrieve the order book, use `getOptions` to get option names.

The number of entries to return for bids and asks.

List of all bids, best bids first. See below for entry details.

List of all asks, best asks first. See below for entry details.

The fields `bids` and `asks` are lists of order book price level entries, sorted from best to worst.

The total quantity of orders for this price level

```
{
  'time': 1555049455783,
  'bids': [
   ['78.82', '0.526'],//[Price, Quantity]
   ['77.24', '1.22'],
   ['76.65', '1.043'],
   ['76.58', '1.34'],
   ['75.67', '1.52'],
   ['75.12', '0.635'],
   ['75.02', '0.72'],
   ['75.01', '0.672'],
   ['73.73', '1.282'],
   ['73.58', '1.116'],
   ['73.45', '0.471'],
   ['73.44', '0.483'],
   ['72.32', '0.383'],
   ['72.26', '1.283'],
   ['72.11', '0.703'],
   ['70.61', '0.454']],
   'asks': [
     ['122.96', '0.381'],//[Price, Quantity]
     ['144.46', '1'],
     ['155.55', '0.065'],
     ['160.16', '0.052'],
     ['200', '0.775'],
     ['249', '0.17'],
     ['250', '1'],
     ['300', '1'],
     ['400', '1'],
     ['499', '1']]
   }

```


Retrieve the latest trades that have occurred for a specific option.

1

```
GET /openapi/quote/v1/option/trades
```


The number of trades returned

Maker or taker of the trade. `true`\= maker, `false` = taker

```
[
  {
    'price': '1.21',
    'time': 1555034474064,
    'qty': '0.725',
    'isBuyerMaker': False
  },...
]
```


Retrieves the kline information (open, high, trade volume, etc.) for a specific option.

1

```
GET /openapi/quote/v1/option/klines
```


Interval of the kline. Possible values include: `1m`,`5m`,`15m`,`30m`,`1h`,`1d`,`1w`,`1M`

Number of entries returned. Max is capped at 1000.

timestamp of the last datapoint

Taker buy base asset volume

Taker buy quote asset volume

```
[
  [
    1538728740000, //'opentime'
    '36.000000000000000000', //'open'
    '36.000000000000000000', //'high'
    '36.000000000000000000', //'low':
    '36.000000000000000000', //'close'
    '148976.11427815',  // Volume
    1499644799999,      // Close time
    '2434.19055334',    // Quote asset volume
    308,                // Number of trades
    '1756.87402397',    // Taker buy base asset volume
    '28.46694368'       // Taker buy quote asset volume
  ],...
]
```


`base asset` refers to the asset that is the quantity of a symbol.

`quote asset` refers to the asset that is the price of a symbol.

Private Options Endpoints


-----------------------------

Places a buy order for an option. This API endpoint requires your request to be signed.

1

```
POST /openapi/openapi/option/order
```


A unique ID of the order. Automatically generated if not sent.

Direction of the order. Possible values include `BUY` and `SELL`.

The order type, possible types: `LIMIT`, `MARKET`

Time in force. Possible values include `GTC`,`FOK`,`IOC`.

`NO` Required for limit orders

The number of contracts to buy

You can get options' price, quantity configuration data in the `exchange` endpoint.

Timestamp when the order is created.

Last time this order was updated

A unique ID of the order.

Quantity of orders that has been executed

Average price of filled orders.

The order type, possible types: `LIMIT`, `MARKET`

Direction of the order. Possible values include `BUY` or `SELL`

The state of the order.Possible values include `NEW`, `PARTIALLY_FILLED`, `FILLED`, `CANCELED`, and `REJECTED`.

Time in force. Possible values include `GTC`,`FOK`,`IOC`.

Fees incurred for this order.

In the `fees` field:

Actual transaction fees occurred.

```
{
    'time':1541161088303,
    'updateTime': 1541161088303,
    'orderId': 28,
    'clientOrderId': 213443,
    'symbol': 'BTC0412CS4200',
    'price': 102.32,
    'origQty': 21.3,
    'executedQty': 10.2,
    'avgPrice': 3121.13
    'type': 'LIMIT',
    'side': 'SELL',
    'status': 'NEW',
    'timeInForce': 'GTC',
    'fees':[]
}
```


Cancels an order, specified by `orderId` or `clientOrderId`. This API endpoint requires your request to be signed.

1

```
DELETE /openapi/option/v1/order/cancel
```


The order ID of the order to be canceled

One **MUST** be provided of these two parameters.

Timestamp when order request is submitted (ms).

Last time this order was updated (ms)

Quantity of orders that has been executed

Average price of filled orders.

The order type, possible types: `LIMIT`, `MARKET`

Direction of the order. Possible values include `BUY` or `SELL`

The state of the order.Possible values include `NEW`, `PARTIALLY_FILLED`, `FILLED`, `CANCELED`, and `REJECTED`.

Time in force. Possible values include `GTC`,`FOK`,`IOC`.

Fees incurred for this order.

In the `fees` field:

Actual transaction fees occurred.

```
{
  'time':1541161088303,
  'updateTime': 1541161088303,
  'orderId': 713637304,
  'clientOrderId': 213443,
  'symbol': 'BTC0412CS4200',
  'price': 102.32,
  'origQty': 21.3,
  'executedQty': 10.2,
  'avgPrice': 3121.13
  'type': 'LIMIT',
  'side': 'SELL',
  'status': 'CANCELED', //status will always be `CANCELED` for cancel request
  'timeInForce': 'GTC',
  'fees': []
}
```


Retrieves open orders. This API endpoint requires your request to be signed.

1

```
GET /openapi/option/v1/openOrders
```


Symbol to return open orders for. If not sent, orders of all options will be returned.

Direction of the order, possible values include `BUY` and `SELL`.

Order types to return, possible values include `LIMIT` and `MARKET`.

Number of entries to return.

If `orderId` is set, it will get orders < that `orderId`. Otherwise most recent orders are returned.

Timestamp when order request is submitted (ms).

Last time this order was updated (ms)

Quantity of orders that has been executed

Average price of filled orders.

The order type, possible types: `LIMIT`, `MARKET`

Direction of the order. Possible values include `BUY` or `SELL`

The state of the order.Possible values include `NEW`, `PARTIALLY_FILLED`, `FILLED`, `CANCELED`, and `REJECTED`.

Time in force. Possible values include `GTC`,`FOK`,`IOC`.

Fees incurred for this order.

In the `fees` field:

Actual transaction fees occurred.

```
[
  {
    'time': '1554948456641',
    'updateTime': '0',
    'orderId': '337326535438529024',
    'clientOrderId': '19524737',
    'symbol': 'BTC0412CS4200',
    'price': '1.98',
    'origQty': '1',
    'executedQty': '0',
    'avgPrice': '0',
    'type': 'LIMIT',
    'side': 'BUY',
    'status': 'NEW',
    'timeInForce': 'GTC',
    'fees': []
  },...

]
```


Retrieves current positions. This API endpoint requires your request to be signed.

1

```
GET /openapi/option/v1/positions
```


Name of the option. If not sent, positions for all options will be returned.

For each unique `symbol`, this endpoint will return the following information.

The position of the option. Can be negative (short) or positive (long)

Total margin amount for position held.

Settlement timestamp of the option.

Strike price of the option.

Number of option contracts that can be closed.

Average price for the position

Profit or loss for holding the position.

**Long Position:** `changed`/`averagePrice` **Short Position:** (`changed` \* `position`) / (`margin` - `averagePrice` \* `position`)

Current index price of the underlying asset.

```
[
  {
    'symbol': 'BTC0412CS4200',
    'position': '-10.760',
    'margin': '5380',
    'settlementTime': '1555056000000',
    'strikePrice': '4200',
    'price': '500.00',
    'availablePosition': '10.76',
    'averagePrice': '126.56',
    'changedRate': '-100.00',
    'changed': '-4018.21',
    'index': '5012.28666667'
  },...
]
```


Retrieves history of orders that have been partially or fully filled or canceled. This API endpoint requires your request to be signed.

1

```
GET /openapi/option/v1/historyOrders
```


Name of the option. If not sent, orders of all options will be returned.

Direction of the order. Possible values include `BUY` and `SELL`.

Order Type. Possible values include `LIMIT` and `MARKET`.

Status of the order. Possible values include `PARTIALLY_FILLED`, `FILLED`, and `CANCELED`.

Number of items to be returned

Timestamp when order request is submitted (ms).

Last time this order was updated

Quantity of orders that has been executed

Average price of filled orders.

The order type, possible types: `LIMIT`, `MARKET`

Direction of the order. Possible values include `BUY` or `SELL`

The state of the order.Possible values include `NEW`, `PARTIALLY_FILLED`, `FILLED`, `CANCELED`, and `REJECTED`.

Time in force. Possible values include `GTC`,`FOK`,`IOC`.

Fees incurred for this order.

In the `fees` field:

Actual transaction fees occurred.

```
{
  [
    {
      'time':1541161088303,
      'updateTime': 1541161088303,
      'orderId': 28,
      'clientOrderId': 213443,
      'symbol': 'BTC0412CS4200',
      'price': 102.32,
      'origQty': 21.3,
      'executedQty': 10.2,
      'avgPrice': 3121.13
      'type': 'LIMIT',
      'side': 'SELL',
      'status': 'NEW',
      'timeInForce': 'GTC',
      'fees':[]
    },...
  ]
}
```


Get details on a specific order, regardless of order state.

1

```
GET /openapi/option/v1/getOrder
```


Order ID. **Either** `**orderId**` **or** `**clientOrderId**` **must be sent**

Unique client customized ID of the order. **Either** `**orderId**` **or** `**clientOrderId**` **must be sent**

Timestamp when order request is submitted (ms).

Last time this order was updated

Quantity of orders that has been executed

Average price of filled orders.

The order type, possible types: `LIMIT`, `MARKET`

Direction of the order. Possible values include `BUY` or `SELL`

The state of the order.Possible values include `NEW`, `PARTIALLY_FILLED`, `FILLED`, `CANCELED`, and `REJECTED`.

Time in force. Possible values include `GTC`,`FOK`,`IOC`.

Fees incurred for this order.

In the `fees` field:

Actual transaction fees occurred.

```
{
  'time':1541161088303,
  'updateTime': 1541161088303,
  'orderId': 28,
  'clientOrderId': 213443,
  'symbol': 'BTC0412CS4200',
  'price': 102.32,
  'origQty': 21.3,
  'executedQty': 10.2,
  'avgPrice': 3121.13
  'type': 'LIMIT',
  'side': 'SELL',
  'status': 'NEW',
  'timeInForce': 'GTC',
  'fees':[]
}
```


Retrieve the trade history of the account. This API endpoint requires your request to be signed.

1

```
GET /openapi/option/v1/myTrades
```


Name of the option. If not sent, trades for all symbols will be returned.

The number of trades returned (clamped to max 1000)

The timestamp of the trade（ms）

Trade side from the user's point of view. Possible values include `BUY` and `SELL`

The order type, possible types: `LIMIT`, `MARKET`

```
[
  {
    'time': '1554897921663',
    'tradeId': '336902617393292032',
    'orderId': '336902617267462912',
    "matchOrderId": 336002617267469062,
    'price': '99',
    'quantity': '11.414',
    'feeTokenName': 'BUSDT',
    'fee': '0.1129986',
    'type': 'LIMIT',
    'side': 'BUY',
    'symbol': 'BTC0412PS3900'
  },...
]
```


Retrieves settlement events that have affected your account. This API endpoint requires your request to be signed.

1

```
GET  /openapi/option/v1/settlements
```


None

Type of the option. Possible values include: 'call' and 'put'

The timestamp of the settlement.

Strike price of the option

Settlement price (EDP, which is the average index price in the last 10 minutes) at time of settlement.

Maximum payoff of the option

Average price for the position

Settlement payoff of the option

**Long Position**: `changed`/(averagePrice \* position). **Short Position**: `changed`/(`margin` - averagePrice \* position)

```
[
  {'symbol': 'BTC0405PS3850',
  'optionType': 'put',
  'margin': '0',
  'timestamp': '1554451200000',
  'strikePrice': '3850',
  'settlementPrice': '4956.54',
  'maxPayOff': '500',
  'averagePrice': '119.27',
  'position': '0',
  'changed': '0',
  'changedRate': '0'},...
  ]       
```


This endpoint is used to retrieve options account balance. This endpoint requires you to be signed.

1

```
GET  /openapi/option/v1/account
```


None

Total asset value in option account quoted in USDT.

Total option value quoted in USDT

In the `balances` field:

Amount locked (for open orders)

Amount used for margin (for short positions)

```
{
  'totalAsset': '8533.0606762',
  'optionAsset': '558.1832',
  'balances': [
    {
      'tokenName': 'USDT',
      'free': '0.0',
      'locked': '0.0',
      'margin': '0.0'
    },
    {
      'tokenName': 'BUSDT',
      'free': '7961.9951881',
      'locked': '12.8822881',
      'margin': '5798.0'
    },...
  ]
}
```


Last updated 11 months ago

# Public Rest API (2018-09-25) | TruBit Pro
1.  [Spot](https://docs-api.trubit.com/trubit-pro/spot)

Public Rest API (2018-09-25)
----------------------------

*   All endpoints return either a JSON object or array.
    
*   Data is returned in **ascending** order. Oldest first, newest last.
    
*   All time and timestamp related fields are in milliseconds.
    
*   HTTP `4XX` return codes are used for for malformed requests; the issue is on the sender's side.
    
*   HTTP `429` return code is used when breaking a request rate limit.
    
*   HTTP `418` return code is used when an IP has been auto-banned for continuing to send requests after receiving `429` codes.
    
*   HTTP `5XX` return codes are used for internal errors; the issue is on exchange's side. It is important to **NOT** treat this as a failure operation; the execution status is **UNKNOWN** and could have been a success.
    
*   Any endpoint can return an ERROR; the error payload is as follows:
    

```
{
  "code": -1121,
  "msg": "Invalid symbol."
}
```


*   Specific error codes and messages defined in another document.
    
*   For `GET` endpoints, parameters must be sent as a `query string`.
    
*   For `POST`, `PUT`, and `DELETE` endpoints, the parameters may be sent as a `query string` or in the `request body` with content type `application/x-www-form-urlencoded`. You may mix parameters between both the `query string` and `request body` if you wish to do so.
    
*   Parameters may be sent in any order.
    
*   If a parameter sent in both the `query string` and `request body`, the `query string` parameter will be used.
    

*   The `/openapi/v1/exchange` `rateLimits` array contains objects related to the exchange's `REQUEST_WEIGHT` and `ORDER` rate limits.
    
*   A 429 will be returned when either rate limit is violated.
    
*   Each route has a `weight` which determines for the number of requests each endpoint counts for. Heavier endpoints and endpoints that do operations on multiple symbols will have a heavier `weight`.
    
*   When a 429 is recieved, it's your obligation as an API to back off and not spam the API.
    
*   **Repeatedly violating rate limits and/or failing to back off after receiving 429s will result in an automated IP ban (http status 418).**
    
*   IP bans are tracked and **scale in duration** for repeat offenders, **from 2 minutes to 3 days**.
    

*   Each endpoint has a security type that determines the how you will interact with it.
    
*   API-keys are passed into the Rest API via the `X-BH-APIKEY` header.
    
*   API-keys and secret-keys **are case sensitive**.
    
*   API-keys can be configured to only access certain types of secure endpoints. For example, one API-key could be used for TRADE only, while another API-key can access everything except for TRADE routes.
    
*   By default, API-keys can access all secure routes.
    

Endpoint can be accessed freely.

Endpoint requires sending a valid API-Key and signature.

Endpoint requires sending a valid API-Key and signature.

Endpoint requires sending a valid API-Key.

Endpoint requires sending a valid API-Key.

*   `TRADE` and `USER_DATA` endpoints are `SIGNED` endpoints.
    

### 

SIGNED (TRADE and USER\_DATA) Endpoint security

*   `SIGNED` endpoints require an additional parameter, `signature`, to be sent in the `query string` or `request body`.
    
*   Endpoints use `HMAC SHA256` signatures. The `HMAC SHA256 signature` is a keyed `HMAC SHA256` operation. Use your `secretKey` as the key and `totalParams` as the value for the HMAC operation.
    
*   The `signature` is **not case sensitive**.
    
*   `totalParams` is defined as the `query string` concatenated with the `request body`.
    

*   A `SIGNED` endpoint also requires a parameter, `timestamp`, to be sent which should be the millisecond timestamp of when the request was created and sent.
    
*   An additional parameter, `recvWindow`, may be sent to specify the number of milliseconds after `timestamp` the request is valid for. If `recvWindow` is not sent, **it defaults to 5000**.
    
*   Currently, `recvWindow` is only used when creates order.
    
*   The logic is as follows:
    
    ```
if (timestamp < (serverTime + 1000) && (serverTime - timestamp) <= recvWindow) {
  // process request
} else {
  // reject request
}
```

    

**Serious trading is about timing.** Networks can be unstable and unreliable, which can lead to requests taking varying amounts of time to reach the servers. With `recvWindow`, you can specify that the request must be processed within a certain number of milliseconds or be rejected by the server.

**It recommended to use a small recvWindow of 5000 or less!**

### 

SIGNED Endpoint Examples for POST /openapi/v1/order

Here is a step-by-step example of how to send a vaild signed payload from the Linux command line using `echo`, `openssl`, and `curl`.

tAQfOrPIZAhym0qHISRt8EFvxPemdBm5j5WMlkm3Ke9aFp0EGWC2CGM8GHV4kCYW

lH3ELTNiFxCQTmi9pPcWWikhsjO04Yoqw3euoHUuOLC3GYBW64ZqzQsiOEHXQS76

#### 

Example 1: As a query string

*   **queryString:** symbol=ETHBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1538323200000
    

```
[linux]$ echo -n "symbol=ETHBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1538323200000" | openssl dgst -sha256 -hmac "lH3ELTNiFxCQTmi9pPcWWikhsjO04Yoqw3euoHUuOLC3GYBW64ZqzQsiOEHXQS76"
(stdin)= 5f2750ad7589d1d40757a55342e621a44037dad23b5128cc70e18ec1d1c3f4c6
```


```
(HMAC SHA256)
[linux]$ curl -H "X-BH-APIKEY: tAQfOrPIZAhym0qHISRt8EFvxPemdBm5j5WMlkm3Ke9aFp0EGWC2CGM8GHV4kCYW" -X POST 'https://$HOST/openapi/v1/order?symbol=ETHBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1538323200000&signature=5f2750ad7589d1d40757a55342e621a44037dad23b5128cc70e18ec1d1c3f4c6'
```


#### 

Example 2: As a request body

*   **requestBody:** symbol=ETHBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1538323200000
    

```
[linux]$ echo -n "symbol=ETHBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1538323200000" | openssl dgst -sha256 -hmac "lH3ELTNiFxCQTmi9pPcWWikhsjO04Yoqw3euoHUuOLC3GYBW64ZqzQsiOEHXQS76"
(stdin)= 5f2750ad7589d1d40757a55342e621a44037dad23b5128cc70e18ec1d1c3f4c6
```


```
(HMAC SHA256)
[linux]$ curl -H "X-BH-APIKEY: tAQfOrPIZAhym0qHISRt8EFvxPemdBm5j5WMlkm3Ke9aFp0EGWC2CGM8GHV4kCYW" -X POST 'https://$HOST/openapi/v1/order' -d 'symbol=ETHBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1538323200000&signature=5f2750ad7589d1d40757a55342e621a44037dad23b5128cc70e18ec1d1c3f4c6'
```


#### 

Example 3: Mixed query string and request body

*   **queryString:** symbol=ETHBTC&side=BUY&type=LIMIT&timeInForce=GTC
    
*   **requestBody:** quantity=1&price=0.1&recvWindow=5000&timestamp=1538323200000
    

```
[linux]$ echo -n "symbol=ETHBTC&side=BUY&type=LIMIT&timeInForce=GTCquantity=1&price=0.1&recvWindow=5000&timestamp=1538323200000" | openssl dgst -sha256 -hmac "lH3ELTNiFxCQTmi9pPcWWikhsjO04Yoqw3euoHUuOLC3GYBW64ZqzQsiOEHXQS76"
(stdin)= 885c9e3dd89ccd13408b25e6d54c2330703759d7494bea6dd5a3d1fd16ba3afa
```


```
(HMAC SHA256)
[linux]$ curl -H "X-BH-APIKEY: tAQfOrPIZAhym0qHISRt8EFvxPemdBm5j5WMlkm3Ke9aFp0EGWC2CGM8GHV4kCYW" -X POST 'https://$HOST/openapi/v1/order?symbol=ETHBTC&side=BUY&type=LIMIT&timeInForce=GTC' -d 'quantity=1&price=0.1&recvWindow=5000&timestamp=1538323200000&signature=885c9e3dd89ccd13408b25e6d54c2330703759d7494bea6dd5a3d1fd16ba3afa'
```


Note that the signature is different in example 3. There is no & between "GTC" and "quantity=1".

*   `base asset` refers to the asset that is the `quantity` of a symbol.
    
*   `quote asset` refers to the asset that is the `price` of a symbol.
    

**Symbol status:**

**Symbol type:**

**Asset type:**

**Order status:**

**Order types:**

*   STOP\_LOSS (unavailable now)
    
*   STOP\_LOSS\_LIMIT (unavailable now)
    
*   TAKE\_PROFIT (unavailable now)
    
*   TAKE\_PROFIT\_LIMIT (unavailable now)
    
*   MARKET\_OF\_PAYOUT (unavailable now)
    

**Order side:**

**Time in force:**

**Kline/Candlestick chart intervals:**

m -> minutes; h -> hours; d -> days; w -> weeks; M -> months

**Rate limiters (rateLimitType)**

**Rate limit intervals**

Test connectivity to the Rest API.

**Weight:** 0

**Parameters:** NONE

**Response:**

Test connectivity to the Rest API and get the current server time.

**Weight:** 0

**Parameters:** NONE

**Response:**

```
{
  "serverTime": 1538323200000
}
```


Current trading rules and symbol information

**Weight:** 0

**Parameters:** NONE

**Response:**

```
{
  "timezone": "UTC",
  "serverTime": 1538323200000,
  "rateLimits": [{
      "rateLimitType": "REQUESTS_WEIGHT",
      "interval": "MINUTE",
      "limit": 1500
    },
    {
      "rateLimitType": "ORDERS",
      "interval": "SECOND",
      "limit": 20
    },
    {
      "rateLimitType": "ORDERS",
      "interval": "DAY",
      "limit": 350000
    }
  ],
  "brokerFilters":[],
  "symbols": [{
    "symbol": "ETHBTC",
    "status": "TRADING",
    "baseAsset": "ETH",
    "baseAssetPrecision": "0.001",
    "quoteAsset": "BTC",
    "quotePrecision": "0.01",
    "icebergAllowed": false,
    "filters": [{
      "filterType": "PRICE_FILTER",
      "minPrice": "0.00000100",
      "maxPrice": "100000.00000000",
      "tickSize": "0.00000100"
    }, {
      "filterType": "LOT_SIZE",
      "minQty": "0.00100000",
      "maxQty": "100000.00000000",
      "stepSize": "0.00100000"
    }, {
      "filterType": "MIN_NOTIONAL",
      "minNotional": "0.00100000"
    }]
  }]
}
```


```
GET /openapi/quote/v1/depth
```


**Weight:** Adjusted based on the limit:

**Parameters:**

**Caution:** setting limit=0 can return a lot of data.

**Response:**

\[PRICE, QTY\]

```
{
  "bids": [
    [
      "3.90000000",   // PRICE
      "431.00000000"  // QTY
    ],
    [
      "4.00000000",
      "431.00000000"
    ]
  ],
  "asks": [
    [
      "4.00000200",  // PRICE
      "12.00000000"  // QTY
    ],
    [
      "5.10000000",
      "28.00000000"
    ]
  ]
}
```


```
GET /openapi/quote/v1/trades
```


Get recent trades (up to last 500).

**Weight:** 1

**Parameters:**

**Response:**

```
[
  {
    "price": "4.00000100",
    "qty": "12.00000000",
    "time": 1499865549590,
    "isBuyerMaker": true
  }
]
```


```
GET /openapi/quote/v1/klines
```


Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time.

**Weight:** 1

**Parameters:**

*   If startTime and endTime are not sent, the most recent klines are returned.
    

**Response:**

```
[
  [
    1499040000000,      // Open time
    "0.01634790",       // Open
    "0.80000000",       // High
    "0.01575800",       // Low
    "0.01577100",       // Close
    "148976.11427815",  // Volume
    1499644799999,      // Close time
    "2434.19055334",    // Quote asset volume
    308                // Number of trades
  ]
]
```


#### 

24hr ticker price change statistics

```
GET /openapi/quote/v1/ticker/24hr
```


24 hour price change statistics. **Careful** when accessing this with no symbol.

**Weight:** 1 for a single symbol; **40** when the symbol parameter is omitted

**Parameters:**

*   If the symbol is not sent, tickers for all symbols will be returned in an array.
    

**Response:**

```
{
  "time": 1538725500422,
  "symbol": "ETHBTC",
  "bestBidPrice": "4.00000200",
  "bestAskPrice": "4.00000200",
  "lastPrice": "4.00000200",
  "openPrice": "99.00000000",
  "highPrice": "100.00000000",
  "lowPrice": "0.10000000",
  "volume": "8913.30000000"
}
```


OR

```
[
  {
    "time": 1538725500422,
    "symbol": "ETHBTC",
    "lastPrice": "4.00000200",
    "openPrice": "99.00000000",
    "highPrice": "100.00000000",
    "lowPrice": "0.10000000",
    "volume": "8913.30000000"
 }
]
```


```
GET /openapi/quote/v1/ticker/price
```


Latest price for a symbol or symbols.

**Weight:** 1

**Parameters:**

*   If the symbol is not sent, prices for all symbols will be returned in an array.
    

**Response:**

```
{
  "price": "4.00000200"
}
```


OR

```
[
  {
    "symbol": "LTCBTC",
    "price": "4.00000200"
  },
  {
    "symbol": "ETHBTC",
    "price": "0.07946600"
  }
]
```


```
GET /openapi/quote/v1/ticker/bookTicker
```


Best price/qty on the order book for a symbol or symbols.

**Weight:** 1

**Parameters:**

*   If the symbol is not sent, bookTickers for all symbols will be returned in an array.
    

**Response:**

```
{
  "symbol": "LTCBTC",
  "bidPrice": "4.00000000",
  "bidQty": "431.00000000",
  "askPrice": "4.00000200",
  "askQty": "9.00000000"
}
```


OR

```
[
  {
    "symbol": "LTCBTC",
    "bidPrice": "4.00000000",
    "bidQty": "431.00000000",
    "askPrice": "4.00000200",
    "askQty": "9.00000000"
  },
  {
    "symbol": "ETHBTC",
    "bidPrice": "0.07946700",
    "bidQty": "9.00000000",
    "askPrice": "100000.00000000",
    "askQty": "1000.00000000"
  }
]
```


```
POST /openapi/v1/order  (HMAC SHA256)
```


Send in a new order.

**Weight:** 1

**Parameters:**

A unique id for the order. Automatically generated if not sent.

Used with `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` orders. Unavailable

Used with `LIMIT`, `STOP_LOSS_LIMIT`, and `TAKE_PROFIT_LIMIT` to create an iceberg order. Unavailable

Additional mandatory parameters based on `type`:

Additional mandatory parameters

`timeInForce`, `quantity`, `price`

`timeInForce`, `quantity`, `price`, `stopPrice`

`timeInForce`, `quantity`, `price`, `stopPrice`

Other info:

*   `LIMIT_MAKER` are `LIMIT` orders that will be rejected if they would immediately match and trade as a taker.
    
*   `STOP_LOSS` and `TAKE_PROFIT` will execute a `MARKET` order when the `stopPrice` is reached.
    
*   Any `LIMIT` or `LIMIT_MAKER` type order can be made an iceberg order by sending an `icebergQty`.
    
*   Any order with an `icebergQty` MUST have `timeInForce` set to `GTC`.
    

Trigger order price rules against market price for both MARKET and LIMIT versions:

*   Price above market price: `STOP_LOSS` `BUY`, `TAKE_PROFIT` `SELL`
    
*   Price below market price: `STOP_LOSS` `SELL`, `TAKE_PROFIT` `BUY`
    

**Response:**

```
{
  "orderId": 28,
  "clientOrderId": "6k9M212T12092"
}
```


```
POST /openapi/v1/order/test (HMAC SHA256)
```


Test new order creation and signature/recvWindow long. Creates and validates a new order but does not send it into the matching engine.

**Weight:** 1

**Parameters:**

Same as `POST /openapi/v1/order`

**Response:**

```
GET /openapi/v1/order (HMAC SHA256)
```


Check an order's status.

**Weight:** 1

**Parameters:**

Notes:

*   Either `orderId` or `origClientOrderId` must be sent.
    
*   For some historical orders `cummulativeQuoteQty` will be < 0, meaning the data is not available at this time.
    

**Response:**

```
{
  "symbol": "LTCBTC",
  "orderId": 1,
  "clientOrderId": "9t1M2K0Ya092",
  "price": "0.1",
  "origQty": "1.0",
  "executedQty": "0.0",
  "cummulativeQuoteQty": "0.0",
  "avgPrice": "0.0",
  "status": "NEW",
  "timeInForce": "GTC",
  "type": "LIMIT",
  "side": "BUY",
  "stopPrice": "0.0",
  "icebergQty": "0.0",
  "time": 1499827319559,
  "updateTime": 1499827319559,
  "isWorking": true
}
```


```
DELETE /openapi/v1/order  (HMAC SHA256)
```


Cancel an active order.

**Weight:** 1

**Parameters:**

Either `orderId` or `clientOrderId` must be sent.

**Response:**

```
{
  "symbol": "LTCBTC",
  "clientOrderId": "tU721112KM",
  "orderId": 1,
  "status": "CANCELED"
}
```


#### 

Current open orders (USER\_DATA)

```
GET /openapi/v1/openOrders  (HMAC SHA256)
```


GET all open orders on a symbol. **Careful** when accessing this with no symbol.

**Weight:** 1

**Parameters:**

**Notes:**

*   If `orderId` is set, it will get orders < that `orderId`. Otherwise most recent orders are returned.
    

**Response:**

```
[
  {
    "symbol": "LTCBTC",
    "orderId": 1,
    "clientOrderId": "t7921223K12",
    "price": "0.1",
    "origQty": "1.0",
    "executedQty": "0.0",
    "cummulativeQuoteQty": "0.0",
    "avgPrice": "0.0",
    "status": "NEW",
    "timeInForce": "GTC",
    "type": "LIMIT",
    "side": "BUY",
    "stopPrice": "0.0",
    "icebergQty": "0.0",
    "time": 1499827319559,
    "updateTime": 1499827319559,
    "isWorking": true
  }
]
```


#### 

History orders (USER\_DATA)

```
GET /openapi/v1/historyOrders (HMAC SHA256)
```


GET all orders of the account; canceled, filled or rejected.

**Weight:** 5

**Parameters:**

**Notes:**

*   If `orderId` is set, it will get orders < that `orderId`. Otherwise most recent orders are returned.
    

**Response:**

```
[
  {
    "symbol": "LTCBTC",
    "orderId": 1,
    "clientOrderId": "987yjj2Ym",
    "price": "0.1",
    "origQty": "1.0",
    "executedQty": "0.0",
    "cummulativeQuoteQty": "0.0",
    "avgPrice": "0.0",
    "status": "NEW",
    "timeInForce": "GTC",
    "type": "LIMIT",
    "side": "BUY",
    "stopPrice": "0.0",
    "icebergQty": "0.0",
    "time": 1499827319559,
    "updateTime": 1499827319559,
    "isWorking": true
  }
]
```


#### 

Account information (USER\_DATA)

```
GET /openapi/v1/account (HMAC SHA256)
```


GET current account information.

**Weight:** 5

**Parameters:**

**Response:**

```
{
  "canTrade": true,
  "canWithdraw": true,
  "canDeposit": true,
  "updateTime": 123456789,
  "balances": [
    {
      "asset": "BTC",
      "free": "4723846.89208129",
      "locked": "0.00000000"
    },
    {
      "asset": "LTC",
      "free": "4763368.68006011",
      "locked": "0.00000000"
    }
  ]
}
```


#### 

Account trade list (USER\_DATA)

```
GET /openapi/v1/myTrades  (HMAC SHA256)
```


GET trades for a specific account.

**Weight:** 5

**Parameters:**

**Notes:**

*   If only `fromId` is set，it will get orders < that `fromId` in descending order.
    
*   If only `toId` is set, it will get orders > that `toId` in ascending order.
    
*   If `fromId` is set and `toId` is set, it will get orders < that `fromId` and > that `toId` in descending order.
    
*   If `fromId` is not set and `toId` it not set, most recent order are returned in descending order.
    

**Response:**

```
[
  {
    "symbol": "ETHBTC",
    "id": 28457,
    "orderId": 100234,
    "matchOrderId": 109834,
    "price": "4.00000100",
    "qty": "12.00000000",
    "commission": "10.10000000",
    "commissionAsset": "ETH",
    "time": 1499865549590,
    "isBuyer": true,
    "isMaker": false,
    "feeTokenId": "ETH",
    "fee": "0.012"
  }
]
```


#### 

Account deposit list (USER\_DATA)

```
GET /openapi/v1/depositOrders  (HMAC SHA256)
```


GET deposit orders for a specific account.

**Weight:** 5

**Parameters:**

Deposit OrderId to fetch from. Default gets most recent deposit orders.

**Notes:**

*   If `fromId` is set, it will get orders > that `fromId`. Otherwise most recent orders are returned.
    

**Response:**

```
[
  {
	"orderId": 100234,
	"token": "EOS",
	"address": "deposit2bh",
	"addressTag": "19012584",
	"fromAddress": "clarkkent",
	"fromAddressTag": "19029901",
	"time": 1499865549590,
	"quantity": "1.01"
  }
]
```


### 

User data stream endpoints

Specifics on how user data streams work is in another document.

#### 

Start user data stream (USER\_STREAM)

```
POST /openapi/v1/userDataStream
```


Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent.

**Weight:** 1

**Parameters:**

**Response:**

```
{
  "listenKey": "1A9LWJjuMwKWYP4QQPw34GRm8gz3x5AephXSuqcDef1RnzoBVhEeGE963CoS1Sgj"
}
```


#### 

Keepalive user data stream (USER\_STREAM)

```
PUT /openapi/v1/userDataStream
```


Keepalive a user data stream to prevent a time out. User data streams will close after 60 minutes. It's recommended to send a ping about every 30 minutes.

**Weight:** 1

**Parameters:**

**Response:**

#### 

Close user data stream (USER\_STREAM)

```
DELETE /openapi/v1/userDataStream
```


Close out a user data stream.

**Weight:** 1

**Parameters:**

**Response:**

#### 

Sub-account list(SUB\_ACCOUNT\_LIST)

```
POST /openapi/v1/subAccount/query
```


Query sub-account lists

**Parameters:**

None

**Weight:** 5

**Response:**

```
[
    {
        "accountId": "122216245228131",
        "accountName": "",
        "accountType": 1,
        "accountIndex": 0 // main-account: 0, sub-account: 1
    },
    {
        "accountId": "482694560475091200",
        "accountName": "createSubAccountByCurl", // sub-account name
        "accountType": 1, // sub-account type 1. token trading 3. contract trading
        "accountIndex": 1
    },
    {
        "accountId": "422446415267060992",
        "accountName": "",
        "accountType": 3,
        "accountIndex": 0
    },
    {
        "accountId": "482711469199298816",
        "accountName": "createSubAccountByCurl",
        "accountType": 3,
        "accountIndex": 1
    },
]
```


#### 

Internal Account Transfer (ACCOUNT\_TRANSFER)

```
POST /openapi/v1/transfer
```


Internal transfer

**Weight:** 1

**Parameters:**

source account type: 1. token trading account 2.Options account 3. Contracts account

sub-account index(valid when using main-account api, get sub-account indices from `SUB_ACCOUNT_LIST` endpoint)

Target account type: 1. token trading account 2.Options account 3. Contracts account

sub-account index(valid when using main-account api, get sub-account indices from `SUB_ACCOUNT_LIST` endpoint)

**Response:**

```
{
    "success":"true" // success
}
```


**Explanation**

1.  Either transferring or receiving account must be the main account (Token trading account)
    
2.  Main account api can support transferring to other account(including sub-accounts) and receiving from other accounts
    
3.  **Sub-account API only supports transferring from current account to the main-account. Therefore** `**fromAccountType\fromAccountIndex\toAccountType\toAccountIndex**` **should be left empty.**
    

#### 

Check Balance Flow (BALANCE\_FLOW)

```
POST /openapi/v1/balance_flow
```


Check blance flow

**Weight:** 5

**Parameters:**

**Response:**

```
[
    {
        "id": "539870570957903104",
        "accountId": "122216245228131",
        "tokenId": "BTC",
        "tokenName": "BTC",
        "flowTypeValue": 51, // balance flow type
        "flowType": "USER_ACCOUNT_TRANSFER", // balance flow type name
        "flowName": "Transfer", // balance flow type Explanation
        "change": "-12.5", // change
        "total": "379.624059937852365", // total asset after change
        "created": "1579093587214"
    },
    {
        "id": "536072393645448960",
        "accountId": "122216245228131",
        "tokenId": "USDT",
        "tokenName": "USDT",
        "flowTypeValue": 7,
        "flowType": "AIRDROP",
        "flowName": "Airdrop",
        "change": "-2000",
        "total": "918662.0917630848",
        "created": "1578640809195"
    }
]
```


**Explanation**

1.  Main-account API can query balance flow for token account and other accounts(including sub-accounts, or designated `accountType` and `accountIndex` accounts)
    
2.  Sub-account API can only query current sub-account, therefore `accountType` and `accountIndex` is not required.
    

**Please see the following for balance flow types**

userAccountTransfer 专用，流水没有subjectExtId

INVITATION\_REFERRAL\_BONUS

Filters define trading rules on a symbol. Filters come in two forms: `symbol filters` and `broker filters`.

**PRICE\_FILTER**

The `PRICE_FILTER` defines the `price` rules for a symbol. There are 3 parts:

*   `minPrice` defines the minimum `price`/`stopPrice` allowed.
    
*   `maxPrice` defines the maximum `price`/`stopPrice` allowed.
    
*   `tickSize` defines the intervals that a `price`/`stopPrice` can be increased/decreased by.
    

In order to pass the `price filter`, the following must be true for `price`/`stopPrice`:

*   (`price`\-`minPrice`) % `tickSize` == 0
    

**/exchange format:**

```
  {
    "filterType": "PRICE_FILTER",
    "minPrice": "0.00000100",
    "maxPrice": "100000.00000000",
    "tickSize": "0.00000100"
  }
```


**LOT\_SIZE**

The `LOT_SIZE` filter defines the `quantity` (aka "lots" in auction terms) rules for a symbol. There are 3 parts:

*   `minQty` defines the minimum `quantity`/`icebergQty` allowed.
    
*   `maxQty` defines the maximum `quantity`/`icebergQty` allowed.
    
*   `stepSize` defines the intervals that a `quantity`/`icebergQty` can be increased/decreased by.
    

In order to pass the `lot size`, the following must be true for `quantity`/`icebergQty`:

*   (`quantity`\-`minQty`) % `stepSize` == 0
    

**/exchange format:**

```
  {
    "filterType": "LOT_SIZE",
    "minQty": "0.00100000",
    "maxQty": "100000.00000000",
    "stepSize": "0.00100000"
  }
```


**MIN\_NOTIONAL**

The `MIN_NOTIONAL` filter defines the minimum notional value allowed for an order on a symbol. An order's notional value is the `price` \* `quantity`.

**/exchange format:**

```
  {
    "filterType": "MIN_NOTIONAL",
    "minNotional": "0.00100000"
  }
```


**MAX\_NUM\_ORDERS**

The `MAX_NUM_ORDERS` filter defines the maximum number of orders an account is allowed to have open on a symbol. Note that both "algo" orders and normal orders are counted for this filter.

**/exchange format:**

```
  {
    "filterType": "MAX_NUM_ORDERS",
    "limit": 25
  }
```


**MAX\_NUM\_ALGO\_ORDERS**

The `MAX_ALGO_ORDERS` filter defines the maximum number of "algo" orders an account is allowed to have open on a symbol. "Algo" orders are `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` orders.

**/exchange format:**

```
  {
    "filterType": "MAX_NUM_ALGO_ORDERS",
    "maxNumAlgoOrders": 5
  }
```


**ICEBERG\_PARTS**

The `ICEBERG_PARTS` filter defines the maximum parts an iceberg order can have. The number of `ICEBERG_PARTS` is defined as `CEIL(qty / icebergQty)`.

**/exchange format:**

```
  {
    "filterType": "ICEBERG_PARTS",
    "limit": 10
  }
```


**BROKER\_MAX\_NUM\_ORDERS**

The `MAX_NUM_ORDERS` filter defines the maximum number of orders an account is allowed to have open on the exchange. Note that both "algo" orders and normal orders are counted for this filter.

**/exchange format:**

```
  {
    "filterType": "BROKER_MAX_NUM_ORDERS",
    "limit": 1000
  }
```


**BROKER\_MAX\_NUM\_ALGO\_ORDERS**

The `MAX_ALGO_ORDERS` filter defines the maximum number of "algo" orders an account is allowed to have open on the exchange. "Algo" orders are `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` orders.

**/exchange format:**

```
  {
    "filterType": "BROKER_MAX_NUM_ALGO_ORDERS",
    "limit": 200
  }
```


```
POST /openapi/v1/user/transfer
```


Last updated 11 months ago

# User Data Streams | TruBit Pro
1.  [Spot](https://docs-api.trubit.com/trubit-pro/spot)

User Data Streams
-----------------

*   A User Data Stream `listenKey` is valid for 60 minutes after creation.
    
*   Doing a `PUT` on a `listenKey` will extend its validity for 60 minutes.
    
*   Doing a `DELETE` on a `listenKey` will close the stream.
    
*   User Data Streams are accessed at **/openapi/ws/<listenKey>**
    
*   A single connection to api endpoint is only valid for 24 hours; expect to be disconnected at the 24 hour mark
    
*   User data stream payloads are **not guaranteed** to be in order during heavy periods; **make sure to order your updates using E**
    

```
POST /openapi/v1/userDataStream
```


Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent.

**Weight:** 1

**Parameters:**

**Response:**

```
{
  "listenKey": "1A9LWJjuMwKWYP4QQPw34GRm8gz3x5AephXSuqcDef1RnzoBVhEeGE963CoS1Sgj"
}
```


### 

Ping/Keep-alive a listenKey

```
PUT /openapi/v1/userDataStream
```


Keepalive a user data stream to prevent a time out. User data streams will close after 60 minutes. It's recommended to send a ping about every 30 minutes.

**Weight:** 1

**Parameters:**

**Response:**

```
DELETE /openapi/v1/userDataStream
```


Close out a user data stream.

**Weight:** 1

**Parameters:**

**Response:**

Account state is updated with the `outboundAccountInfo` event.

**Payload:**

```
{
  "e": "outboundAccountInfo",   // Event type
  "E": 1499405658849,           // Event time
  // "m": 0,                       // Maker commission rate (bips)
  // "t": 0,                       // Taker commission rate (bips)
  // "b": 0,                       // Buyer commission rate (bips)
  // "s": 0,                       // Seller commission rate (bips)
  "T": true,                    // Can trade?
  "W": true,                    // Can withdraw?
  "D": true,                    // Can deposit?
  // "u": 1499405658848,           // Time of last account update
  "B": [                        // Balances changed
    {
      "a": "LTC",               // Asset
      "f": "17366.18538083",    // Free amount
      "l": "0.00000000"         // Locked amount
    }
  ]
}
```


Orders are updated with the `executionReport` event. Check the API documentation and below for relevant enum definitions. Average price can be found by doing `Z` divided by `z`.

**Payload:**

```
{
  "e": "executionReport",        // Event type
  "E": 1499405658658,            // Event time
  "s": "ETHBTC",                 // Symbol
  "c": 1000087761,               // Client order ID
  "S": "BUY",                    // Side
  "o": "LIMIT",                  // Order type
  "f": "GTC",                    // Time in force
  "q": "1.00000000",             // Order quantity
  "p": "0.10264410",             // Order price
  // "P": "0.00000000",             // Stop price
  // "F": "0.00000000",             // Iceberg quantity
  // "g": -1,                       // Ignore
  // "x": "NEW",                    // Current execution type
  "X": "NEW",                    // Current order status
  // "r": "NONE",                   // Order reject reason; will be an error code.
  "i": 4293153,                  // Order ID
  "l": "0.00000000",             // Last executed quantity
  "z": "0.00000000",             // Cumulative filled quantity
  "L": "0.00000000",             // Last executed price
  "n": "0",                      // Commission amount
  "N": null,                     // Commission asset
  "u": true,                     // Is the trade normal, ignore for now
  // "T": 1499405658657,            // Transaction time
  // "t": -1,                       // Trade ID
  // "I": 8641984,                  // Ignore
  "w": true,                     // Is the order working? Stops will have
  "m": false,                    // Is this trade the maker side?
  // "M": false,                    // Ignore
  "O": 1499405658657,            // Order creation time
  "Z": "0.00000000"              // Cumulative quote asset transacted quantity
}
```


**Execution types:**

Last updated 11 months ago

# Web Socket Streams (2019-08-12) | TruBit Pro
1.  [Spot](https://docs-api.trubit.com/trubit-pro/spot)

Web Socket Streams (2019-08-12)
-------------------------------

*   The base endpoint is [here](https://github.com/Galactic-Tech/GitBook/blob/main/Spot/endpoint.md)
    
*   Raw streams are accessed at **/openapi/quote/ws/v1**
    

realtimes, trade, kline\_$interval, depth

1m, 5m, 15m, 30m, 1h, 2h, 6h, 12h, 1d, 1w, 1M

**Sample Subscription Data:**

```
{
  "symbol" : "$symbol0, $symbol1",
  "topic" : "$topic",
  "event" : "sub",
  // customizable parameter
  "params" : {
      // kline max limit is 2000, default is 1
      "limit" : "$limit",
      // Whether data is returned in binary format, default to false
      "binary" : "false"
  }
}
```


Specify number of entries returned

Whether returned values is in binary format. **DEFAULT** value is **false**

The client need to send a `PING` message to the server regularly through the Websocket, which then the server replies with `PONG`. If the client does not send the message every 5 minutes, the server will close the connection.

```
{
    "ping": 1535975085052
}
```


```
{
    "pong": 1535975085052
}
```


The Trade Streams push raw trade information; each trade has a unique buyer and seller.

After successful handshake and connected to server, the server will return the latest 60 trades. After this payload, the following will be real-time trades.

Variable "v" acts as an tradeId. This variable is shared across different symbols; however, each ID is unique. For example, suppose in the last 5 seconds 3 trades happened in ETHSUDT, BTCUSDT, and BHTBTC. Their version (which is "v") will be consecutive: 112, 113, 114.

**Subscription message structure:**

```
{
  "symbol": "$symbol0, $symbol1",
  "topic": "trade",
  "event": "sub",
  "params": {
    "binary": false // Whether data returned is in binary format
  }
}
```


**Payload:**

```
{
  "symbol": "BTCUSDT",
  "topic": "trade",
  "data": [{
    "v": "426635153180475392", // Version
    "t": 1565594873508,  //Timestamp
    "p": "11369", // Price
    "q": "0.01", // Quantity
    "m": false // true = buy, false = sell
  }, {
    "v": "426635153373413376",
    "t": 1565594873531,
    "p": "11369",
    "q": "0.0012",
    "m": false
  }],
  "f": false // Whether this is the first entry
}
```


24hr Ticker statistics for a symbol that changed in an array.

**Subscription message structure:**

```
{
  "symbol": "$symbol0, $symbol1",
  "topic": "realtimes",
  "event": "sub",
  "params": {
    "binary": false
  }
}
```


**Payload:**

```
{
  "symbol": "ETHUSDT",
  "topic": "realtimes",
  "data": [{
    "t": "1565592599015", //time
    "s": "ETHUSDT", //symbol
    "c": "212.63", //close
    "h": "216.96", //high
    "l": "206.78", //low
    "o": "210.23", //open
    "v": "73013.575", //volume
    "qv": "15726612.498168", //trade amount (in base asset, in this case is USDT)
    }],
  "f": false // Whether this is the first entry
}
```


### 

Kline/Candlestick Streams

The Kline/Candlestick Stream push updates to the current klines/candlestick every second.

**Kline/Candlestick chart intervals:**

m -> minutes; h -> hours; d -> days; w -> weeks; M -> months

**Subscription message structure:**

```
{
  "symbol": "$symbol0, $symbol1",
  "topic": "kline_"+$interval,
  "event": "sub",
  "params": {
    "binary": false
  }
}
```


**Payload:**

```
{
  "symbol": "BTCUSDT",
  "topic": "kline",
  "params": {"klineType": "15m"},
  "data": [{
    "t": 1565595900000, //kline start time
    "s": "BTCUSDT", // symbol
    "c": "11436.14", //close
    "h": "11437", //high
    "l": "11381.89", //low
    "o": "11381.89", //open
    "v": "16.3306" //volume
  }],
  "f": true// Whether this is the first entry
}
```


The Depth Streams for symbols.

Here is the book dump instructions：

*   The book dump frequency：Every 300ms, if book version changed.
    
*   The book dump depth：300 for asks and bids each.
    
*   The book version change event：
    
    *   order quantity or amount changes
        
    

```
{
  "symbol": "$symbol0, $symbol1",
  "topic": "depth",
  "event": "sub",
  "params": {
    "binary": false
    }
}
```


**Payload:**

```
{
  "symbol": "BTCUSDT",
  "topic": "depth",
  "data": [{
    "s": "BTCUSDT", //Symbol
    "t": 1565600357643, //Timestamp
    "v": "112801745_18", //Version
    "b": [ //Bids
      ["11371.49", "0.0014"], //[Price, Quantity]
      ["11371.12", "0.2"],
      ["11369.97", "0.3523"],
      ["11369.96", "0.5"],
      ["11369.95", "0.0934"],
      ["11369.94", "1.6809"],
      ["11369.6", "0.0047"],
      ["11369.17", "0.3"],
      ["11369.16", "0.2"],
      ["11369.04", "1.3203"],
    "a": [//Asks
      ["11375.41", "0.0053"], //[Price, Quantity]
      ["11375.42", "0.0043"],
      ["11375.48", "0.0052"],
      ["11375.58", "0.0541"],
      ["11375.7", "0.0386"],
      ["11375.71", "2"],
      ["11377", "2.0691"],
      ["11377.01", "0.0167"],
      ["11377.12", "1.5"],
      ["11377.61", "0.3"]
    ]
  }],
  "f": true// Whether this is the first entry
}
```


```
{
  "symbol": "$symbol0, $symbol1",
  "topic": "diffDepth",
  "event": "sub",
  "params": {
    "binary": false
  }
}
```


Order book price and quantity depth updates used to locally manage an order book pushed every second.

In the Diff. (difference) depth stream, the quantity doesn"t necessarily mean the corresponding quantity to the price anymore. If the quantity is 0, it means this previous price level is not in the orderbook anymore. If the quantity is > 0, it means the updated quantity for this price level.

Suppose now we have received the first depth data payload:

```
["0.00181860", "155.92000000"]// price, quantity
```


If the next payload is:

This means that this price level"s quantity has changed.

If the next payload is:

This means that this price level is not in orderbook anymore.

**Payload:**

```
{
  "symbol": "BTCUSDT",
  "topic": "diffDepth",
  "data": [{
    "e": 0,
    "t": 1565687625534,
    "v": "115277986_18",
    "b": [
      ["11316.78", "0.078"],
      ["11313.16", "0.0052"],
      ["11312.12", "0"],
      ["11309.75", "0.0067"],
      ["11309.58", "0"],
      ["11306.14", "0.0073"]
    ],
    "a": [
      ["11318.96", "0.0041"],
      ["11318.99", "0.0017"],
      ["11319.12", "0.0017"],
      ["11319.22", "0.4516"],
      ["11319.23", "0.0934"],
      ["11319.24", "3.0665"]
    ]
  }],
  "f": false //Whether this is the first entry
}
```


This stream is for index prices gathered for options and futures.

**Subscription message structure:**

```
{
  "symbol": "$symbol0, $symbol1",
  "topic": "index",
  "event": "sub",
}
```


**Payload:**

```
{
  "symbol": "HTUSDT",  
  "topic": "index",
  "data": [{
    "symbol": "HTUSDT",
    "index": "5.0941",
    "edp": "5.08799333",
    "formula": "(5.0941[HUOBI])/1"
  }],
  "f": true// Whether this is the first entry
}
```


**Error Codes:**

```
INVALID_REQUEST("-10000", "Invalid request!")
JSON_FORMAT_ERROR("-10001", "Invalid JSON!")
INVALID_EVENT("-10002", "Invalid event")
REQUIRED_EVENT("-10003", "Event required!")
INVALID_TOPIC("-10004", "Invalid topic!")
REQUIRED_TOPIC("-10005", "Topic required!")
PARAM_EMPTY("-10007", "Params required!")
PERIOD_EMPTY("-10008", "Period required!")
PERIOD_ERROR("-10009", "Invalid period!")
SYMBOLS_ERROR("-100010", "Invalid Symbols!")
```


Last updated 11 months ago