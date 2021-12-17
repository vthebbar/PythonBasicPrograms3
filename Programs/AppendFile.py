# Program to append content to file

import os

cd = os.getcwd() # current directory
print("Current dir:",cd)
pd=os.path.dirname(cd) # parent directory
print("Parent dir:",pd)

file_path = pd+"/"+"Programs"+"/"+"Files"+"/"+"Write.txt"

try:
    with open(file_path,"r") as f:  # open file in append mode
        print("File closed?", f.closed)
        f.write("\nAppend line1")
        f.write("\nAppend lin2")
except Exception as e:
    print("Exception", e)
finally:
    print("Finally block")
    print("File closed?", f.closed)  # file automatically closed once control is out of with block
