from abc import ABC, abstractmethod
class Myengineer(ABC):
    @abstractmethod
    def mybranch(self):
        pass

class MyEEE(Myengineer):
    def mybranch(self):
        print("I am an electrical and electronics Engineer")

myobj = MyEEE()
myobj.mybranch()
