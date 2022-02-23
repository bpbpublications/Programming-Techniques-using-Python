s1 = 'His Name is ABC'
print(s1) # -- SP1
print(s1.splitlines()) # -- SP2
s2 = 'His\nName is\nABC'
print(s2.splitlines()) # -- SP3
print(s2.splitlines(True)) # -- SP4
s3 = 'What\r a\n Game'
s4 = s3.splitlines()
print(s4) # -- SP5
print("".join(s4)) # -- SP6
