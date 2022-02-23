import re
mymatcher = re.finditer('\s','fx&A I#82%3')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) # PC1
print("------------------")
mymatcher = re.finditer('\S','fx&A I#82%3')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) # PC2
print("------------------")
mymatcher = re.finditer('\d','fx&A I#82%3')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) # PC3
print("------------------")
mymatcher = re.finditer('\D','fx&A I#82%3')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) # PC4
print("------------------")
mymatcher = re.finditer('\w','fx&A I#82%3_')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) # PC5
print("------------------")
mymatcher = re.finditer('\W','fx&A I#82%3_')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) # PC6
print("------------------")
mymatcher = re.finditer('\AThe','The Corono Virus in world')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) # PC7
print("------------------")
mymatcher = re.finditer(r"rld\b",'The Corono Virus in world')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) # PC8
print("------------------")
mymatcher = re.finditer(r'\Bect','A Temporary effect')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) # PC9
print("------------------")
mymatcher = re.finditer('effect\Z','A Temporary effect')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) # PC10
print("------------------")
mymatcher = re.finditer('.','fx&A\nI#82%3')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) # PC11