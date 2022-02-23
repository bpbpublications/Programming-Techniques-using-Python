import pickle


class Student:
    def __init__(self, name, age, rollno, hometown):
        self.name = name
        self.age = age
        self.rollno = rollno
        self.hometown = hometown

    def mydisplay(self):
        print(self.name, "\t", self.age, "\t", self.rollno, "\t", self.hometown)


with open("mypick_unpickfile.dat", "wb") as myfile1:
    mystu1 = Student('Shyam', 12, 1, "HYD")
    pickle.dump(mystu1, myfile1)
    print("Pickling of Student Object completed...")

with open("mypick_unpickfile.dat", "rb") as myfile1:
    myobj = pickle.load(myfile1)
    print("Printing Student Information after unpickling")
    myobj.mydisplay()
