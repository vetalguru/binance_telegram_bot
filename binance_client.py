import requests

class BinanceClient:
    """
    A client for interacting with the Binance API.
    Attributes:
        BASE_URL (str): The base URL for the Binance API.
        api_key (str): The API key for authenticating with the Binance API.
        api_secret (str): The API secret for authenticating with the Binance API.
    """

    BASE_URL = 'https://api.binance.com'

    def __init__(self, api_key, api_secret) -> None:
        """
        Initializes the BinanceClient with the provided API key and secret.

        Args:
            api_key (str): The API key for accessing the Binance API.
            api_secret (str): The API secret for accessing the Binance API.
        """
        self.api_key = api_key
        self.api_secret = api_secret

    def _get_headers(self) -> dict:
        """
        Generate the headers required for making authenticated requests to the Binance API.

        Returns:
            dict: A dictionary containing the API key header.
        """
        return {'X-MBX-APIKEY': self.api_key}

    def _get(self, endpoint, params=None) -> dict:
        """
        Sends a GET request to the specified endpoint with optional parameters.

        Args:
            endpoint (str): The API endpoint to send the GET request to.
            params (dict, optional): A dictionary of query parameters to include in the request.

        Returns:
            dict: The JSON response from the server if the request is successful.
            None: If an error occurs during the request.

        Raises:
            requests.exceptions.RequestException: If an error occurs while making the request.
        """
        url = f"{self.BASE_URL}{endpoint}"
        try:
            response = requests.get(url, headers=self._get_headers(), params=params)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def _post(self, endpoint, data=None) -> dict:
        """
        Sends a POST request to the specified endpoint with the provided data.

        Args:
            endpoint (str): The API endpoint to send the request to.
            data (dict, optional): The data to include in the POST request. Defaults to None.

        Returns:
            dict: The JSON response from the server if the request is successful.
            None: If an error occurs during the request.
        """
        url = f"{self.BASE_URL}{endpoint}"
        try:
            response = requests.post(url, headers=self._get_headers(), data=data)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def get_coin_price(self, symbol=None) -> list:
        """
        Get spot index price for option underlying

        Request weight: 1

        Args:
            symbol (str, option): Spot pair（Option contract underlying asset, e.g BTCUSDT)

        Returns:
            list: A list containing the current price of the specified cryptocurrency.

        Return example:
            [
                {
                    "symbol":"ETHBTC",
                    "price":"0.03031000"
                },
                {
                    "symbol":"LTCBTC"
                    ,"price":"0.00109400"
                },
                ...
            ]
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
        return self._get('/api/v3/ticker/price', params = params)

    def get_server_time(self) -> dict:
        """
        Test connectivity to the Rest API and get the current server time.

        Request weight: 1

        Returns:
            dict: A dictionary containing the server time.

        Return example:
            {
                "serverTime": 1499827319559
            }
        """
        return self._get('/api/v3/time')
    
    def get_book_ticker(self, symbol=None) -> list:
        """
        Get the best price/quantity on the order book for a specified symbol.

        Args:
            symbol (str): The symbol to get the book ticker for (e.g., 'BTCUSDT').

        Returns:
            list: A list containing the best bid and ask prices and quantities.

        Return example:
            [
                {
                    "symbol": "BTCUSDT",
                    "bidPrice": "4.00000000",
                    "bidQty": "431.00000000",
                    "askPrice": "4.00000200",
                    "askQty": "12.00000000"
                }
            ]
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
        return self._get('/api/v3/ticker/bookTicker', params=params)
    
    def get_ticker_price(self, symbol=None) -> list:
        """
        Get the latest price for a given symbol.

        Args:
            symbol (str): The symbol for which to get the latest price (e.g., 'BTCUSDT').

        Returns:
            list: A list containing the latest price information for the given symbol.
        
        Return example:
            [
                {
                    "symbol": "BTCUSDT",
                    "price": "0.00391480"
                }
            ]
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
        return self._get('/api/v3/ticker/price', params=params)

    def get_ticker_24hr(self, symbol=None) -> list:
        """
        Get 24 hour rolling window price change statistics.

        Request weight: 5

        Args:
            symbol (str, optional): Option trading pair, e.g BTC-200730-9000-C

        Returns:
            list: A list containing the 24-hour ticker price change statistics.

        Return example:
            [
                {
                    "symbol": "BTC-200730-9000-C",
                    "priceChange": "-16.2038",        //24-hour price change
                    "priceChangePercent": "-0.0162",  //24-hour percent price change
                    "lastPrice": "1000",              //Last trade price
                    "lastQty": "1000",                //Last trade amount
                    "open": "1016.2038",              //24-hour open price
                    "high": "1016.2038",              //24-hour high
                    "low": "0",                       //24-hour low
                    "volume": "5",                    //Trading volume(contracts)
                    "amount": "1",                    //Trade amount(in quote asset)
                    "bidPrice":"999.34",              //The best buy price
                    "askPrice":"1000.23",             //The best sell price
                    "openTime": 1592317127349,        //Time the first trade occurred within the last 24 hours
                    "closeTime": 1592380593516,       //Time the last trade occurred within the last 24 hours     
                    "firstTradeId": 1,                //First trade ID
                    "tradeCount": 5,                  //Number of trades
                    "strikePrice": "9000",            //Strike price
                    "exercisePrice": "3000.3356"      //return estimated settlement price one hour before exercise, return index price at other times
                }
            ]
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
        return self._get('/api/v3/ticker/24hr', params=params)

    def get_avg_price(self, symbol) -> dict:
        """
        Get the current average price for a symbol.

        Args:
            symbol (str): The symbol to get the average price for.

        Returns:
            dict: A dictionary containing the average price information.

        Return example:
            {
                "mins":5,
                "price":"102778.65236263",
                "closeTime":1738175921705
            }
        """
        params = {"symbol": symbol}
        return self._get('/api/v3/avgPrice', params=params)

    def get_recent_trades(self, symbol, limit=500) -> list:
        """
        Get the most recent trades for a given symbol from the Binance API.

        Args:
            symbol (str): The trading pair symbol (e.g., 'BTCUSDT').
            limit (int, optional): The number of recent trades to retrieve. Defaults to 500.

        Returns:
            list: A list containing the recent trades data.

        Return example:
            [
                {
                    "id":4485307234,
                    "price":"102672.56000000",
                    "qty":"0.00532000",
                    "quoteQty":"546.21801920",
                    "time":1738176140230,
                    "isBuyerMaker":true,
                    "isBestMatch":true
                },
                ...
            ]
        """
        params = {"symbol": symbol, "limit": limit}
        return self._get('/api/v3/trades', params=params)
    
    def get_historical_trades(self, symbol, limit=500) -> list:
        """
        Get historical trades for a given symbol.

        Args:
            symbol (str): The trading symbol (e.g., 'BTCUSDT').
            limit (int, optional): The number of historical trades to retrieve. Default is 500.

        Returns:
            list: A list containing the historical trades data.
        
        Return example:
            [
                {
                    "id":4485312120,
                    "price":"102766.99000000",
                    "qty":"0.00005000",
                    "quoteQty":"5.13834950",
                    "time":1738176265769,
                    "isBuyerMaker":true,
                    "isBestMatch":true
                },
                ...
            ]
        """
        params = {"symbol": symbol, "limit": limit}
        return self._get('/api/v3/historicalTrades', params=params)

    def get_aggregate_trades(self, symbol, fromId=None, startTime=None, endTime=None, limit=500) -> list:
        """
        Get compressed, aggregate market trades. Market trades that fill in 100ms with the same price
        and the same taking side will have the quantity aggregated.

        Request weight: 20

        Args:
            symbol (str): symbol name	
            fromId (long, optional): ID to get aggregate trades from INCLUSIVE.
            startTime (long, optional): Timestamp in ms to get aggregate trades from INCLUSIVE.
            endTime	(long, optional): Timestamp in ms to get aggregate trades until INCLUSIVE.
            limit (int, optional) Default 500; max 1000.

            Support querying futures trade histories that are not older than one year

            If both startTime and endTime are sent, time between startTime and endTime must be less than 1 hour.

            If fromId, startTime, and endTime are not sent, the most recent aggregate trades will be returned.

            Only market trades will be aggregated and returned, which means the insurance fund trades and ADL trades won't be aggregated.

            Sending both startTime/endTime and fromId might cause response timeout, please send either fromId or startTime/endTime

        Returns:
            list: A list containing the aggregate trades data.

        Return example:
            [
                {
                    "a": 26129,         // Aggregate tradeId
                    "p": "0.01633102",  // Price
                    "q": "4.70443515",  // Quantity
                    "f": 27781,         // First tradeId
                    "l": 27781,         // Last tradeId
                    "T": 1498793709153, // Timestamp
                    "m": true,          // Was the buyer the maker?
                    "M": true           // Was the trade the best price match?
                }
            ]
        """
        params = {"symbol": symbol, "limit": limit}
        if fromId:
            params["fromId"] = fromId
        if startTime:
            params["startTime"] = startTime
        if endTime:
            params["endTime"] = endTime
        return self._get('/api/v3/aggTrades', params=params)

    def get_klines(self, symbol, interval, startTime=None, endTime=None, limit=500) -> list:
        """
        Get kline/candlestick bars for an option symbol. Klines are uniquely identified by their open time

        Request weight based on parameter limit
        Limit       weight
        [1,100)	    1
        [100, 500)	2
        [500, 1000]	5
        1000        10

        Args:
            symbol (str): Option trading pair, e.g BTC-200730-9000-C
            interval (str): Time interval (e.g., '1m', '5m', '1h')
            startTime (long, optional): Start Time 1592317127349
            endTime (long, optional): End Time
            limit (int, optional): Number of records. Default: 500. Max: 1500

            If startTime and endTime are not sent, the most recent klines are returned.

        Returns:
            list: A list containing the candlestick data.

        Return example:
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
                    308,                // Number of trades
                    "1756.87402397",    // Taker buy base asset volume
                    "28.46694368",      // Taker buy quote asset volume
                    "17928899.62484339" // Ignore
                ]
            ]
        """
        params = {"symbol": symbol, "interval": interval, "limit": limit}
        if startTime:
            params["startTime"] = startTime
        if endTime:
            params["endTime"] = endTime
        return self._get('/api/v3/klines', params=params)

    def get_exchange_info(self) -> dict:
        """
        Get current exchange trading rules and symbol information

        Request weight: 1

        Returns:
            dict: A dictionary containing the exchange information.

        Return example:
            {
                "timezone": "UTC",                    // Time zone used by the server
                "serverTime": 1592387337630,          // Current system time
                "optionContracts": [                  // Option contract underlying asset info
                    {
                    "baseAsset": "BTC",               // Base currency
                    "quoteAsset": "USDT",             // Quotation asset
                    "underlying": "BTCUSDT",          // Name of the underlying asset of the option contract
                    "settleAsset": "USDT"             // Settlement currency
                    }
                ],
                "optionAssets": [                     // Option asset info
                    {
                    "name": "USDT"                    // Asset name
                    }
                ],
                "optionSymbols": [                    // Option trading pair info
                    {
                        "expiryDate": 1660521600000,    // expiry time
                        "filters": [
                            {
                                "filterType": "PRICE_FILTER",
                                "minPrice": "0.02",
                                "maxPrice": "80000.01",
                                "tickSize": "0.01"
                            },
                            {
                                "filterType": "LOT_SIZE",
                                "minQty": "0.01",
                                "maxQty": "100",
                                "stepSize": "0.01"
                            }
                        ],
                        "symbol": "BTC-220815-50000-C",   // Trading pair name
                        "side": "CALL",                   // Direction: CALL long, PUT short
                        "strikePrice": "50000",           // Strike price
                        "underlying": "BTCUSDT",          // Underlying asset of the contract
                        "unit": 1,                        // Contract unit, the quantity of the underlying asset represented by a single contract.
                        "makerFeeRate": "0.0002",         // maker commission rate
                        "takerFeeRate": "0.0002",         // taker commission rate
                        "minQty": "0.01",                 // Minimum order quantity
                        "maxQty": "100",                  // Maximum order quantity
                        "initialMargin": "0.15",          // Initial Magin Ratio
                        "maintenanceMargin": "0.075",     // Maintenance Margin Ratio
                        "minInitialMargin": "0.1",        // Min Initial Margin Ratio
                        "minMaintenanceMargin": "0.05",   // Min Maintenance Margin Ratio
                        "priceScale": 2,                  // price precision
                        "quantityScale": 2,               // quantity precision
                        "quoteAsset": "USDT"              // Quotation asset
                    }
                ],
                "rateLimits": [
                    {
                        "rateLimitType": "REQUEST_WEIGHT",
                        "interval": "MINUTE",
                        "intervalNum": 1,
                        "limit": 2400
                    },
                    {
                        "rateLimitType": "ORDERS",
                        "interval": "MINUTE",
                        "intervalNum": 1,
                        "limit": 1200
                    },
                    {
                        "rateLimitType": "ORDERS",
                        "interval": "SECOND",
                        "intervalNum": 10,
                        "limit": 300
                    }
                ]
            }
        """
        return self._get('/api/v3/exchangeInfo')

    def get_order_book(self, symbol, limit=100) -> dict:
        """
        Check orderbook depth on specific symbol

        Request weight:
            limit	        weight
            5, 10, 20, 50	2
            100	            5
            500	            10
            1000	        20

        Args:
            symbol (str): Option trading pair, e.g BTC-200730-9000-C
            limit (int, optional): Default:100 Max:1000.Optional value:[10, 20, 50, 100, 500, 1000]

        Returns:
            dict: A dictionary containing the order book data.

        Return example:
            {
                "T": 1589436922972,   // transaction time
                "u": 37461            // update id
                "bids": [             // Buy order
                    [
                    "1000",            // Price
                    "0.9"              // Quantity
                    ]
                ],
                "asks": [              // Sell order
                    [
                    "1100",            // Price
                    "0.1"              // Quantity
                    ]
                ]
            }
        """
        params = {"symbol": symbol, "limit": limit}
        return self._get('/api/v3/depth', params=params)
