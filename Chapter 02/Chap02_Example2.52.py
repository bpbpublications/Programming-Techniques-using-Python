s1 = "Python is a programming language"
print(s1.split()) # -- S1
print(s1.split('Python')) # -- S2
print(s1.split('a')) # -- S3
print(s1.split('a',1)) # -- S4
print(s1.split('a',2)) # -- S5
print(s1.split('a',3)) # -- S6
s2 = 'apple,litchi,grapes,mango'
print(s2.split(':')) # -- S7
print(s2.split(',',0)) # -- S8
print(s2.split(',',1)) # -- S9
print(s2.split(',',2)) # -- S10