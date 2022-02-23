from time import sleep
class Demo:
    def __init__(self):
        print("Initializing the object")
    def __del__(self):
        print("clean up activities are performed...")
myobj=Demo()
myobj = None #L2
sleep(5)
print("Application end")
