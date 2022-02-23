from abc import ABC, abstractmethod
class Myengineer(ABC):
    @abstractmethod
    def mybranch(self):
        pass

class MyEEE(Myengineer):
    pass

myobj = MyEEE()
