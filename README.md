# Binance Telegram Bot

This project is a Telegram bot designed for interacting with Binance, providing functionalities such as tracking cryptocurrency prices, managing your portfolio, and performing trades.

## Features

- **Real-time Price Updates:** Get the latest price information for your favorite cryptocurrencies.
- **Portfolio Management:** View and manage your cryptocurrency portfolio directly within Telegram.
- **Trading Support:** Execute buy and sell orders through Binance's API.
- **Alerts:** Set up price alerts and get notified instantly.
- **Secure Authentication:** Use API keys securely to ensure your Binance account is protected.

## Requirements

- Python 3.8 or higher
- A Binance account with API access enabled
- A Telegram bot token (you can create one via [BotFather](https://core.telegram.org/bots#botfather))

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/binance-telegram-bot.git
   cd binance-telegram-bot
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   Create a `.env` file in the root directory with the following:
   ```env
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   BINANCE_API_KEY=your_binance_api_key
   BINANCE_API_SECRET=your_binance_api_secret
   ```

4. Run the bot:
   ```bash
   python bot.py
   ```

## Usage

1. Start the bot in Telegram by searching for your bot and clicking "Start."
2. Use the provided commands to interact with Binance, such as:
   - `/price BTCUSDT` - Get the current price of Bitcoin in USDT.
   - `/portfolio` - View your Binance portfolio.
   - `/buy BTCUSDT 0.01` - Buy 0.01 BTC with USDT.
   - `/sell BTCUSDT 0.01` - Sell 0.01 BTC for USDT.

## Commands

| Command         | Description                                     |
|-----------------|-------------------------------------------------|
| `/price [pair]` | Get the price of a specific trading pair.       |
| `/portfolio`    | View your Binance portfolio.                   |
| `/buy`          | Buy a specified amount of cryptocurrency.      |
| `/sell`         | Sell a specified amount of cryptocurrency.     |
| `/alert`        | Set a price alert for a trading pair.          |

## Security Notes

- Do not share your API keys with anyone.
- Use IP whitelisting in Binance to limit API access to trusted sources.
- Keep your `.env` file secure and do not include it in version control.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

This bot is provided "as is" without warranty of any kind. Use it at your own risk. Trading cryptocurrencies involves risk, and you should do your own research before making any trades.

---

Feel free to reach out for support or feature requests by opening an issue or contacting me on Telegram.
