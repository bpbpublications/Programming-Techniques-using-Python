with open("myfileno.txt",'w') as myfile1:
    print("The file descriptor is: ", myfile1.fileno()) # FN1
print("The file descriptor is: ", myfile1.fileno()) # FN2
