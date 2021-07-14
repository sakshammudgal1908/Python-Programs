#write a program to rename a file
#first we are copying the contents of the file into another file, then we will delete the old file.Hence this is a way of renaming a file
#importing the os moduleand using os.remove("filename.tex") will remove/delete the file which name has been specified in the ()
import os
oldname="Samplefile.txt"
newname="Renamed-file.txt"

with open (oldname) as f:
    contents=f.read()

with open (newname,'w') as f:
    f.write(contents)

os.remove(oldname)
