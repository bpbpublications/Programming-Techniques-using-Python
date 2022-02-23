try:
    # file creation
    myfile1 = open("myflush.txt", "w")

    # writing data in the file
    myfile1.write("Hello beginner!")

    # clearing the internal buffer
    myfile1.flush()

    # writing the data again
    myfile1.write("I hope you are enjoying python file handling")

    # again flushing the internal buffer
    myfile1.flush()

    # writing the data again
    myfile1.write("\nI hope yes")

    # file getting closed
    myfile1.close()

    # reading entire file contents
    myfile1 = open("myflush.txt", "r")
    print(myfile1.read())
finally:
    myfile1.close()
