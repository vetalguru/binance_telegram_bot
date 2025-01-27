from datetime import datetime
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
            "/book_ticker_btc - Get the order book for Bitcoin (BTC)\n"
            "/book_ticker_sol - Get the order book for Solana (SOL)\n"
            "/ticker_price_btc - Get the ticker price for Bitcoin (BTC)\n"
            "/ticker_price_sol - Get the ticker price for Solana (SOL)\n"
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
            server_time = self.binance.get_server_time().get('serverTime') / 1000.0
            date_time = datetime.fromtimestamp(server_time).strftime('%Y-%m-%d %H:%M:%S')
            await update.message.reply_text(f'The server time is {date_time}')
        except Exception as e:
            await update.message.reply_text(f'Failed to get the server time: {e}')

    async def get_book_ticker_btc(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        symbol = 'BTCUSDT'
        try:
            book_ticker = self.binance.get_book_ticker(symbol)
            await update.message.reply_text(f'The order book for {symbol} is {book_ticker}')
        except Exception as e:
            await update.message.reply_text(f'Failed to get the order book for {symbol}: {e}')

    async def get_book_ticker_sol(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        symbol = 'SOLUSDT'
        try:
            book_ticker = self.binance.get_book_ticker(symbol)
            await update.message.reply_text(f'The order book for {symbol} is {book_ticker}')
        except Exception as e:
            await update.message.reply_text(f'Failed to get the order book for {symbol}: {e}')

    async def get_ticker_price_btc(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        symbol = 'BTCUSDT'
        try:
            ticker_price = self.binance.get_ticker_price(symbol)
            await update.message.reply_text(f'The ticker price for {symbol} is {ticker_price}')
        except Exception as e:
            await update.message.reply_text(f'Failed to get the ticker price for {symbol}: {e}')

    async def get_ticker_price_sol(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        symbol = 'SOLUSDT'
        try:
            ticker_price = self.binance.get_ticker_price(symbol)
            await update.message.reply_text(f'The ticker price for {symbol} is {ticker_price}')
        except Exception as e:
            await update.message.reply_text(f'Failed to get the ticker price for {symbol}: {e}')

    def run(self) -> None:
        self.app.add_handler(CommandHandler("help", self.help))
        self.app.add_handler(CommandHandler("price_btc", self.price_btc))
        self.app.add_handler(CommandHandler("price_sol", self.price_sol))
        self.app.add_handler(CommandHandler("server_time", self.server_time))
        self.app.add_handler(CommandHandler("book_ticker_btc", self.get_book_ticker_btc))
        self.app.add_handler(CommandHandler("book_ticker_sol", self.get_book_ticker_sol))
        self.app.add_handler(CommandHandler("ticker_price_btc", self.get_ticker_price_btc))
        self.app.add_handler(CommandHandler("ticker_price_sol", self.get_ticker_price_sol))

        self.app.run_polling()
