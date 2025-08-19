Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> str1="welcome"
>>> print(str1)
welcome
>>> name="hello"
>>> print(name[0:3])
hel
>>> print(name[2::])
llo
>>> print(name[-3:-1])
ll
>>> print(name[0:2])
he
>>> 
>>> print(name[:3])
hel
>>> print(name[:])
hello
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
>>> print('w' in str1 )
True
>>> print('wo' not in str1)
False
>>> print('wo' in str1)
True
>>> print("This string is::%s"%(str))
This string is::hello
>>> print("{1} and {0} best players".format("azar","mohamed"))
mohamed and azar best players
>>> print("{a},{b},{c}".format(a="azar",b="mohamed",c="AS"))
azar,mohamed,AS
>>> Integer=10
>>> Float  =1.2
>>> string ="azar"
>>> print("Hi i am Integer..My value is::%d\n Hi I am float..My value is%f\n Hi I am string.. My value is%s")
Hi i am Integer..My value is::%d
 Hi I am float..My value is%f
 Hi I am string.. My value is%s
str1="welcome"
print(str1.capitalize())
Welcome
print(str1.casefold())
welcome
str2="WELCOME"
print(str2.casefold())
welcome
str3="NANDAKUMAR"
print(str3.casefold())
nandakumar
str3="NANDAKUMAR"
str3="nandakumar"
print(str3.casefold())
nandakumar
str4="Hello Welcome"
res=str3.center(20)
print("old value::",str3)
old value:: nandakumar
str4="Hello Welcome"
res=str4.center(20)
print("old value::",str4)
old value:: Hello Welcome
print("new value::",res)
new value::    Hello Welcome    
str1="nandakumar"
print(str1.count('a'))
3
print(str1.count('j'))
0
print(str3.startswith('N'))
False
print(str2.startswith('W'))
True
print(str4.startswith('H'))
True
print(str4.endswith('E'))
False
print(str4.endswith('e'))
True
print(str3.isalnum())
True
str3="nandakumar"
print(str3.isalnum())
True

======= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/qwerty.py =======
False

======= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/qwerty.py =======
Traceback (most recent call last):
  File "C:/Users/User/AppData/Local/Programs/Python/Python313/qwerty.py", line 4, in <module>
    print(string2.isalnum())
AttributeError: 'int' object has no attribute 'isalnum'

======= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/qwerty.py =======
True

======= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/qwerty.py =======
False

===== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\nesed loop2.py ====
*
**
***
****
*****

==== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\nested loop5.py ====
01234
01234
01234
01234
01234
43210
43210
43210
43210
43210
1
12
123
1234
12345

=== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\Nested looping.py ===
00000
11111
22222
33333
44444
*****
*****
*****
*****
*****
01234
01234
01234
01234
01234

===== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\nesed loop2.py ====
*
**
***
****
*****
1
22
333
4444
55555

===== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\nesed loop2.py ====
*
**
***
****
*****
1
22
333
4444
55555
1
12
123
1234
12345

==== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\nested loop5.py ====
01234
01234
01234
01234
01234
43210
43210
43210
43210
43210
00000
11111
22222
33333
44444

==== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\nested loop3.py ====
*****
****
***
**
*

==== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\nested loop3.py ====
*****
****
***
**
*
*****
****
***
**
*
**********
********
******
****
**

==== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\nested loop3.py ====
*****
****
***
**
*
*****
****
***
**
*
******************************

==== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\nested loop3.py ====
*****
****
***
**
*
*****
****
***
**
*
**********
********
******
****
**

==== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\nested loop3.py ====
*****
****
***
**
*
*****
****
***
**
*
*****
****
***
**
*

==== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\nested loop3.py ====
*****
****
***
**
*
*****
****
***
**
*
*****
****
***
**
*
*****
****
***
**
*

==== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\nested loop5.py ====
01234
01234
01234
01234
01234
43210
43210
43210
43210
43210
00000
11111
22222
33333
44444

=== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\Nested looping.py ===
00000
11111
22222
33333
44444
*****
*****
*****
*****
*****
01234
01234
01234
01234
01234

=== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\Nested looping.py ===
00000
11111
22222
33333
44444
*****
*****
*****
*****
*****
01234
01234
01234
01234
01234
43210
43210
43210
43210
43210
