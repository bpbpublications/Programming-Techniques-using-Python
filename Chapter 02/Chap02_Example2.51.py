s1 = "   Good Morning   "
print("I am greeting you! " + s1) # -- RT1
print(len("I am greeting you! " + s1)) # -- RT2
print("I am greeting you! " + s1.rstrip())# -- RT3
print(len("I am greeting you! " + s1.rstrip())) # -- RT4
s2 = "  Python and C#"
print(s2.rstrip()) # -- RT5
print(s2.rstrip('#')) # -- RT6
s3 = "www.abc.com/"
print(s3.rstrip('/')) # -- RT7
s4 = 'apple,...ssssssssw'
print(s4.rstrip(',.ws')) # -- RT8
print(s4.rstrip('ws.,')) # -- RT9