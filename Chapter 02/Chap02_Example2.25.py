#format
print("Hello {} beginners. The value of pi is {} ".format('Python',3.14159)) # -- FO1
print("Hello {0} beginners. The value of pi is {1} ".format('Python',3.14159)) # -- FO2
print("Hello {lang} beginners. The value of pi is {pi:9.3f} ".format(lang = 
'Python',pi = 3.14159)) 
# -- FO3
print("Hello {0} beginners. The value of pi is {pi:9.3f} ".format('Python',pi = 3.14159)) 
# -- FO4

print("The number is {:d}".format(654)) # -- FO5
print("The float number is {:f}".format(987.34567)) # -- FO6
print("bin {0:b} octal {0:o} hex {0:x}".format(10)) # -- FO7

print("{:4d}".format(56)) # -- FO8
print("{:3d}".format(987654)) # -- FO9
print("{:6.2f}".format(86.45468)) # -- FO10
print("{:03d}".format(1)) # -- FO11
print("{:06.2f}".format(86.45468)) # -- FO12

print("{:+f} {:+f}".format(33.36, -33.36)) # -- FO13
print("{:-f} {:-f}".format(33.36, -33.36)) # -- FO14
print("{: f} {: f}".format(33.36, -33.36)) # -- FO15

print("{:6d}".format(13)) # -- FO16
print("{:^10.2f}".format(86.45468)) # -- FO17
print("{:<06d}".format(13)) # -- FO18
print("{:=8.4f}".format(-86.45468)) # -- FO19

print("{:6}".format("top")) # -- FO20
print("{:>6}".format("top")) # -- FO21
print("{:^6}".format("top")) # -- FO22
print("{:*^6}".format("top")) # -- FO23

print("{:.4}".format("Lycopersicum")) # -- FO24
print("{:4.3}".format("Lycopersicum")) # -- FO25
print("{:^4.3}".format("Lycopersicum")) # -- FO26

num = 100000000  
print("dec: {:,}".format(num))  # -- FO27
print("dec: {:.3%}".format(33/9)) # -- FO28