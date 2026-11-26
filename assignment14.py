import logging

# Configure logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("program.log"),
        logging.StreamHandler()
    ]
)

# Display different logging messages
logging.debug("Debugging the program")
logging.info("Program executed successfully")
logging.warning("This is a warning message")
logging.error("An error has occurred")
logging.critical("Critical error detected")

#2026-11-25 09:15:54,464 - DEBUG - Debugging the program
#2026-11-25 09:15:54,465 - INFO - Program executed successfully
#2026-11-25 09:15:54,465 - WARNING - This is a warning message
#2026-11-25 09:15:54,465 - ERROR - An error has occurred
#2026-11-25 09:15:54,465 - CRITICAL - Critical error detected