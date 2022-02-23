import logging

num1 = 3
num2 = 0
try:
  divres = num1 / num2
except Exception as e:
  logging.error("Displaying Exception", exc_info=True)
