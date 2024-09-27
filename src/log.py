
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='output.log', max_bytes=1024 * 1024, backup_count=5):
    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Create a rotating file handler
    file_handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    file_handler.setLevel(logging.INFO)

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Add the formatter to the file handler
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    return logger