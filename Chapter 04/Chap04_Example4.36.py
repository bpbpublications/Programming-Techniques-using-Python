def fname(myname, *args, funcname = 'Undefined',**kwargs):
    print(myname)
    print(args)
    print(funcname)
    print(kwargs)

fname('Saurabh',1,2,3,4,5,6,a1=1,name1="Hello") # ML1
print("---------------------------------------------")
fname('Priyanka',11,12,13,14,15,16,funcname = "PADK", a1=2,name1="demo") # ML2
