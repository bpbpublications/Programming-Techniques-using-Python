from threading import *


class abc:
    def __init__(self, seat_available):
        self.seat_available = seat_available
        self.mylock = Lock()

    def abc_reserveseat(self, seat_required):
        self.mylock.acquire()
        print("Number of seats remaining : ", self.seat_available)
        if self.seat_available >= seat_required:
            print(f"{current_thread().name} was alloted the seat No. L{self.seat_available}")
            self.seat_available = self.seat_available - 1
        else:
            print("All the seats are booked now Sorry !")
        self.mylock.release()


obj_abc = abc(2)
myt1 = Thread(target=obj_abc.abc_reserveseat, args=(1,), name='Saurabh')
myt2 = Thread(target=obj_abc.abc_reserveseat, args=(1,), name='Nilesh')
myt3 = Thread(target=obj_abc.abc_reserveseat, args=(1,), name='Divya')
myt1.start()
myt2.start()
myt3.start()
print("Main Thread")
