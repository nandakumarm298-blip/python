def myfunc(n):
    return lambda a:a*n

my1=myfunc(2)
print(my1(11))

my2=myfunc(3)
print(my1(12))

