Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> my=deque()
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    my=deque()
NameError: name 'deque' is not defined
>>> mystack=LifoQueue(maxsize=5)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    mystack=LifoQueue(maxsize=5)
NameError: name 'LifoQueue' is not defined
>>> from collections import deque:
...     
SyntaxError: invalid syntax
>>> from collections import deque
>>> my=deque()
>>> my.append('a')
>>> my.append('b')
>>> my.append('c')
>>> my
deque(['a', 'b', 'c'])
>>> my.pop()
'c'
>>> my
deque(['a', 'b'])
>>> from queue import LifoQueue
>>> mystack=LifoQueue(maxsize=5)
>>> print(mystack.qsize())
0
>>> mystack.put('x')
>>> mystack.put('y')
>>> mystack.put('z')
>>> print("stack is Full",mystack.full())
stack is Full False
>>> print("size of stack",mystack.qsize())
size of stack 3
>>> mystack.put('a')
>>> mystack.put('b')
>>> print("stack is Full",mystack.full())
stack is Full True
