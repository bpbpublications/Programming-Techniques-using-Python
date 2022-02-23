class Parent:
    def result(self,num1,num2):
        print(f"Subtraction of numbers {num1} and {num2} is", num1-num2)
    
class Child(Parent):
    def mydisplay(self):
        print('Hey I am a child class')
    
    def result(self,num1,num2):
        print(f"Addition of numbers {num1} and {num2} is", num1+num2)

mychild = Child()
mychild.result(3,4)

myparent = Parent()
myparent.result(3,4)