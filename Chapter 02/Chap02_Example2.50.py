s1 = "Python is a programming language"
print(s1.rsplit()) # -- RS1
print(s1.rsplit('Python')) # -- RS2
print(s1.rsplit('a')) # -- RS3
print(s1.rsplit('a',1)) # -- RS4
print(s1.rsplit('a',2)) # -- RS5
print(s1.rsplit('a',3)) # -- RS6
s2 = 'apple,litchi,grapes,mango'
print(s2.rsplit(':')) # -- RS7
print(s2.rsplit(',',0)) # -- RS8
print(s2.rsplit(',',1)) # -- RS9
print(s2.rsplit(',',2)) # -- RS10