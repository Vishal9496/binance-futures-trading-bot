def validate_cli_args(args, logger):
    """
    Validates user input before sending anything to Binance.
    We don't want to accidentally order 0 quantity or place a limit order without a price!
    """
    if args.quantity <= 0:
        logger.error("Quantity must be greater than 0.")
        return False

    if args.type == 'LIMIT' and args.price is None:
        logger.error("Price is absolutely REQUIRED for LIMIT orders. (Like our ₹200 Biryani rule!)")
        return False
        
    if args.type == 'MARKET' and args.price is not None:
        logger.warning("You provided a price for a MARKET order. The bot will ignore the price and execute at market value.")

    if not args.symbol.endswith('USDT'):
        logger.warning(f"Symbol {args.symbol} doesn't end with USDT. Ensure it's a valid USDT-M testnet pair.")

    return True