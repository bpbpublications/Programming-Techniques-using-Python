import re
mymatcher = re.finditer('x','xyxxyxxxyxxxxy')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) #Q1
print("------------------")
mymatcher = re.finditer('x+','xyxxyxxxyxxxxy')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) #Q2
print("------------------")
mymatcher = re.finditer('x*','xyxxyxxxyxxxxy')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) #Q3
print("------------------")
mymatcher = re.finditer('x?','xyxxyxxxyxxxxy')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) #Q4
print("------------------")
mymatcher = re.finditer('x{3}','xyxxyxxxyxxxxy')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) #Q5
print("------------------")
mymatcher = re.finditer('x{3,5}','xyxxyxxxyxxxxy')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) #Q6
print("------------------")
mymatcher = re.finditer('^x','xyxxyxxxyxxxxy')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) #Q7
print("------------------")
mymatcher = re.finditer('y$','xyxxyxxxyxxxxy')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) #Q8