import logging
import os


class LoggGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename= "logg//auto.log",format='%(asctime)s : %(levelname)s : %(message)s',datefmt='%m-%d-%y %I:%M:%S %p')

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        return logger
    
log=LoggGen.loggen()
log.info("*******************loging****************")
log.info("*******************loging****************")
log.info("*******************loging****************")
log.info("*******************loging****************")
log.info("*******************loging****************")
log.info("*******************loging****************")
log.info("*******************loging****************")