s1 = "Save Plant Save Environment!save Plant Save Environment!save 	Plant Save Environment!"
print(s1.rfind('Save')) # -- S1
print(s1.rfind('demo')) # -- S2
print(s1.rfind('save')) # -- S3
print(s1.rfind('save',57)) # -- S4
print(s1.rfind('Environment',15,22)) # -- S5
print(s1.rfind('Environment',15,32)) # -- S6
s2 = 'Fabulous'
print(s2.rfind('u')) # -- S7
print(s2.rfind('o',5)) # -- S8
print(s2.rfind('o',6)) # -- S9
s3 = "Horror"
print(s3.rfind('r')) # -- S10
print(s3.rfind('r',-5)) # -- S11
print(s3.rfind('r',-2,-5)) # -- S12
print(s3.rfind('r',-5,-2)) # -- S13