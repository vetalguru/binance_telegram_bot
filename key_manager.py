class KeyManager:
    # File containing the Telegram API key
    TELEGRAM_API_KEY_FILE = 'telegram_api_key.txt'
    
    # File containing the Binance API key
    BINANCE_API_KEY_FILE = 'binance_api_key.txt'
    
    # File containing the Binance API secret key
    BINANCE_API_SECRET_KEY_FILE = 'binance_api_secret.txt'

    def __init__(self):
        self.telegram_api_key = None
        self.binance_api_key = None
        self.binance_api_secret = None
        self._load_keys()

    def _load_keys(self):
        try:
            with open(self.TELEGRAM_API_KEY_FILE, 'r') as f:
                self.telegram_api_key = f.readline().strip()
        except FileNotFoundError as e:
            print(f"Error: {self.TELEGRAM_API_KEY_FILE} not found")
            self.telegram_api_key = None

        try:
            with open(self.BINANCE_API_KEY_FILE, 'r') as f:
                self.binance_api_key = f.readline().strip()
        except FileNotFoundError as e:
            print(f"Error: {self.BINANCE_API_KEY_FILE} not found")
            self.binance_api_key = None

        try:
            with open(self.BINANCE_API_SECRET_KEY_FILE, 'r') as f:
                self.binance_api_secret = f.readline().strip()
        except FileNotFoundError as e:
            print(f"Error: {self.BINANCE_API_SECRET_KEY_FILE} not found")
            self.binance_api_secret = None

    def get_telegram_api_key(self):
        return self.telegram_api_key

    def get_binance_api_key(self):
        return self.binance_api_key

    def get_binance_api_secret(self):
        return self.binance_api_secret
