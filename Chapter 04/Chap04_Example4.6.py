def my_complex(my_real, my_imag):
    my_result = complex(my_real,my_imag)
    return my_result

print(my_complex(my_real = 2,my_imag = 8)) # K1
print(my_complex(my_imag = 8, my_real = 2)) # K2
print(my_complex(2,my_imag = 8)) # K3
