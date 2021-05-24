import logging
from logging import Formatter, FileHandler

logger = logging.getLogger('liuliu')
logger.setLevel(logging.INFO)

handler = FileHandler('./liuliu.log')
handler.setLevel(logging.INFO)
handler.setFormatter(Formatter(fmt='%(asctime)s: %(message)s',datefmt='%Y-%m-%d %H-%M-%S'))

logger.addHandler(handler)