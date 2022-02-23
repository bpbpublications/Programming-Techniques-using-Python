class Heart:
    myheart = 4 # class variable
    @classmethod # decorator
    def mylivingbeing(cls,myname): # class method with parameter
        print(f"{myname} have {cls.myheart} chambered heart") # accessing class variable inside class method

Heart.mylivingbeing('Crocodile') # calling class method with argument
Heart.mylivingbeing('Human') # calling class method with argument
