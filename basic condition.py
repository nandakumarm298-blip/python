Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
==== No Subprocess ====

WARNING: Running IDLE without a Subprocess is deprecated
and will be removed in a later version. See Help/IDLE Help
for details.

>>> a=10
>>> b=20
>>> c=a*B
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    c=a*B
        ^
NameError: name 'B' is not defined. Did you mean: 'b'?
>>> print(a*b)
200
>>> print((a*b))
200
>>> print(c)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(c)
          ^
NameError: name 'c' is not defined
>>> print(c=a*b)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(c=a*b)
    ~~~~~^^^^^^^
TypeError: print() got an unexpected keyword argument 'c'
