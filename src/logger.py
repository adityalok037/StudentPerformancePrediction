import logging
import os
from datetime import datetime

# Define log file name with current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# This creates a log file name based on the current date and time in the format 'MM_DD_YYYY_HH_MM_SS.log'

# Define the logs directory and make sure it exists
logs_dir = os.path.join(os.getcwd(), "logs")
# Construct the path for the logs directory by joining the current working directory with 'logs'

os.makedirs(logs_dir, exist_ok=True)
# Create the 'logs' directory if it does not already exist. The 'exist_ok=True' argument avoids raising an error if the directory already exists.

# Define the full path for the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)
# Combine the logs directory path with the log file name to get the full path for the log file

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    # Set the log file location, format, and logging level
    # 'filename' specifies where to write the log messages
    # 'format' defines the log message format with timestamp, line number, logger name, log level, and message
    # 'level' sets the minimum level of messages to log (INFO level and above)
)

# Example logging statement
logging.info("Logging is configured and ready.")
# This logs an INFO level message to indicate that logging has been successfully configured
