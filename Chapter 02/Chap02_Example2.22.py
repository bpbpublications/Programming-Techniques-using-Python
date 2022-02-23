#endswith
str1 = 'www.abc.com'
print(str1.endswith('com')) # -- EW1
print(str1.endswith('args')) # -- EW2
str2 = 'ISRO stands for Indian Space Research Organisation'
print(str2.endswith('Organisation')) # -- EW3
print(str2.endswith('Organisation.')) # -- EW4
print(str2.endswith('Organisation', 14)) # -- EW5
print(str2.endswith('ISRO', 0,3)) # -- EW6
print(str2.endswith('ISRO', 0,4)) # -- EW7
print(str2.endswith('for', 5,15)) # -- EW8
