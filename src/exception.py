# this is for custom exceptation 
# it will probably give you a  message how your message should look like inside your file with respect to your custom exceptation .we created own custom exception class which is inheriting from exception and also overridden  init method right over here and have create an error message variable inside this getting pupulated from this particular function and finally we print this right when  we raise a custom exception it is going to print the error

import logging
import sys
from src.logger import *

# Configure logging with a specific format and log level
logging.basicConfig(
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

def error_message_detail(error, error_detail: sys):
    """
    This function captures the details of the error, including the file name and line number where the error occurred.
    
    Args:
    error (Exception): The error that occurred.
    error_detail (sys): The sys module to extract exception information.

    Returns:
    str: A formatted string with the error details.
    """
    _, _, exc_tb = error_detail.exc_info()  # Extract the traceback object from the error details
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the file name where the error occurred
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)  # Format the error message with file name, line number, and error message
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        """
        Initialize the custom exception with the error message and details.

        Args:
        error_message (str): The error message.
        error_detail (sys): The sys module to extract exception information.
        """
        super().__init__(error_message)  # Initialize the base Exception class with the error message
        self.error_message = error_message_detail(error_message, error_detail=error_detail)  # Populate the custom error message with detailed information

    def __str__(self):
        """
        Return the custom error message when the exception is printed.
        """
        return self.error_message

# if __name__=="__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("divide by zero")
#         raise CustomException(e,sys)