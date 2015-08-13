__author__ = 'wangcl'

import logging
import os



def getLogger(name, level=logging.DEBUG):
    logger = logging.getLogger(name)
    path = os.path.join(os.path.dirname(__file__), "../logs/" + name + ".log")
    hdlr = logging.FileHandler(path)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG)
    return logger
