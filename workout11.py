Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> str="hello"
>>> str1="world"
>>> print(str*3)
hellohellohello
>>> print(str+str1)
helloworld
>>> print(str[2:4])
ll
>>> print('w' in str)
False
>>> a=10
>>> id(a)
140736288531656
>>> 12 and 11
11
>>> 12 and 0
0
>>> 0
0
>>> 12 and 0 and 1
0
>>> 12 or 0
12
>>> 0 or 0 or 12
12
>>> 0 or 0
0
>>> print('w' in str1)
True
>>> print('wo' in str1)
True
>>> print('wo' not in str1)
False
>>> print("The string is::%s"%(str))
The string is::hello
>>> print("{1} and {0} best players".format("azar","mohamed"))
mohamed and azar best players
>>> print("{a},{b},{c}".format(a="nandakumar",b="jeeva",c="12"))
nandakumar,jeeva,123
