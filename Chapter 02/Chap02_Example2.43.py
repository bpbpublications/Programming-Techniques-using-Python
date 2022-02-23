d1 = {'d':'l',"e":'o',"f":'t'}
s1 = "def"
print(s1.maketrans(d1)) # -- MT1

a1 = "sail"
b1 = "1234"
str1 = "simple awesome indian lost"
print(str1.maketrans(a1,b1)) # -- MT2
print(str1.translate(str1.maketrans(a1,b1))) # -- MT3

firstString = "def"
secondString = "ghi"
thirdString = "deg"
string = ""
print(string.maketrans(firstString, secondString, thirdString)) # -- MT4