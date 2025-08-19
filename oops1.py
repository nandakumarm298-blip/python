class sample:
    def fun1(s):
        print("This is fun1")
f1=sample()
f1.fun1()

class sample:
    def fun1(self):
        print("This is fun1")
    def fun2(self):
        print("This is fun2")
f1=sample()
f1.fun1()
f1.fun2()

class B:
    def fun1(self):
        self.name=input("Enter the name is ::")
        print("This is base class",self.name)
class D(B):
    def fun2(self):
        print("This is derived class",self.name)
f1=D()
f1.fun1()
f2.fun2()

class Animal:
    def eat(self):
        self.age=int(input("Enter the age is ::"))
        print("Animal is eating")
class Bird:
    def fly(self):
        print("Bird is flying")
class Eagle(Animal,Bird):
    def hunt(self):
        print("Eagle is hunting",self.age)
e1=Eagle()
e1=eat()
e1.fly()
e1.hunt()
