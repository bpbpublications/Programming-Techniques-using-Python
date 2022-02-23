from threading import *


class abc:
    def __init__(self, seat_available):  # ML1
        self.seat_available = seat_available

    def abc_reserveseat(self, seat_required):  # ML2
        print("Number of seats remaining : ", self.seat_available)
        if self.seat_available >= seat_required:  # ML3
            print(f"{current_thread().name} was alloted the seat No. L{self.seat_available}")
            self.seat_available = self.seat_available - 1
        else:
            print("All the seats are booked now Sorry !")


obj_abc = abc(1)  # ML4
myt1 = Thread(target=obj_abc.abc_reserveseat, args=(1,), name='Saurabh')
myt2 = Thread(target=obj_abc.abc_reserveseat, args=(1,), name='Nilesh')
myt1.start()
myt2.start()
