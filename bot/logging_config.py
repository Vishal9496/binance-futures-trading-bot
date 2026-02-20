import logging
import sys

def setup_logger():
    """
    Sets up a logger that outputs to both a file and the console.
    It's like having WhatsApp read receipts (console) and a chat backup (file).
    """
    logger = logging.getLogger("TradingBot")
    logger.setLevel(logging.INFO)

    # Prevent adding multiple handlers if logger is called multiple times
    if not logger.handlers:
        # File Handler - saves logs to a file
        file_handler = logging.FileHandler("trading_bot.log")
        file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)

        # Console Handler - prints to your terminal
        console_handler = logging.StreamHandler(sys.stdout)
        console_formatter = logging.Formatter('%(levelname)s: %(message)s')
        console_handler.setFormatter(console_formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger