Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
==== No Subprocess ====

WARNING: Running IDLE without a Subprocess is deprecated
and will be removed in a later version. See Help/IDLE Help
for details.

>>> amount=1000;
>>> if(amount>1000)
SyntaxError: expected ':'
>>> if(amount==1000):
...     print("your amount is::",amount)
... 
...     
your amount is:: 1000
>>> marks=100
>>> a=marks/0
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a=marks/0
      ~~~~~^~
ZeroDivisionError: division by zero
>>> a=marks/2
>>> print(a)
50.0
>>> x=5
>>> y="welcome"
>>> z=x+y
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    z=x+y
      ~^~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> x=5
>>> y="hello"
>>> try:
...     z=x+y
... except TypeError:
...     print("Enter:cannot add an int and a str")
... 
...     
Enter:cannot add an int and a str
>>> a=[1,2,3]
>>> trt:
...     
SyntaxError: invalid syntax
a=[1,2,3]
try:
    print("second element=%d"%(a[1]))
    print("fourth element=%d"%(a[3]))
except:
    print("An error occurred")

    
second element=2
An error occurred
def fun(a):
    if a<4:
        b=a/(a-3)
        print("value of b=",b)
try:
    
SyntaxError: invalid syntax
def fun(a):
    if a<4:
        b=a/(a-3)
        print("value of b=",b)
try:
    
SyntaxError: invalid syntax
