Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s=0;
n=int(input("Enter the n value is ::"))
Enter the n value is ::153
temp=n;
while(n>0):
    rem=n%10;
    s=s+rem*rem;
    n=n//10;
    if(temp==0):
        print("This is Armstrong")
    else:
        print("NOt an Armstrong")

        
NOt an Armstrong
NOt an Armstrong
NOt an Armstrong
s=0;
n=int(input("Enter the n value is ::"))
Enter the n value is ::153
temp=n;
while(n>0):
    rem=n%10;
    s=s+rem*rem
    n=n//10;
    if(temp==0):
        print("This is Armstrong")
    else:
        print("NOt an Armstrong")
        
SyntaxError: multiple statements found while compiling a single statement

====================================================== RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/Armstrong.py =====================================================
Enter the n value is ::153
NOt an Armstrong
NOt an Armstrong
NOt an Armstrong

====================================================== RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/Armstrong.py =====================================================
Enter the n value is ::153
NOt an Armstrong
NOt an Armstrong
NOt an Armstrong

====================================================== RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/Armstrong.py =====================================================
Enter the n value is ::153
NOt an Armstrong
NOt an Armstrong
This is Armstrong

====================================================== RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/Armstrong.py =====================================================
Enter the n value is ::153
This is Armstrong

c=int(input("Enter the number of terms ::"))
Enter the number of terms ::5
first=0
second=1
for i in range (c):
    if i <= 1:
        next=i
    else:
        next=first+second
        first=second
        second=next
        print(next)

        
1
2
3
>>> 
================================================== RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/fibonocci series.py ==================================================
Enter the number of terms ::6
1
2
3
5
>>> 
================================================== RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/fibonocci series.py ==================================================
Enter the number of terms ::6
0
1
1
2
3
5
>>> 
================================================== RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/fibonocci series.py ==================================================
Enter the number of terms ::7
0
1
1
2
3
5
8
>>> 
====================================================== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\Armstrong.py =====================================================
Enter the n value is ::202
NOt an Armstrong
>>> 
======================================================== RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/swap.py ========================================================
Before swapping :: 10 20
After swapping :: 20 10
>>> 
======================================================== RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/swap.py ========================================================
Before swapping :: 10 20
After swapping :: 20 10
>>> 
======================================================== RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/swap.py ========================================================
Before swapping :: 10 20
After swapping :: 20 10
Before swapping :: 25 50
After swapping :: 50 25
