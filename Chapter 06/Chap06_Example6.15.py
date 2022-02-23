import re
mystr = '\n and \t are escape sequences.'
myres = re.findall(r'[\n\t]', mystr)
print(myres)
