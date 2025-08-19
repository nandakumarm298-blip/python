Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
============ RESTART: C:/Users/User/OneDrive/Desktop/Elif ladder2.py ===========
Enter the m1 value is ::200
Enter the m2 value is ::150
Enter the m3 value is ::200
Grade-C
>>> 
================================================================ RESTART: C:/Users/User/OneDrive/Desktop/Elif ladder2.py ===============================================================
Enter the m1 value is ::250
Enter the m2 value is ::300
Enter the m3 value is ::350
Grade-A
>>> 
================================================================ RESTART: C:/Users/User/OneDrive/Desktop/Elif ladder2.py ===============================================================
Enter the m1 value is ::100
Enter the m2 value is ::200
Enter the m3 value is ::100
Fail
>>> 
================================================================ RESTART: C:/Users/User/OneDrive/Desktop/Elif ladder2.py ===============================================================
Enter the m1 value is ::250
Enter the m2 value is ::300
Enter the m3 value is ::150
Grade-B
>>> 
================================================================ RESTART: C:/Users/User/OneDrive/Desktop/Elif ladder2.py ===============================================================
Enter the m1 value is ::250
Enter the m2 value is ::300
Enter the m3 value is ::100
Fail
>>> 
================================================================ RESTART: C:/Users/User/OneDrive/Desktop/Elif ladder2.py ===============================================================
Enter the m1 value is ::300
Enter the m2 value is ::250
Enter the m3 value is ::300
Fail
>>> 
================================================================ RESTART: C:/Users/User/OneDrive/Desktop/Elif ladder2.py ===============================================================
Enter the m1 value is ::400
Enter the m2 value is ::300
Enter the m3 value is ::400
Fail
>>> 
================================================================ RESTART: C:/Users/User/OneDrive/Desktop/Elif ladder2.py ===============================================================
Enter the m1 value is ::300
Enter the m2 value is ::400
Enter the m3 value is ::200
Grade-A

============================================================= RESTART: C:/Users/User/OneDrive/Desktop/Looping statement.py =============================================================
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
    print("I value is ::"i)
    
SyntaxError: invalid syntax. Perhaps you forgot a comma?
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
    if(i%2==0):
        print("Even number::")
        a=i+(i+1)
    else:
        print("Odd number::")
        b=i*(i+1)
    print("sum of even:",a)
    print("Product of odd:",b)

    
Even number::
sum of even: 1
Traceback (most recent call last):
  File "<pyshell#25>", line 9, in <module>
    print("Product of odd:",b)
NameError: name 'b' is not defined
for i in range (0,10,1):
    if(i%2==0):
        print("Even number::")
        a=i+(i+1)
    else:
        print("Odd number::")
        b=i*(i+1)
print("sum of even:",a)
print("Product of odd:",b)
SyntaxError: invalid syntax

j=int(input("Enter the number::"))
Enter the number::5
for i in range(0,j+1,1):
    if(i%2==0):
        print("Even number")
        a=i+(i+1)
    else:
        print("Odd number")
        b=i*(i+1)
print("sum of even:",a)
print("Product of odd:",b)
SyntaxError: invalid syntax
j=int(input("Enter the number::"))
Enter the number::6
for i in range(0,j+1,1):
    if(i%2==0):
        print("Even number",i)
        a=i+(i+1)
    else:
        print("Odd number",i)
        b=i*(i+1)
print("sum of even:",a)
print("Product of odd:",b)
SyntaxError: invalid syntax
j=int(input("Enter the number::"))
Enter the number::5
for i in range(0,j+1,1):
    if(i%2==0):
        print("Even number",i)
        a=i+(i+1)
    else:
        print("Odd number",i)
        b=i*(i+1);
print("sum of even:",a)
print("Product of odd:",b)
SyntaxError: invalid syntax
j=int(input("Enter the number::"))
Enter the number::8
for i in range(0,j+1,1):
    if(i%2==0):
        print("Even number",i)
        a=i+(i+1)
    else:
        print("Odd number",i)
        b=i*(i+1);
    print ("sum of even:",a)
    print ("Product of odd:",b)

    
Even number 0
sum of even: 1
Traceback (most recent call last):
  File "<pyshell#42>", line 9, in <module>
    print ("Product of odd:",b)
NameError: name 'b' is not defined
j=int(input("Enter the number::"))
Enter the number::9
for i in range(0,j+1,1):
    if(i%2==0):
        print("Even number",i)
        a=i+(i+1)
    else:
        print("Odd number",i)
        b=i*(i+1)
    print ("sum of even:",a)
    print ("Product of odd:",b)

    
Even number 0
sum of even: 1
Traceback (most recent call last):
  File "<pyshell#45>", line 9, in <module>
    print ("Product of odd:",b)
NameError: name 'b' is not defined
a=1
b=0

============================================================= RESTART: C:/Users/User/OneDrive/Desktop/Looping statement.py =============================================================
odd number is :: 0
odd number is :: 1
odd number is :: 2
odd number is :: 3
odd number is :: 4
odd number is :: 5
odd number is :: 6
odd number is :: 7
odd number is :: 8
odd number is :: 9

============================================================= RESTART: C:/Users/User/OneDrive/Desktop/Looping statement.py =============================================================
odd number is :: 0
odd number is :: 2
odd number is :: 4
odd number is :: 6
odd number is :: 8

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
    for j in range (0,m,1):
        print("*",end="")
    print()

    
*****
*****
*****
*****
*****



n=5
m=5
for i in range (0,n,1):
    for j in range (0,m,1):
        print("*")
    print()
    
SyntaxError: multiple statements found while compiling a single statement
n=5
m=5
for i in range (0,n,1):
    for j in range (0,m,1):
        print("*")
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

for i in range (0,n,1):
    for j in range (0,m,1):
        print("*",end="")
    print()

    
*****
*****
*****
*****
*****

for i in range (0,n,1):
    for j in range (0,m,1):
        print(j,end="")
    print()

    
01234
01234
01234
01234
01234

for i in range (0,n,1):
    for j in range (0,m,1):
        print(i,end="")
    print()

    
00000
11111
22222
33333
44444

for i in range (n,0,1):
    for j in range (m,0,1):
        print (i,end="")
    print()

    
for i in range (n,0,1):
    for j in range (m,0,1):
        print(i,end="")
    print()

    
for i in range (n,0,1):
    for j in range (m,0,1):
        print(j,end="")
    print()

    
n=5
m=5
for i in range (n,0,1):
    for j in range (m,0,1):
        print(j,end="")
    print()

    
for i in range (0,n,1):
    for j in range (0,m,1):
        print(j,end="")
    print()

    
01234
01234
01234
01234
01234

============================================ RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/Looping statement excersice 3.py ===========================================

============================================ RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/Looping statement excersice 3.py ===========================================
1
1
