import gc
print("The above method will check whether GC is enebled or disabled")
print(gc.isenabled())
print("The above method will diable the GC explicitly")
gc.disable()
print(gc.isenabled())
print("The above method will enable the GC explicitly")
gc.enable()
print(gc.isenabled())
