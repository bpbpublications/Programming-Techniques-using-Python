def myupper(mystr):
    return mystr.upper()

def mylower(mystr):
    return mystr.lower()

def world_virus(myfunc):
    virus = myfunc("CoronA")
    print(virus)

world_virus(myupper) # FF1
world_virus(mylower) # FF2
