import re 
  
mymatch=re.split('\s',"Python is awesome")
print(type(mymatch)) # SP1
print(mymatch) # SP2
for loop in mymatch: # SP3
    print(loop)
mytxt = "www.abc.com"
mymatch=re.split('\.',mytxt)
print(mymatch) # SP4
print(re.split('\W+', 'Fruits, fruits , Fruits')) # SP5
print(re.split('\W+', "Fruit's fruits Fruits")) # SP6
print(re.split('\W+', '25th March 2020, at 12:02 PM')) # SP7 
print(re.split('\d+', '25th March 2020, at 12:02 PM')) # SP8