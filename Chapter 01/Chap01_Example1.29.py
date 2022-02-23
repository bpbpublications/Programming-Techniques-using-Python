print('Hello "Students"  World')

# We cannot use single quote inside single quote as we will be getting syntax error

#  ------- print("Hello  "Students" World")
print("I'm here")
print()
print('I am printing after a new line')
print('Hello \t Python Beginners')
print('Hello ' + '! I hope you are enjoying print function')
print('Hi '*2)
print('Hello','I am printing space without concatenation operator')

x,y,z = 3,4,5
print('The ratio of x,y and z are ', x,y,z,sep = ':')

print('Hello',end=' ')
print('Python',end=' ')
print('Beginners.',end=' ')
print('This',end=' ')
print('is',end=' ')
print('an',end=' ')
print('example',end=' ')
print('of',end=' ')
print('end',end=' ')
print('attribute')

li = [1,2,3,4] # list
t1 = (5,6,7,8) # tuple
s1 = {9,10,11,12} # set
print(li,t1,s1)
print(li,end = ' ')
print(t1,end = ' ')
print(s1)

r,s,t = 3,4,5
print('r value is %i'%r) # f1
print('r value is %i and s value is %i' %(r,s)) # f2

my_name = 'Python'
l1 = [3,4,5,6]
print("Hello %s . The list is as follows %s " %(my_name,l1))

name = 'Ram'
salary = 100000
age = 22 
print("Hello I am {0}. My age is {1} years old and salary is {2}".format(name,age,salary)) # M-1
print("Hello I am {}. My age is {} years old and salary is {}".format(name,age,salary)) # M-2
print("Hello I am {x}. My age is {y} years old and salary is {z}".format(z = salary, x = name, y = age)) # M-3
print(f"Hello I am {name}. My age is {age} years old and salary is {salary}") # M-4

newline = ord('\n') 
print(f"Hi: I am {newline}")