import argparse
from bot.client import get_binance_client
from bot.orders import place_order
from bot.logger import logger

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Bot")
    parser.add_argument("--symbol", required=True, help="e.g., BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--qty", required=True, type=float)
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    try:
        client = get_binance_client()
        result = place_order(
            client, 
            args.symbol, 
            args.side, 
            args.type, 
            args.qty, 
            args.price
        )
        
        if result:
            print("\n--- ORDER DETAILS ---")
            print(f"ID: {result['orderId']}")
            print(f"Avg Price: {result.get('avgPrice', 'N/A')}")
            print(f"Status: {result['status']}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
