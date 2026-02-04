import logging
import os

def setup_logger():
    if not os.path.exists('logs'):
        os.makedirs('logs')

    logger = logging.getLogger("TradingBot")
    logger.setLevel(logging.INFO)

    # File Handler
    fh = logging.FileHandler('logs/trading.log')
    fh.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    
    # Console Handler
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))

    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger

logger = setup_logger()
