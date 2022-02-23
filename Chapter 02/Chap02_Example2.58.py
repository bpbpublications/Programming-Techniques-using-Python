s1 = "rst"
s2 = "uvw"
s3 = "xy"
string = "xytabc"
print(string) # -- TR1
translation = string.maketrans(s1, s2, s3)
print(string.translate(translation)) # -- TR2

translation = {100: None, 101: None, 102: 103}
string = "abcdef"
print(string) # -- TR3
print(string.translate(translation)) # -- TR4