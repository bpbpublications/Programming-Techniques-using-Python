import re
mytxt = '123 \n123 gfh'
mypattern = '\s'
myreplace = ''
mystr = re.subn(mypattern, myreplace, mytxt) 
print(mystr) # SUBN1
print(type(mystr))
print(mystr[0])
print(mystr[1])
print("-------------")
mystr = re.subn(mypattern, myreplace, mytxt,count =1) 
print(mystr) # SUBN2
print("-------------")
print(re.subn('st', '*#' , 'Stay safe, stay healthy', flags = re.IGNORECASE)) # SUBN3
print("-------------")
print(re.subn('st', '*#' , 'Stay safe, stay healthy')) # SUBN4
print("-------------")
print(re.subn('st', '*#' , 'Stay safe, stay healthy', count = 1, flags = re.IGNORECASE)) # SUBN5
print("-------------")
print(re.subn('\sAND\s', ' & ' , 'The prince and the pauper', count = 1, flags = re.IGNORECASE)) # SUBN6