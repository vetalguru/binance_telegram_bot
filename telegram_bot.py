from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from telegeram_api_key import TelegramAPIKey


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Help message')


async def user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{update.effective_user.first_name}')


async def echo (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)


def main():
    try:
        TELEGRAM_API_KEY = TelegramAPIKey().get_token()
        if not TELEGRAM_API_KEY:
            print("Error: Unable to get Telegram API key")
            exit(1)
    except FileNotFoundError:
        print("Error: telegeram_api_key.txt file not found")
        exit(1)

    app = ApplicationBuilder().token(TELEGRAM_API_KEY).build()
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("user", user))
    app.add_handler(CommandHandler("stop", echo))

    app.run_polling()


if __name__ == '__main__':
    main()
