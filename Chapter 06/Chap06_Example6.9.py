import re

mypattern = input("Please write the pattern to check: ")
mymatch = re.search(mypattern, "101101110")
if mymatch != None:
    print("We have found match")
    print("Start Index is :", mymatch.start(), "and End Index is :", mymatch.end())
else:
    print("We have not found the match")
