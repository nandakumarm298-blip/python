Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
================================================== RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/function program.py ==================================================
This is func1
Enter the a value is ::150
Your value is :: 150
This is func2
>>> 
================================================== RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/function program1.py =================================================
This is func1
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
This is func2
>>> 
==================================================== RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/pass function.py ===================================================
Welcome
>>> 
==================================================== RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/pass function.py ===================================================
Welcome
Nandakumar
Jeeva
>>> 
================================================= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/function recursion.py =================================================
Recursion Example
k value :: 3
k value :: 2
k value :: 1
check 0
If 1
check 1
If 3
check 2
If 6
>>> 
>>> 

... 
>>> a=2
b=3
print(a&b)
2
a=4
b=5
print(a&b)
4
a=3
b=4
print(a|b)
7
a=5
b=6
print(a^b)
3
a=64
print(~a)
-65
a=5
print(a>>1)
2
b=4
print(b<<2)
16
a=20
if(a==20):
    print("A is Equal")

    
A is Equal
a=30
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
a=25
if(a%5==0):
    print("A is odd")
else:
    print("A is not Even")

    
A is odd
a=42
if(a%3==0):
    print("A is Even")
else:
    print("A is not odd")

    
A is Even
a=57
if(a%2==0):
    print("A is Even")
else:
    print("A is odd")

    
A is odd
a=int(input("Enter the number"))
Enter the number25
if(a%2==0):
    print("It is a Even number")
else:
    print("It is not odd number")

    
It is not odd number
age=int(input("Enter the age is ::"))
Enter the age is ::70
if(age>=61):
    salary=int(input("Enter the salary is ::"))
    if(salary>=25000):
        bns=salary+500;
        print("Your salary is ::",bns)
    else:
        bns=salary+1000:
            
SyntaxError: invalid syntax
age=int(input("Enter the age is ::"))
Enter the age is ::70
if(age>=61):
    salary=int(input("Enter the salary is ::"))
    if(salary>=25000):
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
Enter the age is ::40
if(age>=61):
    salary=int(input("Enter the salary is ::"))
    if(salary>=25000):
        bns=salary+500;
        print("Your salary is ::",bns)
    else:
        bns=salary+1000;
        print("Your salary is ::",bns)
else:
    print("Your age is invalid")

    
Your age is invalid
age=int(input("Enter the age is ::"))
Enter the age is ::71
if(age>=61):
    salary=int(input("Enter the salary is ::"))
    if(salary>=25000):
        bns=salary+500;
        print("Your salary is ::",bns)
    else:
        bns=salary+1000;
        print("Your salary is ::",bns)
else:
    print("Your age is invalid")

    
Enter the salary is ::20000
Your salary is :: 21000
m1=int(input("Enter the m1 value is ::"))
Enter the m1 value is ::250
m2=int(input("Enter the m2 value is ::"))
Enter the m2 value is ::300
m3=int(input("Enter the m3 value is ::"))
Enter the m3 value is ::400
tot=m1+m2+m3
if(tot>=900 and tot>1000):
    print("Grade-A")
elif(tot>=700 and tot>800):
    print("Grade-B")
elif(tot>=500 and tot>600):
    print("Grade-C")
else:
    print("Fail")

    
Grade-B
m1=int(input("Enter the m1 value is ::"))
Enter the m1 value is ::500
m2=int(input("Enter the m2 value is ::"))
Enter the m2 value is ::400
m3=int(input("Enter the m3 value is ::"))
Enter the m3 value is ::300
tot=m1+m2+m3if(tot>=900 and tot>1000):
    print("Grade-A")
elif(tot>=700 and tot>800):
    print("Grade-B")
elif(tot>=500 and tot>600):
    print("Grade-C")
else:
    print("Fail")
    
SyntaxError: invalid syntax
m1=int(input("Enter the m1 value is ::"))
Enter the m1 value is ::500
m2=int(input("Enter the m2 value is ::"))
Enter the m2 value is ::400
m3=int(input("Enter the m3 value is ::"))
Enter the m3 value is ::300
tot=m1+m2+m3
if(tot>=900 and tot>1000):
    print("Grade-A")
elif(tot>=700 and tot>800):
    print("Grade-B")
elif(tot>=500 and tot>600):
    print("Grade-C")
else:
    print("Fail")

    
