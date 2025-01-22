import requests

class BinanceClient:
    BASE_URL = 'https://api.binance.com'

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def _get_headers(self):
        return {'X-MBX-APIKEY': self.api_key}

    def _get(self, endpoint, params=None):
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.get(url, headers=self._get_headers(), params=params)
        return response.json()

    def _post(self, endpoint, data=None):
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.post(url, headers=self._get_headers(), data=data)
        return response.json()

    def get_coin_price(self, symbol):
        params = {"symbol": symbol}
        return self._get('/api/v3/ticker/price', params = params)
