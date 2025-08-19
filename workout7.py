Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
tup1=(10,20,30,40,50)
print(tup1)
(10, 20, 30, 40, 50)
print(type(tup1))
<class 'tuple'>
tup2=(10,"nandakumar",2.6)
print(tup2)
(10, 'nandakumar', 2.6)
print(type(tup2))
<class 'tuple'>
tup1
(10, 20, 30, 40, 50)
tup1[0]=100
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tup1[0]=100
TypeError: 'tuple' object does not support item assignment
tup1
(10, 20, 30, 40, 50)
print(tup1)
(10, 20, 30, 40, 50)
print(len(tup1))
5
tup3=("Nandakumar")
type(tup3)
<class 'str'>
tup3=("Nandakumar")
tup3
'Nandakumar'
type(tup3)
<class 'str'>
tup3='Nandakumar'
type(tup3)
<class 'str'>
tup3=('Nandakumar')
type(tup3)
<class 'str'>
tup4=('Nandakumar')
type(tup4)
<class 'str'>
tup4=('Nandakumar',)
type(tup4)
<class 'tuple'>
list1=[10,20,30,40,50,60]
type(list1)
<class 'list'>
k=tuple(list1)
k
(10, 20, 30, 40, 50, 60)
tup1[0:1]
(10,)
tup1[0:3]
(10, 20, 30)
tup1[-4:-1]
(20, 30, 40)
if 10 in tup1:
    print("Yes","found")

    
Yes found
list1=[10,20,30,40,55]
del list1
del .list1[0]
SyntaxError: invalid syntax
del list1[0]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    del list1[0]
NameError: name 'list1' is not defined. Did you mean: 'list'?
list1=[10,20,30,40,55]
del.list1[20]
SyntaxError: invalid syntax
list1=[10,20,30,40,55]
del.list1[2]
SyntaxError: invalid syntax
list1=[10,20,30,40,55]
del list1[2]
list1
[10, 20, 40, 55]
tup1=(10,20,30,40,50,60)
tup1=(a1,a2,a3,a4,a5,a6)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    tup1=(a1,a2,a3,a4,a5,a6)
NameError: name 'a1' is not defined
tup1=(10,20,30,40,50,60)
(a1,a2,a3,a4,a5,a6)=tup1
a1
10
a2
20
a
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a
NameError: name 'a' is not defined. Did you mean: 'a1'?
a3
30
a4
40
a5
50
a6
60
tup2=(10,20,)
3
tup2=(10,20,30,40,50)
(a1,a2,*a3)=tup2
a1
10
a2
20
>>> a3
[30, 40, 50]
>>> list1=["azar","mohamed","sheik"]
>>> for x in list1:
...     print(x)
... 
...     
azar
mohamed
sheik
>>> list1=["azar","mohamed","sheik"]
>>> i=0
>>> while i<len(list1):
...     print(list1[i])
...     i=i+1
... 
...     
azar
mohamed
sheik
>>> tup1=(10,20,30,40,50,60)
>>> tup2=('azar',)
>>> tup1=(10,20,30,40,50,60)
>>> tup2=('azar','nandakumar','jeeva')
>>> tup3=tup1+tup2
>>> 
>>> tup3
(10, 20, 30, 40, 50, 60, 'azar', 'nandakumar', 'jeeva')
>>> tup1=(10,20,30,40,50,60)
>>> tup1*2
(10, 20, 30, 40, 50, 60, 10, 20, 30, 40, 50, 60)
>>> tup5=(10,10,20,30,40,10)
>>> x=tup5.count(20)
>>> x
1
>>> tup5=(10,10,20,30,40,10)
>>> a=tup5.index(10)
>>> a
0
>>> a=tup5.index(20)
>>> a
2
>>> a=tup5.index(30)
>>> a
3
