import logging

logging.basicConfig(level=logging.INFO)

print(type(logging))
logging.debug("hidden")
logging.info("shown")
logging.warning("shown")
logging.error('shown')