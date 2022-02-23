#random bytearray
randomByteArray = bytearray('DEF', 'utf-8')
mv1 = memoryview(randomByteArray)
print(mv1[0]) #-- MV1
print(bytes(mv1[0:2])) #-- MV2
print(list(mv1[0:3])) #-- MV3
