Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> empname={"mohamed","Azar","Azar","sheik"}
>>> print(empname)
{'sheik', 'mohamed', 'Azar'}
>>> print(type(empname))
<class 'set'>
>>> empname
{'sheik', 'mohamed', 'Azar'}
>>> for i in empname:
...     print(i)
... 
...     
sheik
mohamed
Azar
>>> set1={}
>>> print(set1)
{}
>>> set2=set()
>>> print(set2)
set()
>>> print(type(set1))
<class 'dict'>
>>> print(type(set2))
<class 'set'>
>>> studname=set(["azar","mohamed","mohamed1","azar1"])
>>> print(studname)
{'mohamed1', 'azar', 'azar1', 'mohamed'}
>>> studname.add("azar2")
>>> studname.add("azar3")
>>> studname
{'mohamed1', 'azar1', 'azar2', 'azar', 'azar3', 'mohamed'}
>>> studname.update(["a1","b1","c1"])
>>> studname
{'mohamed1', 'c1', 'azar1', 'azar2', 'b1', 'a1', 'azar', 'azar3', 'mohamed'}
>>> studname.discard("c1")
>>> studname
{'mohamed1', 'azar1', 'azar2', 'b1', 'a1', 'azar', 'azar3', 'mohamed'}
>>> studname.remove("azar1")
>>> studname
{'mohamed1', 'azar2', 'b1', 'a1', 'azar', 'azar3', 'mohamed'}
>>> studname.pop()
'mohamed1'
>>> studname
{'azar2', 'b1', 'a1', 'azar', 'azar3', 'mohamed'}
>>> studname.clear()
studname
set()
s1={"a1","b1","c1"}
s2={"a2","b2","c2"}
print(s1|s2)
{'b1', 'a1', 'c2', 'c1', 'b2', 'a2'}
print(s1.union(s2))
{'b1', 'a1', 'c2', 'c1', 'b2', 'a2'}
s1={'a1',}
s1={'a1','c1','b1'}
s2={'c2','b2','a2'}
print(s1&s2)
set()
s3={"a2","b2","c3"}
print(s2&s3)
{'a2', 'b2'}
print(s2.intersection(s3))
{'a2', 'b2'}
