# assert - used to check/compare result

import math

assert "Vishwa" in["Vishwa","Raja","Rani","Kumar"],"Value not found"
print("Value found")


assert "Python" in "Welcome to Python", "Python not found"
print("Python found")

try:
    assert math.sqrt(64) == 8, "Incorrect result"
    print("Correct result")
except Exception as e:
    print("Exception", e)