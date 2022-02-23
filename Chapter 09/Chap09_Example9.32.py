# importing necessary modules
from zipfile import ZipFile

# zip file name is specified
myfile_name = "E:\\python_progs\\zip\\myfiles.zip"

# by default zip file opening in READ mode
with ZipFile(myfile_name, 'r') as myzip:
    # table of contents for the archive are getting displayed
    myzip.printdir()
    print("-----------------------------")
    # extracting all the files to the directory specified
    print('Extracting all the files started...')
    myzip.extractall("E:\\python_progs\\zip\\")
    print('Done!')
