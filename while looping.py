Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
i=0
while(i<=5):
    print("I value is ::",i)
    i=i+1

    
I value is :: 0
I value is :: 1
I value is :: 2
I value is :: 3
I value is :: 4
I value is :: 5

n=int(input("Enter the n value is ::"))
Enter the n value is ::1234
reverse=0;
while(n!=0):
    reverse=reverse*10;
    reverse=reverse+n%10;
    n      =n//10;
    print("Reverse Number is ::",reverse)

    
Reverse Number is :: 4
Reverse Number is :: 43
Reverse Number is :: 432
Reverse Number is :: 4321
n=int(input("Enter the n value is ::"))
Enter the n value is ::123
reverse=0;while(n!=0):
    reverse=reverse*10;
    reverse=reverse+n%10;
    n      =n//10;
    print("Reverse Number is ::",reverse)
    
SyntaxError: invalid syntax
n=int(input("Enter the n value is ::"))
Enter the n value is ::123
reverse=0;
while(n!=0):
    reverse=reverse*10;
    reverse=reverse+n%10;
    n      =n//10;
    print("Reverse Number is ::",reverse)

    
Reverse Number is :: 3
Reverse Number is :: 32
Reverse Number is :: 321
>>> 
>>> t=int(input("Enter the value is ::"))
Enter the value is ::1234
>>> sum=0;
>>> while(t!=0):
...     remainder=t%10;
...     sum      =sum+remainder;
...     t        =t//10;
...     print("sum of digits ::",sum)
... 
...     
sum of digits :: 4
sum of digits :: 7
sum of digits :: 9
sum of digits :: 10
>>> 
>>> fact=1
>>> for i in range (1,4):
...     fact=fact*i;
...     print("Fact value is ::",fact)
... 
...     
Fact value is :: 1
Fact value is :: 2
Fact value is :: 6
>>> fact=1for i in range (1,7):
...     fact=fact*i;
...     print("Fact value is ::",fact)
...     
SyntaxError: invalid syntax
>>> 
>>> fact=1
>>> for i in range (1,7):
...     fact=fact*i;
...     print("Fact value is ::",fact)
... 
...     
Fact value is :: 1
Fact value is :: 2
Fact value is :: 6
Fact value is :: 24
Fact value is :: 120
Fact value is :: 720
