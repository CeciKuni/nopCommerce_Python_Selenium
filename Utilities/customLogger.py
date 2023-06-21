import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename='.\\Logs\\automation.log', level=logging.INFO, force=True,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p'
                            )
        logger = logging.getLogger()
        return logger