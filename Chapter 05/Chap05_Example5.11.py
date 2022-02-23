import logging

logging.basicConfig(filename='mywarninglog.txt',level=logging.WARNING)
print("Displaying Warning level demo: ")
logging.debug('Debug message')
logging.info('Info message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')
