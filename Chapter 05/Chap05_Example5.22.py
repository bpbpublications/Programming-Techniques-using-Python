import logging

logging.basicConfig(filename='myerrorlog.txt',level=logging.INFO,
format='%(asctime)s: %(levelname)s-%(message)s', 
datefmt = '%d-%m-%Y %H:%M:%S %p')
logging.info("Division of 2 numbers:")
try:
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    print(num1/num2)
except ValueError as msg:
    print("Only numbers are allowed")
    logging.exception(msg)
except ZeroDivisionError as msg:
    print("Do not try to divide with zero")
    logging.exception(msg)
logging.info("End of the code") 