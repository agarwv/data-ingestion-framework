
import logging
from logging.handlers import RotatingFileHandler

def setup_logging():
    logger = logging.getLogger("IngestionFramework")
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        fh = RotatingFileHandler("logs/ingestion.log", maxBytes=1000000, backupCount=3)
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger
