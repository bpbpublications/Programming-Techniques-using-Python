s1 = "   Good Morning   "
print(s1) # -- S1
print(len(s1)) # -- S2
print( s1.strip())# -- S3
print(len(s1.strip())) # -- S4
s2 = "  Python and C#"
print(s2.strip()) # -- S5
print(s2.strip('#')) # -- S6
s3 = "www.abc.com/"
print(s3.strip('@')) # -- S7
s4 = 'apple,...ssssssssw'
print(s4.strip(',.ws')) # -- S8
print(s4.strip('ws.,')) # -- S9
s5 = '#banana#'
print(s5.strip('#')) # -- S10
print(s5.rstrip('#')) # -- S11
print(s5.lstrip('#')) # -- S12