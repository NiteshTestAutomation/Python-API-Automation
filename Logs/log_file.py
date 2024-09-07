import logging
import os
current_log_file_path = os.path.join(os.path.abspath(__file__ + "/../../"), "Logs/Current_logfile.log")


def generateLog():
    logger = logging.getLogger()
    filehandler = logging.FileHandler(current_log_file_path,mode="w")
    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s',
                                  datefmt='%d/%m/%Y %I:%M:%S %p')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.DEBUG)
    return logger


# logger.debug("Debug message")
# logger.info("Information regarding the test case")
# logger.warning("Test case pass but with a Warning message")
# logger.error("Test case fail")
# logger.critical("Important test case fail on which other test case depends")

