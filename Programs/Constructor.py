# constructors

class A(object):
    def __init__(self):
        print("Class A constructor")


class B(A):
    def __init__(self):
        print("Class B constructor")
        A.__init__(self)  # calling class A constructor inside class B - method1
        super().__init__() # calling class A constructor inside class B - method2


obj1 = A()  # Class A constructor will be called
obj2 = B()  # Class B constructor will be called



