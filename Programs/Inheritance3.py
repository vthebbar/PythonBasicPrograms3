# Multilevel Inheritance

class A:

    def display(self):
        print("Class A - Display")

    def methodA(self):
        print("Class A -Method A")

class B(A):
    def display(self):
        print("Class B- Display")
        super().display() # It will call parent class A - display method

    def methodB(self):
        print("Class B - Method B")

class C(B):
    def display(self):
        print("Class C - Display")
        super().display()  # it will call parent class B method
    def methodC(self):
        print("Class C - Method C")
        super().methodA() # calling parent class method - option 1 using super()
        B.methodB(self) # calling parent class method - option 2 using class name


# MRO
print(C.mro()) # Method Resolution Order

objc = C()
objc.display()
objc.methodC()
#objc.methodB()
#objc.methodA()