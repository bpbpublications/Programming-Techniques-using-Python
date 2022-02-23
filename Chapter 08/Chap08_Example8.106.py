from abc import ABC, abstractmethod


class Parent(ABC):
    @abstractmethod
    def mymethod1(self):
        pass

    def mymethod2(self):
        print('I am a Concrete method')


myobj = Parent()
