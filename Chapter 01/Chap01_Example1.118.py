#bool 
print(True+True) # -- B1
print(True+False) # -- B2
print(False+False) # -- B3
print(True*3) # -- B4
print(True/True) # -- B5
print(True/3) # -- B6

var_bool1 = False
print(bool(var_bool1)) # -- B7 
  
var_bool1 = True
print(bool(var_bool1))  # -- B8
  
var_bool1 = 15
var_bool2 = 20
print(bool(var_bool1==var_bool2)) # -- B9
  
var_bool1 = None
print(bool(var_bool1))  # -- B10
  
var_bool1 = () 
print(bool(var_bool1))  # -- B11
  
var_bool1 = {} 
print(bool(var_bool1))  # -- B12
  
var_bool1 = 0.0
print(bool(var_bool1))  # -- B13

var_bool1 = 1.0
print(bool(var_bool1))  # -- B14
  
var_bool1 = 'Python'
print(bool(var_bool1))  # -- B15
