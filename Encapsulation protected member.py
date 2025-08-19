class Base:
    def __init__ (self):
        #protected member
        self._a=2;
class Derived(Base):
    def __init__ (self):
        #Calling constructor of Base class
        Base.__init__(self)
        print("Calling protected member of base class:",self._a)
        #Modify the protected variable
        self._a=3
        print("Calling modified protected member outside class:",self._a)
obj1=Derived()
obj2=Base()
#Calling protected member
print("Accessing protected member of obj1:",obj1._a)
#Accessing the protected variable outside
print("Accessing protected member of obj2:",obj2._a)
            
        
