import re
mytxt = '123 \n123 gfh'
mypattern = '\s'
myreplace = ''
mystr = re.sub(mypattern, myreplace, mytxt) 
print(mystr) # SUB1
print("-------------")
mystr = re.sub(mypattern, myreplace, mytxt,count =1) 
print(mystr) # SUB2
print("-------------")
print(re.sub('st', '*#' , 'Stay safe, stay healthy', flags = re.IGNORECASE)) # SUB3
print("-------------")
print(re.sub('st', '*#' , 'Stay safe, stay healthy')) # SUB4
print("-------------")
print(re.sub('st', '*#' , 'Stay safe, stay healthy', count = 1, flags = re.IGNORECASE))
 # SUB5
print("-------------")
print(re.sub(r'\sAND\s', ' & ' , 'The prince and the pauper', flags = re.IGNORECASE))
 # SUB6