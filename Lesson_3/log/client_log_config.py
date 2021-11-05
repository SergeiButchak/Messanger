import os
import logging
import logging.handlers

LOG_PATH = 'logs'
LOG_FILE = 'client.log'

logger = logging.getLogger('client')
formatter = logging.Formatter("[%(asctime)s][%(levelname)s][%(module)s] %(message)s ")

if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)
filename = os.path.join(LOG_PATH, LOG_FILE)

fh = logging.handlers.TimedRotatingFileHandler(filename, encoding='utf-8', when='D', interval=1, backupCount=7)
fh.setFormatter(formatter)

logger.addHandler(fh)
logger.setLevel(logging.DEBUG)