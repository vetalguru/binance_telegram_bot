from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


class TelegramBotManager:
    def __init__(self, api_key: str) -> None:
        try:
            self.app = ApplicationBuilder().token(api_key).build()
        except Exception as e:
            print(f"Failed to initialize the bot: {e}")
            self.app = None
    
    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(f'Help message')

    async def user(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(f'User name: {update.effective_user.first_name}')

    async def echo (self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(update.message.text)

    def run(self) -> None:
        self.app.add_handler(CommandHandler("help", self.help))
        self.app.add_handler(CommandHandler("user", self.user))
        self.app.add_handler(CommandHandler("echo", self.echo))

        self.app.run_polling()
