import threading
from time import sleep


def multiply_two():
    for i in range(11):
        print(f"2*{i} = {i * 2}")
        sleep(1)
    print("Child Thread Completed")


def multiply_three():
    for i in range(11):
        print(f"3*{i} = {i * 3}")


myt1 = threading.Thread(target=multiply_two)
myt1.start()
myt1.join(5)
multiply_three()
print("Main Thread Completed")
