# Method overriding is an example for Polymorphism

# Parent class and child class contain same method name and signature

class Parent:

    def display(self):
        print("Parent class display method")


class Child(Parent):
    def display(self):
        print("Child class display method")



p=Parent()
c=Child()

p.display()
c.display()

