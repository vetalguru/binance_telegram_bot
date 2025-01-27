from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from binance_client import BinanceClient


class TelegramBotManager:
    def __init__(self, api_key: str, binance: BinanceClient) -> None:
        try:
            self.app = ApplicationBuilder().token(api_key).build()
            self.binance = binance
        except Exception as e:
            print(f"Failed to initialize the bot: {e}")
            self.app = None
    
    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        help_message = (
            "Available commands:\n"
            "/help - Show this help message\n"
            "/price_btc - Get the current price of Bitcoin (BTC)\n"
            "/price_sol - Get the current price of Solana (SOL)\n"
            "/server_time - Get the current server time from Binance\n"
        )
        await update.message.reply_text(help_message)

    async def price_btc(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        symbol = 'BTCUSDT'
        try:
            price = self.binance.get_coin_price(symbol)
            await update.message.reply_text(f'The current price of {symbol} is {price}')
        except Exception as e:
            await update.message.reply_text(f'Failed to get the price for {symbol}: {e}')
        
    async def price_sol(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        symbol = 'SOLUSDT'
        try:
            price = self.binance.get_coin_price(symbol)
            await update.message.reply_text(f'The current price of {symbol} is {price}')
        except Exception as e:
            await update.message.reply_text(f'Failed to get the price for {symbol}: {e}')

    async def server_time(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        try:
            server_time = self.binance.get_server_time()
            await update.message.reply_text(f'The server time is {server_time}')
        except Exception as e:
            await update.message.reply_text(f'Failed to get the server time: {e}')

    def run(self) -> None:
        self.app.add_handler(CommandHandler("help", self.help))
        self.app.add_handler(CommandHandler("price_btc", self.price_btc))
        self.app.add_handler(CommandHandler("price_sol", self.price_sol))
        self.app.add_handler(CommandHandler("server_time", self.server_time))

        self.app.run_polling()
