# Read file using context manager (with)

import os

cd = os.getcwd() # current directory
pd = os.path.dirname(cd) # parent directory

file_path = pd+"/"+"Programs"+"/"+"Files"+"/"+"Read.txt"

try:
    with open(file_path) as f:
        print("File Closed?", f.closed)
        print("File name:",f.name)
        print(f.read())
except Exception as e:
    print("Exception", e)

print("File Closed?", f.closed)

