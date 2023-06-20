import os
import shutil

path = "folder"

try:
    # os.remove(path) # CANT DELETE FOLDERS WITH THIS FUNCTION
    # os.rmdir(path)  # FOR DELETING EMPTY FOLDERS
    shutil.rmtree(path)  # FOR DELETING FOLDER WITH DOCUMENTS INSIDE
    print("deleted")
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("You dont have PERMISSION to delete that")
except OSError:
    print('The directory is not empty')
