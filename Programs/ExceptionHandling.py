# Exception handling - try, except, else, finally

try:
    a=int(input("Key in value 1:"))
    b=int(input("Key in value 2:"))
    res=a/b
    print("Result",res)

except ZeroDivisionError as e1:
    print(e1)
except ValueError as e2:
    print(e2)
except TypeError as e3:
    print(e3)
except Exception as e:
    print("Something went wrong",e)
else:
    print("Else part will execute if no exception occurred")

finally:
    print("Finally block will execute always")