from zipfile import ZipFile
import datetime

# file name is specified
myfile_name = "E:\\python_progs\\zip\\myfiles.zip"

# zip file getting opened in READ mode
with ZipFile(myfile_name, 'r') as myzip:
    for info in myzip.infolist():
        print(info.filename)
        print('\tModified Time:\t' + str(datetime.datetime(*info.date_time)))
        print('\tOperating System:\t\t' + str(info.create_system) + '(0 = Windows, 3 = Unix)')
        print('\tSpecifying ZIP version:\t' + str(info.create_version))
        print('\tBytes Compressed:\t' + str(info.compress_size) + ' bytes')
        print('\tBytes Uncompressed:\t' + str(info.file_size) + ' bytes')
