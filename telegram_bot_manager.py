from datetime import datetime
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

from binance_market_data_rest_client import BinanceMarketDataRestClient


class TelegramBotManager:
    def __init__(self, api_key: str, binance_client: BinanceMarketDataRestClient) -> None:
        try:
            self.app = ApplicationBuilder().token(api_key).build()
            self.binance = binance_client
        except Exception as e:
            print(f"Failed to initialize the bot: {e}")
            self.app = None

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        keyboard = [
            [InlineKeyboardButton("📖 Help", callback_data='help'), InlineKeyboardButton("🕒 Server time", callback_data='server_time')],
            [InlineKeyboardButton(" ℹ️ Exchange info", callback_data='exchange_info')],
            [InlineKeyboardButton("💰 Price of BTC", callback_data='price_btc'), InlineKeyboardButton("💰 Average price of BTC", callback_data='avg_price_btc')],
            [InlineKeyboardButton("📈 Book ticker", callback_data='book_ticker_btc'), InlineKeyboardButton("📉 Ticker price", callback_data='ticker_price_btc')],
            [InlineKeyboardButton("📊 24h Ticker", callback_data='ticker_24hr_btc')],
            [InlineKeyboardButton("🛒 Recent trades", callback_data='recent_trades_btc'), InlineKeyboardButton("📜 Historical trades", callback_data='historical_trades_btc')],
            [InlineKeyboardButton("📊 Aggregate trades", callback_data='aggregate_trades_btc')],
            [InlineKeyboardButton("📈 Klines", callback_data='klines_btc')],
            [InlineKeyboardButton("🏦 Order Book", callback_data='order_book_btc')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        if update.message:
            await update.message.reply_text('📌 *Please choose an option:*', reply_markup=reply_markup)
        elif update.callback_query:
            await update.callback_query.message.edit_text('📌 *Please choose an option:*', reply_markup=reply_markup)

    async def button(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        query = update.callback_query
        await query.answer()
        command = query.data

        if command == 'help':
            await self.help(update, context)
        elif command == 'server_time':
            await self.server_time(update, context)
        elif command == 'exchange_info':
            await self.get_exchange_info(update, context)
        elif command == 'price_btc':
            await self.price_btc(update, context)
        elif command == 'avg_price_btc':
            await self.get_avg_price_btc(update, context)
        elif command == 'book_ticker_btc':
            await self.get_book_ticker_btc(update, context)
        elif command == 'ticker_price_btc':
            await self.get_ticker_price_btc(update, context)
        elif command == 'ticker_24hr_btc':
            await self.get_ticker_24hr_btc(update, context)
        elif command == 'recent_trades_btc':
            await self.get_recent_trades_btc(update, context)
        elif command == 'historical_trades_btc':
            await self.get_historical_trades_btc(update, context)
        elif command == 'aggregate_trades_btc':
            await self.get_aggregate_trades_btc(update, context)
        elif command == 'klines_btc':
            await self.get_klines_btc(update, context)
        elif command == 'order_book_btc':
            await self.get_order_book_btc(update, context)
        elif command == 'main_menu':
            await self.start(update, context)
    
    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        help_message = (
            "Available commands:\n"
            "/help - Show this help message\n"
            "/server_time - Get the current server time from Binance\n"
            "/exchange_info - Get the exchange info from Binance\n"
            "/price_btc - Get the current price of Bitcoin (BTCUSDT)\n"
            "/avg_price_btc - Get the average price for Bitcoin (BTC)\n"
            "/book_ticker_btc - Get the order book for Bitcoin (BTC)\n"
            "/ticker_price_btc - Get the ticker price for Bitcoin (BTC)\n"
            "/ticker_24hr_btc - Get the 24hr ticker for Bitcoin (BTC)\n"
            "/recent_trades_btc - Get the recent trades for Bitcoin (BTC)\n"
            "/historical_trades_btc - Get the historical trades for Bitcoin (BTC)\n"
            "/aggregate_trades_btc - Get the aggregate trades for Bitcoin (BTC)\n"
            "/klines_btc - Get the klines for Bitcoin (BTC)\n"
            "/order_book_btc - Get the order book for Bitcoin (BTC)\n"
        )

        keyboard = [[InlineKeyboardButton("🔙 Back", callback_data='main_menu')]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        if update.callback_query:
            await update.callback_query.message.edit_text(help_message, reply_markup=reply_markup)
        else:
            await update.message.reply_text(help_message, reply_markup=reply_markup)

    async def server_time(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        try:
            server_time = self.binance.get_server_time().get('serverTime') / 1000.0
            date_time = datetime.fromtimestamp(server_time).strftime('%Y-%m-%d %H:%M:%S')

            keyboard = [[InlineKeyboardButton("🔙 Back", callback_data='main_menu')]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            if update.callback_query:
                await update.callback_query.message.edit_text(f'The current server time is {date_time}', reply_markup=reply_markup)
            else:
                await update.message.reply_text(f'The current server time is {date_time}', reply_markup=reply_markup)
        except Exception as e:
            await update.message.reply_text(f'Failed to get the server time: {e}')

    async def get_exchange_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        try:
            exchange_info = self.binance.get_exchange_info()
            time_zone = exchange_info.get('timezone')
            server_time = exchange_info.get('serverTime') / 1000.0
            date_time = datetime.fromtimestamp(server_time).strftime('%Y-%m-%d %H:%M:%S')

            keyboard = [[InlineKeyboardButton("🔙 Back", callback_data='main_menu')]]
            reply_markup = InlineKeyboardMarkup(keyboard)

            if update.callback_query:
                await update.callback_query.message.edit_text(f'The exchange data to date {date_time}({time_zone}) received', reply_markup=reply_markup)
            else:
                await update.message.reply_text(f'The exchange data to date {date_time}({time_zone}) received', reply_markup=reply_markup)
        except Exception as e:
            await update.message.reply_text(f'Failed to get the exchange info: {e}')

    async def price_btc(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        symbol = 'BTCUSDT'
        try:
            price_struct = self.binance.get_coin_price(symbol)
            symbol = price_struct.get('symbol')
            price = price_struct.get('price')

            keyboard = [[InlineKeyboardButton("🔙 Back", callback_data='main_menu')]]
            reply_markup = InlineKeyboardMarkup(keyboard)

            if update.callback_query:
                await update.callback_query.message.edit_text(f'{symbol} = {price}', reply_markup=reply_markup)
            else:
                await update.message.reply_text(f'{symbol} = {price}')
        except Exception as e:
            await update.message.reply_text(f'Failed to get the price for {symbol}: {e}')

    async def get_avg_price_btc(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        symbol = 'BTCUSDT'
        try:
            avg_price_struct = self.binance.get_avg_price(symbol)
            symbol = avg_price_struct.get('symbol')
            avg_price = avg_price_struct.get('price')

            keyboard = [[InlineKeyboardButton("🔙 Back", callback_data='main_menu')]]
            reply_markup = InlineKeyboardMarkup(keyboard)

            if update.callback_query:
                await update.callback_query.message.edit_text(f'The average price for {symbol} = {avg_price}', reply_markup=reply_markup)
            else:
                await update.message.reply_text(f'The average price for {symbol} = {avg_price}', reply_markup=reply_markup)
        except Exception as e:
            await update.message.reply_text(f'Failed to get the average price for {symbol}: {e}')

    async def get_book_ticker_btc(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        symbol = 'BTCUSDT'
        try:
            book_ticker = self.binance.get_book_ticker(symbol)

            keyboard = [[InlineKeyboardButton("🔙 Back", callback_data='main_menu')]]
            reply_markup = InlineKeyboardMarkup(keyboard)

            if update.callback_query:
                await update.callback_query.message.edit_text(f'The order book for {symbol} is {book_ticker}', reply_markup=reply_markup)
            else:
                await update.message.reply_text(f'The order book for {symbol} is {book_ticker}', reply_markup=reply_markup)
        except Exception as e:
            await update.message.reply_text(f'Failed to get the order book for {symbol}: {e}')

    async def get_ticker_price_btc(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        symbol = 'BTCUSDT'
        try:
            ticker_price = self.binance.get_ticker_price(symbol)

            keyboard = [[InlineKeyboardButton("🔙 Back", callback_data='main_menu')]]
            reply_markup = InlineKeyboardMarkup(keyboard)

            if update.callback_query:
                await update.callback_query.message.edit_text(f'The ticker price for {symbol} is {ticker_price}', reply_markup=reply_markup)
            else:
                await update.message.reply_text(f'The ticker price for {symbol} is {ticker_price}', reply_markup=reply_markup)
        except Exception as e:
            await update.message.reply_text(f'Failed to get the ticker price for {symbol}: {e}')

    async def get_ticker_24hr_btc(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        symbol = 'BTCUSDT'
        try:
            ticker_24hr = self.binance.get_ticker_24hr(symbol)

            keyboard = [[InlineKeyboardButton("🔙 Back", callback_data='main_menu')]]
            reply_markup = InlineKeyboardMarkup(keyboard)

            if update.callback_query:
                await update.callback_query.message.edit_text(f'The 24hr ticker for {symbol} is {ticker_24hr}', reply_markup=reply_markup)
            else:
                await update.message.reply_text(f'The 24hr ticker for {symbol} is {ticker_24hr}', reply_markup=reply_markup)
        except Exception as e:
            await update.message.reply_text(f'Failed to get the 24hr ticker for {symbol}: {e}')

    async def get_recent_trades_btc(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        symbol = 'BTCUSDT'
        try:
            recent_trades = self.binance.get_recent_trades(symbol)

            keyboard = [[InlineKeyboardButton("🔙 Back", callback_data='main_menu')]]
            reply_markup = InlineKeyboardMarkup(keyboard)

            if update.callback_query:
                await update.callback_query.message.edit_text(f'The recent trades counter of items for {symbol} are {len(recent_trades)}', reply_markup=reply_markup)
            else:
                await update.message.reply_text(f'The downloaded recent trades counter of items for {symbol} are {len(recent_trades)}', reply_markup=reply_markup)
        except Exception as e:
            await update.message.reply_text(f'Failed to get the recent trades for {symbol}: {e}')

    async def get_historical_trades_btc(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        symbol = 'BTCUSDT'
        try:
            historical_trades = self.binance.get_historical_trades(symbol)

            keyboard = [[InlineKeyboardButton("🔙 Back", callback_data='main_menu')]]
            reply_markup = InlineKeyboardMarkup(keyboard)

            if update.callback_query:
                await update.callback_query.message.edit_text(f'The historical trades counter of items for {symbol} are {len(historical_trades)}', reply_markup=reply_markup)
            else:
                await update.message.reply_text(f'The downloaded historical trades counter of items for {symbol} are {len(historical_trades)}', reply_markup=reply_markup)
        except Exception as e:
            await update.message.reply_text(f'Failed to get the historical trades for {symbol}: {e}')

    async def get_aggregate_trades_btc(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        symbol = 'BTCUSDT'
        try:
            aggregate_trades = self.binance.get_aggregate_trades(symbol)

            keyboard = [[InlineKeyboardButton("🔙 Back", callback_data='main_menu')]]
            reply_markup = InlineKeyboardMarkup(keyboard)

            if update.callback_query:
                await update.callback_query.message.edit_text(f'The aggregate trades counter of items for {symbol} are {len(aggregate_trades)}', reply_markup=reply_markup)
            else:
                await update.message.reply_text(f'The downloaded aggregate trades counter of items for {symbol} are {len(aggregate_trades)}', reply_markup=reply_markup)
        except Exception as e:
            await update.message.reply_text(f'Failed to get the aggregate trades for {symbol}: {e}')

    async def get_klines_btc(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        symbol = 'BTCUSDT'
        interval = '1m'
        try:
            klines = self.binance.get_klines(symbol, interval)

            keyboard = [[InlineKeyboardButton("🔙 Back", callback_data='main_menu')]]
            reply_markup = InlineKeyboardMarkup(keyboard)

            if update.callback_query:
                await update.callback_query.message.edit_text(f'The klines counter of items for {symbol} are {len(klines)}', reply_markup=reply_markup)
            else:
                await update.message.reply_text(f'The downloaded klines counter of items for {symbol} are {len(klines)}', reply_markup=reply_markup)
        except Exception as e:
            await update.message.reply_text(f'Failed to get the klines for {symbol}: {e}')

    async def get_order_book_btc(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        symbol = 'BTCUSDT'
        try:
            order_book = self.binance.get_order_book(symbol)
            bids_price = order_book.get('bids')[0][0]

            keyboard = [[InlineKeyboardButton("🔙 Back", callback_data='main_menu')]]
            reply_markup = InlineKeyboardMarkup(keyboard)

            if update.callback_query:
                await update.callback_query.message.edit_text(f'The order book for {symbol} is {bids_price}', reply_markup=reply_markup)
            else:
                await update.message.reply_text(f'The order book for {symbol} is {bids_price}', reply_markup=reply_markup)
        except Exception as e:
            await update.message.reply_text(f'Failed to get the order book for {symbol}: {e}')

    def run(self) -> None:
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(CallbackQueryHandler(self.button))

        self.app.add_handler(CommandHandler("help", self.help))
        self.app.add_handler(CommandHandler("server_time", self.server_time))
        self.app.add_handler(CommandHandler("exchange_info", self.get_exchange_info))
        self.app.add_handler(CommandHandler("price_btc", self.price_btc))
        self.app.add_handler(CommandHandler("avg_price_btc", self.get_avg_price_btc))
        self.app.add_handler(CommandHandler("book_ticker_btc", self.get_book_ticker_btc))
        self.app.add_handler(CommandHandler("ticker_price_btc", self.get_ticker_price_btc))
        self.app.add_handler(CommandHandler("ticker_24hr_btc", self.get_ticker_24hr_btc))
        self.app.add_handler(CommandHandler("recent_trades_btc", self.get_recent_trades_btc))
        self.app.add_handler(CommandHandler("historical_trades_btc", self.get_historical_trades_btc))
        self.app.add_handler(CommandHandler("aggregate_trades_btc", self.get_aggregate_trades_btc))
        self.app.add_handler(CommandHandler("klines_btc", self.get_klines_btc))
        self.app.add_handler(CommandHandler("order_book_btc", self.get_order_book_btc))

        self.app.run_polling()
