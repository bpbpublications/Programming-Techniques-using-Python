import re
mymatcher = re.finditer('[xyz]','djx&AI#82%3U')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) # CC1
print("------------------")
mymatcher = re.finditer('[^xyz]','djx&AI#82%3U')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) # CC2
print("------------------")
mymatcher = re.finditer('[a-z]','djx&AI#82%3U')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) # CC3
print("------------------")
mymatcher = re.finditer('[A-Z]','djx&AI#82%3U')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) # CC4
print("------------------")
mymatcher = re.finditer('[a-zA-Z]','djx&AI#82%3U')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) # CC5
print("------------------")
mymatcher = re.finditer('[0-9]','djx&AI#82%3U')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) # CC6
print("------------------")
mymatcher = re.finditer('[0-6][0-9]','djx&AI#82%3U1059')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) # CC7
print("------------------")
mymatcher = re.finditer('[aeiou]','djx&AI#82%3U')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) # CC8
print("------------------")
mymatcher = re.finditer('[^aeiou]','djx&AI#82%3U')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) # CC9
print("------------------")
mymatcher = re.finditer('[a-zA-Z0-9]','djx&AI#82%3U')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) # CC10
print("------------------")
mymatcher = re.finditer('[^a-zA-Z0-9]','djx&AI#82%3U')
for loop in mymatcher:
    print(loop.start(), '.....', loop.group()) # CC11