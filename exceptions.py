def fun(a):
    if a<4:
        b=a/(a-3)
    print("value of b=",b)
        
try:
    #fun(3)
    fun(5)
except ZeroDivisionError:
    print("zero Division Error")
except NameError:
    print("Name Error Occured and Handled")
    


def fun(a):
    if a<4:
        b=a/(a-3)
    print("value of b=",b)
        
try:
    fun(3)
    #fun(5)
except ZeroDivisionError:
    print("zero Division Error")
except NameError:
    print("Name Error Occured and Handled")
    


