s1 = 'Python is one of the best programming language'
print(s1.rpartition('Python')) # -- RP1
print(s1.rpartition('here')) # -- RP2
print(s1.rpartition('yth')) # -- RP3
print(s1.rpartition('best')) # -- RP4
print(s1.rpartition('language')) # -- RP5
s2 = 'Python is one of the best programming language. I love Python'
print(s2.rpartition('Python')) # -- RP6
