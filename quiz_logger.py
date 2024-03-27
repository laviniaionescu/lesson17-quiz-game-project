import logging

import coloredlogs

logger = logging.getLogger(__name__)
# logging.basicConfig(format='%(levelname)s:%(message)s%(asctime)s', level=logging.DEBUG)
logging.basicConfig(format='%(levelname)s:%(message)s%(asctime)s', level=logging.DEBUG)
coloredlogs.install(level='DEBUG', logger=logger)

if __name__ == '__main__':


    logger.debug("Aici a un debug")
    logger.info("Aici e un info print")
    logger.warning("Aici e un warning")
    logger.error("Aici e o eroare")