import logging

logging.basicConfig(level=10)
print("Displaying Debug level demo: ")
print("The contents inside the file mydebuglog.txt is:")
logging.debug('Debug message')
logging.info('Info message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')
