#encode
s1 = 'Adoråble'
print(s1.encode('ascii','backslashreplace')) # -- E1
print(s1.encode("ascii","ignore")) # -- E2
print(s1.encode("ascii","namereplace")) # -- E3
print(s1.encode("ascii","replace")) # -- E4
print(s1.encode("ascii","xmlcharrefreplace")) # -- E5
print(s1.encode("ascii","strict")) # -- E6
