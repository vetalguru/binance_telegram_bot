from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Help message')


async def user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{update.effective_user.first_name}')


async def echo (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)


def get_token() -> str:
    token_file = open('telegram_api_key.txt', 'r')
    token = token_file.readline()
    token_file.close()
    return token.rstrip()


def main():
    TELEGRAM_API_KEY = get_token()
    if not TELEGRAM_API_KEY:
        print("Error: Uable to get Telegram API key")
        exit(1)

    app = ApplicationBuilder().token(TELEGRAM_API_KEY).build()
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("user", user))
    app.add_handler(CommandHandler("stop", echo))

    app.run_polling()


if __name__ == '__main__':
    main()
