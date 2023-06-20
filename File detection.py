import os

path = "C:\\Users\\itachi\\Desktop\\test folder"

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a dir")
else:
    print("That Location docent exists")
