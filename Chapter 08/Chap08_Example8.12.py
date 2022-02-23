def mycatch(myfunc):
    def func1(num1,num2):
        print("Dividing ",num1," with ",num2)
        if num2==0:
            print("We cannot divide if num2 is 0")
            return
        return myfunc(num1,num2) 
    return func1

@mycatch
def mydivision(num1,num2):
    return num1/num2

print(mydivision(10,3))
print(mydivision(10,2))
print(mydivision(10,0))