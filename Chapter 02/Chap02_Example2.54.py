s1 = 'Python is a User-Friendly language'
print(s1.startswith('Python')) # -- SW1
print(s1.startswith('python')) # -- SW2
print(s1.startswith('User',12)) # -- SW3
print(s1.startswith('User',12,16)) # -- SW4
print(s1.startswith('User',13,16)) # -- SW5
print(s1.startswith(('program','Python'))) # -- SW6
print(s1.startswith(('program','is','a'))) # -- SW7
print(s1.startswith(('User','is'),12,15)) # -- SW8
