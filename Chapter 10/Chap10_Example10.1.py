import threading
x = int('12')
print(x)
print("The current executing thread name is: ",threading.current_thread().getName()) 
