Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=2
>>> b=3
>>> print(a&b)
2
>>> a=2
>>> b=4
>>> print(a|b)
6
>>> a=5
>>> b=6
>>> print(a^b)
3
>>> a=4
>>> print(~a)
-5
>>> a=4
>>> print(a<<1)
8
>>> a=6
>>> print(a>>1)
3
>>> a=10
>>> if(a==10):
...     print("A is Equal")
... 
...     
A is Equal
>>> a=20
>>> if(a==10):
...     print("A is Equal")
... else:
...     print("A is not Equal")
... 
...     
A is not Equal
>>> a=27
... if(a==10):
...     print("A is Equal")
... else:
...     print("A is not Equal")
...     
SyntaxError: multiple statements found while compiling a single statement
>>> a=27
>>> if(a==10):
...     print("A is Equal")
else:
    print("A is not Equal")

    
A is not Equal

a=int(input("Enter the number"))
Enter the number56
if(a%2==0):
    print("It is a Even number")
else:
    print("It is not odd number")

    
It is a Even number

age=int(input("Enter the age is ::"))
Enter the age is ::67
if(age>=61):
    salary=int(input("Enter the salary is ::"))
    if(salary>=20000):
        bns=salary+500;
        print("Your salary is ::",bns)
    else:
        bns=salary+1000;
        print("Your salary is ::",bns)
else:
    print("Your age is invalid")

    
Enter the salary is ::30000
Your salary is :: 30500
age=int(input("Enter the age is ::"))
Enter the age is ::54
if(age>=61):
    salary=int(input("Enter the salary is ::"))
    if(salary>=20000):
        bns=salary+500;
        print("Your salary is ::",bns)
    else:
        bns=salary+1000;
        print("Your salary is ::",bns)
else:
    print("Your age is invalid")

    
Your age is invalid

m1=int(input("Enter the m1 value is ::"))
Enter the m1 value is ::500
m2=int(input("Enter the m2 value is ::"))
Enter the m2 value is ::200
m3=int(input("Enter the m3 value is ::"))
Enter the m3 value is ::150
tot=m1+m2+m3
if(tot>=900):
    print("Grade-A")
elif(tot>=700):
    print("Grade-B")
elif(tot>=500):
    print("Grade-C")
else:
    print("Fail")

    
Grade-B
m1=int(input("Enter the m1 value is ::"))
Enter the m1 value is ::250
m2=int(input("Enter the m2 value is ::"))
Enter the m2 value is ::300
m3=int(input("Enter the m3 value is ::"))
Enter the m3 value is ::100
tot=m1+m2+m3
if(tot>=900):
    print("Grade-A")
elif(tot>=700):
    print("Grade-B")
elif(tot>=500):
    print("Grade-C")
else:
    print("Fail")

    
Grade-C
m1=int(input("Enter the m1 value is ::"))
Enter the m1 value is ::150
m2=int(input("Enter the m2 value is ::"))
Enter the m2 value is ::200
m3=int(input("Enter the m3 value is ::"))
Enter the m3 value is ::600
tot=m1+m2+m3
if(tot>=900):
    print("Grade-A")
elif(tot>=700):
    print("Grade-B")
elif(tot>=500):
    print("Grade-C")
else:
    print("Fail")

    
Grade-A

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
for i in range (0,2,1):
    for j in range (0,2,1):
        print("I value is ::",i,"J value is ::",j)

        
I value is :: 0 J value is :: 0
I value is :: 0 J value is :: 1
I value is :: 1 J value is :: 0
I value is :: 1 J value is :: 1
n=5
m=5
for i in range (0,n,1):
    for i in range (0,m,1):
        print("*",end="")
      print()
      
SyntaxError: unindent does not match any outer indentation level
n=5
m=5
for i in range (0,n,1):
    for i in range (0,m,1):
        print("*",end="")
        print()
        
SyntaxError: multiple statements found while compiling a single statement
n=5
m=5
for i in range (0,n,1):
    for i in range (0,m,1):
        print("*",end="")
        print()

        
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
n=5
m=5
for i in range (0,n,1):
    for i in range (0,m,1):
        print("i",end="")
        print()

        
i
i
i
i
i
i
i
i
i
i
i
i
i
i
i
i
i
i
i
i
i
i
i
i
i
n=5
m=5
for i in range (0,n,1):
    for i in range (0,m,1):
        print("n",end="")
        print()

        
n
n
n
n
n
n
n
n
n
n
n
n
n
n
n
n
n
n
n
n
n
n
n
n
n
