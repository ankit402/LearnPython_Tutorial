from logger import logging

def add(a, b):
    try:
        logging.info("adding {} to {}".format(a, b))
        c = a + b
        logging.info("adding {} ".format(c))
        return a + b
    except Exception as e:
        logging.error("Error occured for calculating  {}".format(e))

add(4,7)