Grade-A
m1=int(input("Enter the m1 value is ::"))
Enter the m1 value is ::300
m2=int(input("Enter the m2 value is ::"))
Enter the m2 value is ::200
m3=int(input("Enter the m3 value is ::"))
Enter the m3 value is ::150
tot=m1+m2+m3
if(tot>=900 and tot>1000):
    print("Grade-A")
elif(tot>=700 and tot>800):
    print("Grade-B")
elif(tot>=500 and tot>600):
    print("Grade-C")
else:
    print("Fail")

    
Grade-C
m1=int(input("Enter the m1 value is ::"))
Enter the m1 value is ::250
m2=int(input("Enter the m2 value is ::"))
Enter the m2 value is ::150
m3=int(input("Enter the m3 value is ::"))
Enter the m3 value is ::100
tot=m1+m2+m3
if(tot>=900 and tot>1000):
    print("Grade-A")
elif(tot>=700 and tot>800):
    print("Grade-B")
elif(tot>=500 and tot>600):
    print("Grade-C")
else:
    print("Fail")

    
Fail
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
        print("Odd is ::",i)

        
Even is :: 0
Odd is :: 1
Even is :: 2
Odd is :: 3
Even is :: 4
Odd is :: 5
Even is :: 6
Odd is :: 7
Even is :: 8
Odd is :: 9
for i in range (0,2,1):
    for j in range (0,2,1):
        print("I value is ::",i,"J value is ::",j)

        
I value is :: 0 J value is :: 0
I value is :: 0 J value is :: 1
I value is :: 1 J value is :: 0
I value is :: 1 J value is :: 1
n=5,m=5
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
n=5
m=5
for i in range (0,n,1):
    for j in range (0,m,1):
        print("#",end="")
        print()

        
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
n=5
m=5
for i in range (0,5,1):
    for j in range (0,5,1):
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
for i in range (0,5,1):
    for j in range (0,5,1):
        print("i",end="")
      print()
      
SyntaxError: unindent does not match any outer indentation level
for i in range (0,5,1):
    for j in range (0,5,1):
        print("i",end="")
print()
SyntaxError: invalid syntax
n=5
m=5
for i in range (0,5,1):
    for j in range (0,5,1):
        print(i,end="")
      print()
      
SyntaxError: unindent does not match any outer indentation level
n=5
m=5
for i in range (0,5,1):
    for j in range (0,5,1):
        print(i,end="")
        print()

        
0
0
0
0
0
1
1
1
1
1
2
2
2
2
2
3
3
3
3
3
4
4
4
4
4
n=5
m=5
for i in range (0,5,1):
    for j in range (0,5,1):
        print(i,end="")

        
0000011111222223333344444
n=5
m=5
for i in range (0,5,1):
    for j in range (0,5,1):
        print(i)
        print()

        
0

0

0

0

0

1

1

1

1

1

2

2

2

2

2

3

3

3

3

3

4

4

4

4

4


========================================================= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/te.py =========================================================
Traceback (most recent call last):
  File "C:/Users/User/AppData/Local/Programs/Python/Python313/te.py", line 1, in <module>
    for i in range (0,n,1):
NameError: name 'n' is not defined

========================================================= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/te.py =========================================================
Traceback (most recent call last):
  File "C:/Users/User/AppData/Local/Programs/Python/Python313/te.py", line 1, in <module>
    for i in range (0,n,1):
NameError: name 'n' is not defined

========================================================= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/te.py =========================================================
Traceback (most recent call last):
  File "C:/Users/User/AppData/Local/Programs/Python/Python313/te.py", line 1, in <module>
    for i in range (0,n,1):
NameError: name 'n' is not defined

========================================================= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/te.py =========================================================
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

========================================================= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/te.py =========================================================
#####
#####
#####
#####
#####

========================================================= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/te.py =========================================================
00000
11111
22222
33333
44444

========================================================= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/te.py =========================================================
55555
55555
55555
55555
55555

========================================================= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/te.py =========================================================
01234
01234
01234
01234
01234

========================================================= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/te.py =========================================================
01234
01234
01234
01234
01234
00000
11111
22222
33333
44444

========================================================= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/te.py =========================================================
01234
01234
01234
01234
01234
00000
11111
22222
33333
44444

==================================================== RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/Nested loop1.py ====================================================
00000
11111
22222
33333
44444
