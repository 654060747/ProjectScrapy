import logging
from logging import Formatter, FileHandler

logger = logging.getLogger('scrapys')
logger.setLevel(logging.INFO)

handler = FileHandler('./xx.log')
handler.setLevel(logging.INFO)
handler.setFormatter(Formatter(fmt='%(asctime)s: %(message)s',datefmt='%Y-%m-%d %H-%M-%S'))

logger.addHandler(handler)
