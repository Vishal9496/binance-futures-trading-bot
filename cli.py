import argparse
import os
import sys
from dotenv import load_dotenv

from bot.logging_config import setup_logger
from bot.client import BinanceTestnetClient
from bot.orders import OrderManager
from bot.validators import validate_cli_args

def main():
    # 1. Setup Logging
    logger = setup_logger()
    
    # 2. Parse Command Line Arguments
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot ")
    parser.add_argument('--symbol', type=str, required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument('--side', type=str, choices=['BUY', 'SELL'], required=True, help="Order side: BUY or SELL")
    parser.add_argument('--type', type=str, choices=['MARKET', 'LIMIT'], required=True, help="Order type: MARKET or LIMIT")
    parser.add_argument('--quantity', type=float, required=True, help="Amount to buy/sell")
    parser.add_argument('--price', type=float, help="Price (Required for LIMIT orders)")
    
    args = parser.parse_args()

    # 3. Validate Inputs
    if not validate_cli_args(args, logger):
        sys.exit(1)

    # 4. Load Environment Variables (API Keys)
    load_dotenv()
    api_key = os.getenv("BINANCE_TESTNET_API_KEY")
    api_secret = os.getenv("BINANCE_TESTNET_API_SECRET")

    if not api_key or not api_secret:
        logger.error("API Keys missing! Please set BINANCE_TESTNET_API_KEY and BINANCE_TESTNET_API_SECRET in your .env file.")
        sys.exit(1)

    # 5. Initialize Client & Execute Order
    try:
        binance_client = BinanceTestnetClient(api_key, api_secret, logger).get_client()
        order_manager = OrderManager(binance_client, logger)
        
        order_manager.place_order(
            symbol=args.symbol.upper(),
            side=args.side.upper(),
            order_type=args.type.upper(),
            quantity=args.quantity,
            price=args.price
        )
    except Exception as e:
        logger.error(f"Bot execution failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()