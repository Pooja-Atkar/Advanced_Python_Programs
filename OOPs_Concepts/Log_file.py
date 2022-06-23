import logging

# Generate logs.log file.
# We can see log information on the logs.log file.

logging.basicConfig(filename="logs.log",format='%(asctime)s %(message)s',filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

str = "www.google.com"
logger.debug(str)
logger.info("I am information level")
logger.warning("It is a warning")
logger.error("It is error")
logger.critical("It is critical")

try:
    print(10/0)
except Exception as e:
    logger.exception(e)  # OR # Also we can write  # logger.error(e,exc_info=True)

# If level not set then by default is warning.
# If set critical level then skip all the below priority means warning and error.show only critical error.
# Generally we set DEBUG level.