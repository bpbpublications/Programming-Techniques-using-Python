import re

mypattern = input("Please write the pattern to check: ")
mymatch = re.fullmatch(mypattern, "rstuvwxyz")
if mymatch != None:
    print("We have found match at the whole string")
    print("Start Index is :", mymatch.start(), "and End Index is :", mymatch.end())
else:
    print("We have not found match at the whole string")
