try:
    myfile1 = open("mydemofile.txt", "w")

    # Status of file objects before closing
    print("mydemofile closed status before closing is:", myfile1.closed)  # C1
finally:
    myfile1.close()

# Status of file objects after closing
print("mydemofile closed status after closing is:", myfile1.closed)  # C2
