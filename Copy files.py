# copyfile() = copies contents of a file
# copy() copyfile() + premission mode + destination can be a directory
# copy2() copy() + copies metadate (file's creation and modification times)

import shutil

shutil.copyfile('test.txt',"C:\\Users\\itachi\\Downloads\\copy.txt") # src, destination
shutil.copy('test.txt',"C:\\Users\\itachi\\Downloads\\copy.txt") # src, destination
shutil.copy2('test.txt',"C:\\Users\\itachi\\Downloads\\copy.txt") # src, destination