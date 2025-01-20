import os
"""
This module provides functionality to retrieve the Telegram API key from a file.
Classes:
    TelegramAPIKey: A class to handle the retrieval of the Telegram API key.
Constants:
    TELEGRAM_API_KEY_FILE (str): The path to the file containing the Telegram API key.
Exceptions:
    FileNotFoundError: Raised when the API key file does not exist.
Methods:
    TelegramAPIKey.get_token(self) -> str:
        Reads the Telegram API key from the file and returns it as a string.
        Raises FileNotFoundError if the API key file is not found.
"""

TELEGRAM_API_KEY_FILE = os.path.join(os.path.dirname(__file__), 'telegram_api_key.txt')

class TelegramAPIKey:
    def get_token(self) -> str:
        if not os.path.exists(TELEGRAM_API_KEY_FILE):
            raise FileNotFoundError(f"API key file not found: {TELEGRAM_API_KEY_FILE}")
        
        with open(TELEGRAM_API_KEY_FILE, 'r') as token_file:
            token = token_file.readline().strip()
        return token
