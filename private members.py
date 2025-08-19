class Base:
    def __init__(self):
        self.a="welcome of a"
        self._c="welcome of c"
#creating a derived class
class Derived(Base):
    def __init__(self):
        #calling contructor of Base class
        Base.__init__(self)
        print("calling private member of base class:")
        print(self._c)
#Derived code
obj1=Base()
print(obj1.a)
