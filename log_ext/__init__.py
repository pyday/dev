__author__ = 'wangcl'

import logging
from logging.handlers import RotatingFileHandler
import os


def getLogger(name, level=logging.DEBUG):
    logger = logging.getLogger(name)
    path = os.path.join(os.path.dirname(__file__), "../logs/" + name + ".log")
    hdlr = RotatingFileHandler(path, maxBytes=5 * 1024 * 1024, backupCount=2)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG)
    return logger
