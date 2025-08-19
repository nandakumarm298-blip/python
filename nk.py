Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=2
b=3
print(a&b)
2
a=2
b=3
print(a|b)
3
a=2
b=3
print(a^b)
1
a=50
print(~a)
-51
a=4
print(a>>1)
2
a=2
print(a<<1)
4
a=10
if(a==10):
    print("A is Equal")

    
A is Equal
a=20
if(a==10):
    print("A is Equal")

    
else:
    
SyntaxError: invalid syntax
a=20
if(a==10:)
SyntaxError: invalid syntax
a=20
if(a==10):
    print("A is Equal")
else:
    print("A is not Equal")

    
A is not Equal
a=10
if(a%2==0):
    print("A is odd")
else:
    print("A is Even")

    
A is odd
a=30
if(a%2==0):
    print("A is odd")
else:
    print("A is Even")

    
A is odd
a=24
if(a%3==0):
    print("A is odd")
else:
    print("A is Even")

    
A is odd
a=73
if(a%2==0):
    print("A is odd")
else:
    print("A is Even")

    
A is Even
a=int(input("Enter the number"))
Enter the number97
if(a%2==0):
    print("It is a Even number")
else:
    print("It is a not odd number")

    
It is a not odd number
age=int(input("Enter the age is ::"))
Enter the age is ::67
if(age>=61):
    salary=int(input("Enter the salary is ::"))
    if(salary>=20000):
        bns=salary+500;
        print("Your salary is ::",bns)
    else:
        bns=salary+1000;
        print("Your salary is::",bns)
else:
    print("Your age is invalid")

    
Enter the salary is ::30000
Your salary is :: 30500
age=int(input("Enter the age is ::"))
Enter the age is ::50

if(age>=61):
    salary=int(input("Enter the salary is ::"))
    if(salary>=20000):
        bns=salary+500;
        print("Your salary is ::",bns)
    else:
        bns=salary+1000;
        print("Your salary is::",bns)
else:
    print("Your age is invalid")

    
Your age is invalid
age=int(input("Enter the age is ::"))
Enter the age is ::63
if(age>=61):
    salary=int(input("Enter the salary is ::"))
    if(salary>=20000):
        bns=salary+500;
        print("Your salary is ::",bns)
    else:
        bns=salary+1000;
        print("Your salary is::",bns)
else:
    print("Your age is invalid")

    
Enter the salary is ::18000
Your salary is:: 19000

===================================================== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\Elif ladder.py ====================================================
Enter the m1 value is ::300
Enter the m2 value is ::400
Enter the m3 value is ::250
Grade-A

===================================================== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\Elif ladder.py ====================================================
Enter the m1 value is ::250
Enter the m2 value is ::300
Enter the m3 value is ::100
Grade-C

===================================================== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\Elif ladder.py ====================================================
Enter the m1 value is ::300
Enter the m2 value is ::200
Enter the m3 value is ::350
Grade-B
for i in range (0,10,1):
    print("I value is ::",i)

    
I value is :: 0
I value is :: 1
I value is :: 2
I value is :: 3
I value is :: 4
I value is :: 5
I value is :: 6
I value is :: 7
I value is :: 8
I value is :: 9
for i in range (10,20,2):
    print("I value is ::",i)

    
I value is :: 10
I value is :: 12
I value is :: 14
I value is :: 16
I value is :: 18
for i in range (0,10,1):
    if(i%2==0):
        print("Even is ::",i)
    else:
        print("odd is ::",i)

        
Even is :: 0
odd is :: 1
Even is :: 2
odd is :: 3
Even is :: 4
odd is :: 5
Even is :: 6
odd is :: 7
Even is :: 8
odd is :: 9
for i in range (0,10,1):
...     if(i%2==0):
...         sum(i+1)
...         print("sum of number is ::",sum)
...     else:
...         print("multiple of number is ::",sum)
... 
...         
Traceback (most recent call last):
  File "<pyshell#99>", line 3, in <module>
    sum(i+1)
TypeError: 'int' object is not iterable
>>> for i in range (0,10,1):
...     if(i%2==0):
...         sum(i+1)
...         print(int(input("sum of number is ::",sum))
...     else:
...         print(int(input("multiple of number is ::",sum))
...               
SyntaxError: invalid syntax
>>> for i in range (0,2,1):
...               for i in range (0,2,1):
...               print("I value is ::",i,"J value is ::",j)
...               
SyntaxError: expected an indented block after 'for' statement on line 2
>>> 
>>> for i in range(0,2,1):
...       for i in range(0,2,1):
...           print("I value is ::",i,"J value is ::",j)
... 
...               
Traceback (most recent call last):
  File "<pyshell#108>", line 3, in <module>
    print("I value is ::",i,"J value is ::",j)
NameError: name 'j' is not defined
>>> for i in range(0,2,1):
...               for i in range(0,2,1):
...                       print("I value is ::",i,"J value is ::",j)
... 
...               
Traceback (most recent call last):
  File "<pyshell#110>", line 3, in <module>
    print("I value is ::",i,"J value is ::",j)
NameError: name 'j' is not defined
>>> 
>>> i=0
...               
