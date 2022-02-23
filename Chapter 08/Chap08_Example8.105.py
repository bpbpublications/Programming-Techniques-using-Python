class TV:
    
    def __init__(self):
        self.__mysonytvprice = 55000
	
    def mysell(self):
        print("The Selling Price is : {}".format(self.__mysonytvprice))

    def myMaxPrice(self, myprice):
        self.__mysonytvprice = myprice

myobj = TV()
myobj.mysell()

# trying to change the price
myobj.__mysonytvprice = 56000
myobj.mysell()

myobj.myMaxPrice(54000)
myobj.mysell()