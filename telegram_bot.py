from telegeram_api_key import TelegramAPIKey
from telegram_bot_manager import TelegramBotManager


def main():
    try:
        TELEGRAM_API_KEY = TelegramAPIKey().get_token()
        if not TELEGRAM_API_KEY:
            print("Error: Unable to get Telegram API key")
            exit(1)
    except FileNotFoundError:
        print("Error: telegeram_api_key.txt file not found")
        exit(1)

    bot_manager = TelegramBotManager(TELEGRAM_API_KEY)
    bot_manager.run()


if __name__ == '__main__':
    main()
