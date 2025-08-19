Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=2
b=5
print(a&b)
0
a=5
b=6
print(a&b)
4
a=6
b=8
print(a|b)
14
a=8
b=7
print(a|b)
15
a=6
b=8
print(a^b)
14
a=9
b=5
print(a^b)
12
a=85
print(~a)
-86
a=6
print(a>>1)
3
a=7
print(a>>2)
1
a=9
print(a<<1)
18
a=12
print(a<<2)
48
a=25
if(a==25):
    print("A is Equal")

    
A is Equal
a=30
if(a==20):
    print("A is Equal")
else:
    print("A is not Equal")

    
A is not Equal
a=47
if(a%2==0):
    print("A is odd")
else:
    print("A is Even")

    
A is Even
a=int(input("Enter the number"))
Enter the number51
if(a%2==0):
    print("It is a Even number")
else:
    print("It is not odd number")

    
It is not odd number
age=int(input("Enter the age is::"))
Enter the age is::62
if(age>=61):
    salary=int(input("Enter the salary is::"))
    if(salary>=30000):
        bns=salary+1000;
        print("Your salary is::",bns)
    else:
        bns=salary+1500;
        print("Your salary is::",bns)
else:
    print("Your age is invalid")

    
Enter the salary is::50000
Your salary is:: 51000
age=int(input("Enter the age is::"))
Enter the age is::25
if(age>=61):
    salary=int(input("Enter the salary is::"))
    if(salary>=30000):
        bns=salary+1000;
        print("Your salary is::",bns)
    else:
        bns=salary+1500;
        print("Your salary is::",bns)
else:
    print("Your age is invalid")

    
Your age is invalid
age=int(input("Enter the age is::"))
Enter the age is::65
if(age>=61):
    salary=int(input("Enter the salary is::"))
    if(salary>=30000):
        bns=salary+1000;
        print("Your salary is::",bns)
    else:
        bns=salary+1500;
        print("Your salary is::",bns)
else:
    print("Your age is invalid")

    
Enter the salary is::28000
Your salary is:: 29500
m1=int(input("Enter the m1 value is::"))
Enter the m1 value is::500
m2=int(input("Enter the m2 value is::"))
Enter the m2 value is::
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    m2=int(input("Enter the m2 value is::"))
ValueError: invalid literal for int() with base 10: ''
m1=int(input("Enter the m1 value is::"))
Enter the m1 value is::500
m2=int(input("Enter the m2 value is::"))
Enter the m2 value is::300
m3=int(input("Enter the m3 value is::"))
Enter the m3 value is::400
tot=m1+m2+m3
if(tot>=1000 and tot>1200):
    print("Grade-A")
elif(tot>=800 and tot>1000):
    print("Grade-B")
elif(tot>=600 and tot>800):
    print("Grade-C")
else:
    print("Fail")

    
Grade-B
m1=int(input("Enter the m1 value is::"))
Enter the m1 value is::600
m2=int(input("Enter the m2 value is::"))
Enter the m2 value is::400
m3=int(input("Enter the m3 value is::"))
Enter the m3 value is::300
tot=m1+m2+m3
if(tot>=1000 and tot>1200):
    print("Grade-A")
elif(tot>=800 and tot>1000):
    print("Grade-B")
elif(tot>=600 and tot>800):
    print("Grade-C")
else:
    print("Fail")

    
Grade-A
m1=int(input("Enter the m1 value is::"))
Enter the m1 value is::400
m2=int(input("Enter the m2 value is::"))
Enter the m2 value is::300
m3=int(input("Enter the m3 value is::"))
Enter the m3 value is::250
tot=m1+m2+m3
if(tot>=1000 and tot>1200):
    print("Grade-A")
elif(tot>=800 and tot>1000):
    print("Grade-B")
elif(tot>=600 and tot>800):
    print("Grade-C")
else:
    print("Fail")

    
Grade-C
m1=int(input("Enter the m1 value is::"))
Enter the m1 value is::250
m2=int(input("Enter the m2 value is::"))
Enter the m2 value is::500
m3=int(input("Enter the m3 value is::"))
Enter the m3 value is::50
tot=m1+m2+m3
if(tot>=1000 and tot>1200):
    print("Grade-A")
elif(tot>=800 and tot>1000):
    print("Grade-B")
elif(tot>=600 and tot>800):
    print("Grade-C")
else:
    print("Fail")

    
Fail

for i in range (0,10,1):
    print("I value is::",i)

    
I value is:: 0
I value is:: 1
I value is:: 2
I value is:: 3
I value is:: 4
I value is:: 5
I value is:: 6
I value is:: 7
I value is:: 8
I value is:: 9
for i in range (10,20,2):
    print("I value is::",i)

    
I value is:: 10
I value is:: 12
I value is:: 14
I value is:: 16
I value is:: 18
for i in range (0,10,1):
    if(i%2==0):
        print("Even is::",i)
    else:
        print("Odd is::",i)

        
Even is:: 0
Odd is:: 1
Even is:: 2
Odd is:: 3
Even is:: 4
Odd is:: 5
Even is:: 6
Odd is:: 7
Even is:: 8
Odd is:: 9
for i in range (0,2,1):
    for j in range (0,2,1):
        print("I value is::",i,"J value is::",j)

        
I value is:: 0 J value is:: 0
I value is:: 0 J value is:: 1
I value is:: 1 J value is:: 0
I value is:: 1 J value is:: 1
n=5
m=5
for i in range (0,n,1):
    for j in range (0,m,1):
        print(*,end="")
        
SyntaxError: Invalid star expression
n=5
m=5
for i in range (0,n,1):
    for j in range (0,m,1):
        print(*,end="")
        
SyntaxError: Invalid star expression
n=5
m=5
for i in range (0,n,1):
    for j in range (0,m,1):
        print("*",end="")
        
SyntaxError: multiple statements found while compiling a single statement

=================================================== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\Nested looping.py ===================================================
J
J
J
J
J
J
J
J
J
J
J
J
J
J
J
J
J
J
J
J
J
J
J
J
J
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

=================================================== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\Nested looping.py ===================================================
JJJJJ
JJJJJ
JJJJJ
JJJJJ
JJJJJ
*****
*****
*****
*****
*****

=================================================== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\Nested looping.py ===================================================
JJJJJ
JJJJJ
JJJJJ
JJJJJ
JJJJJ
*****
*****
*****
*****
*****

=================================================== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\Nested looping.py ===================================================
JJJJJ
JJJJJ
JJJJJ
JJJJJ
JJJJJ
*****
*****
*****
*****
*****

=================================================== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\Nested looping.py ===================================================
iiiii
iiiii
iiiii
iiiii
iiiii
*****
*****
*****
*****
*****

=================================================== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\Nested looping.py ===================================================
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

=================================================== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\Nested looping.py ===================================================
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

==================================================== RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/nested loop5.py ====================================================
00000
11111
22222
33333
44444

==================================================== RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/nested loop5.py ====================================================

==================================================== RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/nested loop5.py ====================================================
00000

11111

22222

33333

44444

==================================================== RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/nested loop5.py ====================================================
00000
11111
22222
33333
44444

==================================================== RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/nested loop5.py ====================================================
01234
01234
01234
01234
01234
i=0
while(i<=5):
    print("I value is::",i)
    i=i+1

    
I value is:: 0
I value is:: 1
I value is:: 2
I value is:: 3
I value is:: 4
I value is:: 5
>>> 
==================================================== RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/nested loop5.py ====================================================
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
>>> 
==================================================== RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/nested loop5.py ====================================================
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
>>> 
=================================================== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\Nested looping.py ===================================================
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
