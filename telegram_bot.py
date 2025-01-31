from telegram_bot_manager import TelegramBotManager

from binance_market_data_rest_client import BinanceMarketDataRestClient
from key_manager import KeyManager


def main():
    key_manager = KeyManager()
    TELEGRAM_API_KEY = key_manager.get_telegram_api_key()

    if not TELEGRAM_API_KEY:
        print("Error: Unable to get Telegram API keys")
        exit(1)

    try:
        binance_marked_data_rest_client = BinanceMarketDataRestClient()
    except ValueError as e:
        # Raised when there is an issue with the provided API keys
        print(f"Failed to initialize the Binance client due to invalid API keys: {e}")
        exit(1)
    except ConnectionError as e:
        # Raised when there is a network issue
        print(f"Failed to initialize the Binance client due to a network issue: {e}")
        exit(1)
    except Exception as e:
        # Catch any other exceptions that may occur
        print(f"Failed to initialize the Binance client: {e}")
        exit(1)

    bot_manager = TelegramBotManager(TELEGRAM_API_KEY, binance_marked_data_rest_client)
    if bot_manager.app is None:
        print("Error: Failed to initialize the Telegram bot manager")
        exit(1)
    
    bot_manager.run()


if __name__ == '__main__':
    main()
