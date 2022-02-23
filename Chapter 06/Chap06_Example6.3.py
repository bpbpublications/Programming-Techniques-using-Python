import re
mycount = 0
mymatcher = re.finditer('10','1000010000100101')
for loop in mymatcher:
    mycount += 1
    print("starting {}: ,ending index {} and group is {}  " .format(loop.start(), loop.end(), loop.group()))
print("The total occurrences of pattern '10' is: ", mycount)
