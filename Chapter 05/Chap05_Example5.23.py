import logging

mylogger = logging.getLogger(__name__)

my_handler = logging.FileHandler('myfilelog.txt')
my_handler.setLevel(logging.ERROR)

my_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
my_handler.setFormatter(my_format)

mylogger.addHandler(my_handler)
mylogger.error('This is an error')
