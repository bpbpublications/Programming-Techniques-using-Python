from abc import ABC, abstractmethod
class Myengineer(ABC):
    @abstractmethod
    def mybranch(self):
        pass

myobj = Myengineer()
