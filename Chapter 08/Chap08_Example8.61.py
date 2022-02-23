class Myfather:
    age = 55 # class variable
    
    def myfatherhobby(self): # instance method
        print("My father's hobby is to listen Music and News")
    
    @classmethod
    def myfatherfood(cls): # class method
        print("My father love to eat roti and sabji")
    
    @staticmethod 
    def myfatherprofession():# static method
        prof = 'doctor'
        print("My father by profession is a ", prof)

class Iamson(Myfather):
    def hobby(self):
        print("I love to help others those who are in need")

myobj = Iamson()
myobj.hobby()
myobj.myfatherhobby()
myobj.myfatherfood()
myobj.myfatherprofession()
print(myobj.age)
print('*'*25)
myobj2 = Myfather()
myobj2.myfatherhobby()
myobj2.myfatherfood()
myobj2.myfatherprofession()
print(myobj2.age)