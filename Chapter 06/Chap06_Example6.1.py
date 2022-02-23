import re
mypattern=re.compile('re')
print(type(mypattern)) # C1
myans=mypattern.findall('regular expressions')
print(myans) # C2
print(mypattern.findall('recursive')) # C3

chk_name = re.compile(r"[^A-Za-zs.]")
myname = input("Kindly, enter the name: ")
while chk_name.search(myname):
    print("Kindly enter the name correctly!")
    myname = input("Kindly, enter the name: ") # C4
