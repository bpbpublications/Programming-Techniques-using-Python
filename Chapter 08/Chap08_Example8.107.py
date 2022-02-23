from abc import ABC, abstractmethod
class Parent(ABC):
    @abstractmethod
    def mymethod1(self):
        pass
    
    def mymethod2(self):
        print('I am a Concrete method')

class MyChild(Parent):
    def mymethod1(self):
        print("I am defining abstract method")

myobj = MyChild()
myobj.mymethod1()
myobj.mymethod2()