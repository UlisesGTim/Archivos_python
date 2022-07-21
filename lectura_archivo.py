import os

path_files = '/DWHSAP/sap_upload/respaldo/'

os.chdir(path_files)

def iterator(path_files):
    f = open(path_files, 'r')
    try:
        print(f.read())
    finally:
        #f.close()


for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".dat"):
        path_files = format((path_files)/(file))
        # call read text file function
        iterator(path_files)
    print("\n")


#iterator(path_files)
