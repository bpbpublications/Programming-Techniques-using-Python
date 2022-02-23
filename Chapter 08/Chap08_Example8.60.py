class Mymath1:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def normal_addition(self):
        return self.num1 + self.num2
    
    def normal_subtraction(self):
        return self.num1 - self.num2

class Mymath2:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def normal_multiplication(self):
        return self.num1 * self.num2
    
    def normal_division(self):
        return self.num1 / self.num2

class Mymath3:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        self.obj1 = Mymath1(num1,num2) # L1
        self.obj2 = Mymath2(num1,num2) # L2
        
    def normal_power(self): # L3
        return self.num1 ** self.num2
    
    def normal_addition(self): # L4
        return self.obj1.normal_addition()

    def normal_subtraction(self): # L5
        return self.obj1.normal_subtraction()
    
    def normal_multiplication(self): # L6
        return self.obj2.normal_multiplication()
    
    def normal_division(self): # L7
        return self.obj2.normal_division()

myobj3 = Mymath3(6,3) # L8
print(myobj3.normal_addition()) # L9
print(myobj3.normal_subtraction()) # L10
print(myobj3.normal_multiplication()) # L11
print(myobj3.normal_division()) # L12
print(myobj3.normal_power()) # L13