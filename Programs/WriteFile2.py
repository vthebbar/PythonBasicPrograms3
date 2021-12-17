# write file using context manager

import os

cd=os.getcwd() # current directory
print("Current dir",cd)
pd = os.path.dirname(cd) # parent directory
print("Parent dir",pd)


file_path = pd+"/"+"Programs"+"/"+"Files"+"/"+"Write.txt"

try:
    with open(file_path,"w") as f: # open file in write mode
        print("File closed?", f.closed)
        f.write("\nContent line1")
        f.write("\nContent line2")

except Exception as e:
    print("exception",e)

finally:
    print("File closed", f.closed)
