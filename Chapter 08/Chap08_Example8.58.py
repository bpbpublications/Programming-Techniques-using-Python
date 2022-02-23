from time import sleep
class Demo:
    def __init__(self):
        print("Initializing the object")
    def __del__(self):
        print("clean up activities are performed...")
myobj=Demo()
myobj1 = myobj
myobj2 = myobj1
print("Deleting myobj reference variable")
print("*"*25)
del myobj
sleep(2)
print("object is not yet destroyed after deleting myobj")
print("Deleting myobj1 reference variable")
print("*"*25)
del myobj1
sleep(2)
print("object is still not yet destroyed even after deleting myobj1")
print("Deleting myobj2 reference variable")
del myobj2 
print("*"*25)
print("Application end")