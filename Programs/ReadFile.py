# Program to read file contents

import os
cd=os.getcwd()  # current directory
print(cd)
pd = os.path.dirname(cd) # parent directory
print(pd)
file_path = pd+"/"+"Programs"+"/"+"Files"+"/"+"Read.txt"
print(file_path)

try:
    f=open(file_path)  # by default file will open in read mode
    print(f.name)
    print("File open?",f.closed)
    file_data = f.read()
    print(file_data)
except Exception as e:
    print("Exception occurred",e)
finally:
    f.close()

print("File closed?",f.closed)