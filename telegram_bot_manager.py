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
            "/ticker_24hr_btc - Get the 24hr ticker for Bitcoin (BTC)\n"
            "/ticker_24hr_sol - Get the 24hr ticker for Solana (SOL)\n"
            "/avg_price_btc - Get the average price for Bitcoin (BTC)\n"
            "/avg_price_sol - Get the average price for Solana (SOL)\n"
            "/recent_trades_btc - Get the recent trades for Bitcoin (BTC)\n"
            "/recent_trades_sol - Get the recent trades for Solana (SOL)\n"
            "/historical_trades_btc - Get the historical trades for Bitcoin (BTC)\n"
            "/historical_trades_sol - Get the historical trades for Solana (SOL)\n"
            "/aggregate_trades_btc - Get the aggregate trades for Bitcoin (BTC)\n"
            "/aggregate_trades_sol - Get the aggregate trades for Solana (SOL)\n"
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

    async def get_ticker_24hr_btc(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        symbol = 'BTCUSDT'
        try:
            ticker_24hr = self.binance.get_ticker_24hr(symbol)
            await update.message.reply_text(f'The 24hr ticker for {symbol} is {ticker_24hr}')
        except Exception as e:
            await update.message.reply_text(f'Failed to get the 24hr ticker for {symbol}: {e}')

    async def get_ticker_24hr_sol(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        symbol = 'SOLUSDT'
        try:
            ticker_24hr = self.binance.get_ticker_24hr(symbol)
            await update.message.reply_text(f'The 24hr ticker for {symbol} is {ticker_24hr}')
        except Exception as e:
            await update.message.reply_text(f'Failed to get the 24hr ticker for {symbol}: {e}')

    async def get_avg_price_btc(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        symbol = 'BTCUSDT'
        try:
            avg_price = self.binance.get_avg_price(symbol)
            await update.message.reply_text(f'The average price for {symbol} is {avg_price}')
        except Exception as e:
            await update.message.reply_text(f'Failed to get the average price for {symbol}: {e}')

    async def get_avg_price_sol(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        symbol = 'SOLUSDT'
        try:
            avg_price = self.binance.get_avg_price(symbol)
            await update.message.reply_text(f'The average price for {symbol} is {avg_price}')
        except Exception as e:
            await update.message.reply_text(f'Failed to get the average price for {symbol}: {e}')

    async def get_recent_trades_btc(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        symbol = 'BTCUSDT'
        try:
            recent_trades = self.binance.get_recent_trades(symbol)
            await update.message.reply_text(f'The downloaded recent trades counter of items for {symbol} are {len(recent_trades)}')
        except Exception as e:
            await update.message.reply_text(f'Failed to get the recent trades for {symbol}: {e}')

    async def get_recent_trades_sol(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        symbol = 'SOLUSDT'
        try:
            recent_trades = self.binance.get_recent_trades(symbol)
            await update.message.reply_text(f'The downloaded recent trades counter of items for {symbol} are {len(recent_trades)}')
        except Exception as e:
            await update.message.reply_text(f'Failed to get the recent trades for {symbol}: {e}')

    async def get_historical_trades_btc(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        symbol = 'BTCUSDT'
        try:
            historical_trades = self.binance.get_historical_trades(symbol)
            await update.message.reply_text(f'The downloaded historical trades counter of items for {symbol} are {len(historical_trades)}')
        except Exception as e:
            await update.message.reply_text(f'Failed to get the historical trades for {symbol}: {e}')

    async def get_historical_trades_sol(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        symbol = 'SOLUSDT'
        try:
            historical_trades = self.binance.get_historical_trades(symbol)
            await update.message.reply_text(f'The downloaded historical trades counter of items for {symbol} are {len(historical_trades)}')
        except Exception as e:
            await update.message.reply_text(f'Failed to get the historical trades for {symbol}: {e}')

    async def get_aggregate_trades_btc(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        symbol = 'BTCUSDT'
        try:
            aggregate_trades = self.binance.get_aggregate_trades(symbol)
            await update.message.reply_text(f'The downloaded aggregate trades counter of items for {symbol} are {len(aggregate_trades)}')
        except Exception as e:
            await update.message.reply_text(f'Failed to get the aggregate trades for {symbol}: {e}')
    
    async def get_aggregate_trades_sol(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        symbol = 'SOLUSDT'
        try:
            aggregate_trades = self.binance.get_aggregate_trades(symbol)
            await update.message.reply_text(f'The downloaded aggregate trades counter of items for {symbol} are {len(aggregate_trades)}')
        except Exception as e:
            await update.message.reply_text(f'Failed to get the aggregate trades for {symbol}: {e}')

    def run(self) -> None:
        self.app.add_handler(CommandHandler("help", self.help))
        self.app.add_handler(CommandHandler("price_btc", self.price_btc))
        self.app.add_handler(CommandHandler("price_sol", self.price_sol))
        self.app.add_handler(CommandHandler("server_time", self.server_time))
        self.app.add_handler(CommandHandler("book_ticker_btc", self.get_book_ticker_btc))
        self.app.add_handler(CommandHandler("book_ticker_sol", self.get_book_ticker_sol))
        self.app.add_handler(CommandHandler("ticker_price_btc", self.get_ticker_price_btc))
        self.app.add_handler(CommandHandler("ticker_price_sol", self.get_ticker_price_sol))
        self.app.add_handler(CommandHandler("ticker_24hr_btc", self.get_ticker_24hr_btc))
        self.app.add_handler(CommandHandler("ticker_24hr_sol", self.get_ticker_24hr_sol))
        self.app.add_handler(CommandHandler("avg_price_btc", self.get_avg_price_btc))
        self.app.add_handler(CommandHandler("avg_price_sol", self.get_avg_price_sol))
        self.app.add_handler(CommandHandler("recent_trades_btc", self.get_recent_trades_btc))
        self.app.add_handler(CommandHandler("recent_trades_sol", self.get_recent_trades_sol))
        self.app.add_handler(CommandHandler("historical_trades_btc", self.get_historical_trades_btc))
        self.app.add_handler(CommandHandler("historical_trades_sol", self.get_historical_trades_sol))
        self.app.add_handler(CommandHandler("aggregate_trades_btc", self.get_aggregate_trades_btc))
        self.app.add_handler(CommandHandler("aggregate_trades_sol", self.get_aggregate_trades_sol))

        self.app.run_polling()
