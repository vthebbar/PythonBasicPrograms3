# Single Inheritance

class Parent:
    def parentMethod(self):
        print("Parent method")

    def display(self):
        print("Parent display")

class Child(Parent):
    def childMethod(self):
        print("Child method")

    def display(self):                # method overriding
        print("Child display")


p=Parent()
c=Child()

p.parentMethod()
p.display()

c.childMethod()
c.display()
