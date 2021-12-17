# Write to a file

import os
cd= os.getcwd() # current directory
print("Current dir:", cd)
pd = os.path.dirname(cd) # parent directory
print("Parent dir:", pd)

file_path = pd+"/"+"Programs"+"/"+"Files"+"/"+"Write.txt"

try:
    f = open(file_path,"w") # open in write mode
    print("File closed?", f.closed)
    print("File name", f.name)
    f.write("content line1")
    f.write("\ncontent line2 ")
except Exception as e:
    print("exception",e)

finally:
    f.close()
    print("File closed?",f.closed)