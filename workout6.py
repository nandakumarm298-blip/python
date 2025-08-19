Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
list1=[10,20,30,5,2,15,36]
type(list1)
<class 'list'>
list1
[10, 20, 30, 5, 2, 15, 36]
list2=(20,25,30,40,50)
type(list2)
<class 'tuple'>
list3=[35,45,60,"Nandakumar",3.5]
list3=[0]

list3[0]
0
list3=[35,45,60,"Nandakumar",3.5]
list3[0]
35
list3[0:4]
[35, 45, 60, 'Nandakumar']
list3[-3:-1]
[60, 'Nandakumar']
list3[::2]
[35, 60, 3.5]
list4=[10,20,20,30,60,65,70,70]
print(list4)
[10, 20, 20, 30, 60, 65, 70, 70]
list4=[10,20,20,30,60,65,70,70]
list4[0]=200
list4
[200, 20, 20, 30, 60, 65, 70, 70]
tup1=(10,20,50,30,40,60)
print(type(tup1))
<class 'tuple'>
print(list(tup1))
[10, 20, 50, 30, 40, 60]
list3=[35,45,60,"Nandakumar",3.5]
if "nandakumar" in list3:
    print("Yes its found")
else:
    print("No its not found")

    
No its not found
list4
[200, 20, 20, 30, 60, 65, 70, 70]
list4.insert(2,'jeeva')
list4
[200, 20, 'jeeva', 20, 30, 60, 65, 70, 70]
list4=[10,20,20,30,60,65,70,70]
list4.append("a1")
list4
[10, 20, 20, 30, 60, 65, 70, 70, 'a1']
list2
(20, 25, 30, 40, 50)
list2.extend(list4)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    list2.extend(list4)
AttributeError: 'tuple' object has no attribute 'extend'
list4=[10,20,20,30,60,65,70,70]
list4.extend(list3)
list4
[10, 20, 20, 30, 60, 65, 70, 70, 35, 45, 60, 'Nandakumar', 3.5]
list1=[10,20,30,5,2,15,36]
list1.remove(30)
list1
[10, 20, 5, 2, 15, 36]
list4=[10,20,20,30,60,65,70,70]
list4.pop(60)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    list4.pop(60)
IndexError: pop index out of range
list4=[10,20,20,30,60,65,70,70]
list4.pop(4)
60
list4
[10, 20, 20, 30, 65, 70, 70]
list4=[10,20,20,30,60,65,70,70]
list4.pop()
70
list4
[10, 20, 20, 30, 60, 65, 70]
list3=[35,45,60,"Nandakumar",3.5]
list3.del(1)
SyntaxError: invalid syntax
list3=[35,45,60,"Nandakumar",3.5]
del list3[2]

list3
[35, 45, 'Nandakumar', 3.5]
list4=[10,20,20,30,60,65,70,70]
list4.clear()
list4
[]
list3=[35,45,60,"Nandakumar",3.5]
for x in list3:
    print(x)

    
35
45
60
Nandakumar
3.5
>>> list3=[35,45,60,"Nandakumar",3.5]
>>> for i in range (len(list3)):
...     print(i)
... 
...     
0
1
2
3
4
>>> list3=[35,45,60,"Nandakumar",3.5]
>>> i=0
>>> while(i<len(list3)):
...     print(list3[i])
...     i=i+1
... 
...     
35
45
60
Nandakumar
3.5
>>> list4=[10,20,20,30,60,65,70,70]
>>> i=0
>>> while(i<len(list4)):
...     print(list4[i])
...     i=i+1
... 
...     
10
20
20
30
60
65
70
70
>>> list4=[10,20,20,30,60,65,70,70]
>>> list4.reverse()
>>> list4
[70, 70, 65, 60, 30, 20, 20, 10]
>>> my1=list4.copy()
>>> my1
[70, 70, 65, 60, 30, 20, 20, 10]
>>> my1+list3
[70, 70, 65, 60, 30, 20, 20, 10, 35, 45, 60, 'Nandakumar', 3.5]
