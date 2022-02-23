class Parent:
    def result(self,num1,num2):
        print(f"Subtraction of numbers {num1} and {num2} is", num1-num2)
    
class Child(Parent):
    def mydisplay(self):
        print('Hey I am a child class')
    
    def result(self,num1,num2):
        super().result(10,9)
        print(f"Addition of numbers {num1} and {num2} is", num1+num2)

mychild = Child()
mychild.result(3,4)