print((lambda a, b, c: a + b + c)(11, 12, 13)) # IIFE1
print((lambda a, b, c=3: a + b + c)(11, 12)) # IIFE2
print((lambda a, b, c=3: a + b + c)(11, b=12)) # IIFE3
print((lambda *args: sum(args))(11,12,13)) # IIFE4
print((lambda **kwargs: sum(kwargs.values()))(Eleven=11, Twelve=12, Thirteen=13)) # IIFE5
print((lambda a, *, b=0, c=0: a + b + c)(11, b=12, c=13)) # IIFE6
