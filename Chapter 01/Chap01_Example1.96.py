#in and not in operators
s1 = 'I am a Python Beginner'
print('I' in s1) # M1
print('Python' in s1) # M2
print('python' not in s1) # M3

s2 = ['apple','mango','litchi']
print('grapes' in s2) # M4
print('grapes' not in s2) # M5
print('litchi' in s2) # M6

s3 = (1,2,3,4)
print(3 not in s3) # M7
print(5 not in s3) # M8
print(1 in s3) # M9

s4 = {'cricket','football','hockey'}
print('badminton' not in s4) # M10
print('snooker' not in s4) # M11
print('chess' in s4) # M12

s5 = {'a':1, 'e':2, 'i':3,'o':4,'u':5}
print('a' in s5) # M13
print(4 in s5) # M14
print(4 not in s5) # M15