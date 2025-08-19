Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
==== No Subprocess ====

WARNING: Running IDLE without a Subprocess is deprecated
and will be removed in a later version. See Help/IDLE Help
for details.

>>> studname=set(["nandakumar","jeeva","maheswari","mohan"])
>>> print(studname)
{'nandakumar', 'jeeva', 'mohan', 'maheswari'}
>>> studname.add("nandakumar1")
>>> studname.add("nandakumar2")
>>> studname
{'nandakumar', 'maheswari', 'nandakumar1', 'jeeva', 'mohan', 'nandakumar2'}
>>> for i in studname:
...     print(i)
... 
...     
nandakumar
maheswari
nandakumar1
jeeva
mohan
nandakumar2
>>> studname.update(["a1","b1","c1"])
>>> studname
{'nandakumar', 'maheswari', 'nandakumar1', 'jeeva', 'mohan', 'a1', 'nandakumar2', 'c1', 'b1'}
>>> studname.discard("a1")
>>> studname
{'nandakumar', 'maheswari', 'nandakumar1', 'jeeva', 'mohan', 'nandakumar2', 'c1', 'b1'}
>>> studname.remove("nandakumar1")
>>> studname
{'nandakumar', 'maheswari', 'jeeva', 'mohan', 'nandakumar2', 'c1', 'b1'}
>>> studname.pop()
'nandakumar'
>>> studname.clear()
>>> studname
set()
