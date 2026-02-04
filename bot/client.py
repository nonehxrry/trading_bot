import os
from binance.client import Client
from dotenv import load_dotenv
from .logger import logger

load_dotenv()

def get_binance_client():
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')

    if not api_key or not api_secret:
        logger.error("API Keys missing in .env file!")
        raise ValueError("Missing API Keys")

    # Connect to Testnet
    client = Client(api_key, api_secret, testnet=True)
    return client
