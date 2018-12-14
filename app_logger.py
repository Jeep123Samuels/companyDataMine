"""App logger."""

import logging

from config import APP_NAME, LOGGING_LEVEL

logger: object = logging.getLogger(APP_NAME)
handler: object = logging.StreamHandler()
formatter: object = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(LOGGING_LEVEL)
