Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
==== No Subprocess ====

WARNING: Running IDLE without a Subprocess is deprecated
and will be removed in a later version. See Help/IDLE Help
for details.

age=int(input("Enter the age is::"))
Enter the age is::65
if(age>=61):
    salary=int(input("Enter the salary is::"))
    if(salary>=25000):
        bns=salary+1000;
        print("Your salary is::",bns)
    else:
        bns=salary+1800;
        print("Your salary is::",bns)
else:
    print("Your age is invalid")

    
Enter the salary is::30000
Your salary is:: 31000
age=int(input("Enter the age is::"))
Enter the age is::50
if(age>=61):
    salary=int(input("Enter the salary is::"))
    if(salary>=25000):
        bns=salary+1000;
        print("Your salary is::",bns)
    else:
        bns=salary+1800;
        print("Your salary is::",bns)
else:
    print("Your age is invalid")

    
Your age is invalid
age=int(input("Enter the age is::"))
Enter the age is::62
if(age>=61):
    salary=int(input("Enter the salary is::"))
    if(salary>=25000):
        bns=salary+1000;
        print("Your salary is::",bns)
    else:
        bns=salary+1800;
        print("Your salary is::",bns)
else:
    print("Your age is invalid")

    
Enter the salary is::22000
Your salary is:: 23800
m1=int(input("Enter the m1 value is::"))
Enter the m1 value is::300
m2=int(input("Enter the m2 value is::"))
Enter the m2 value is::250
m3=int(input("Enter the m3 value is::"))
Enter the m3 value is::400
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
m1=int(input("Enter the m1 value is::"))
Enter the m1 value is::200
m2=int(input("Enter the m2 value is::"))
Enter the m2 value is::150
m3=int(input("Enter the m3 value is::"))
Enter the m3 value is::100
tot=m1+m2+m3
if(tot>=900):
    print("Grade-A")
elif(tot>=700):
    print("Grade-B")
elif(tot>=500):
    print("Grade-C")
else:
    print("Fail")

    
Fail
m1=int(input("Enter the m1 value is::"))
Enter the m1 value is::250
m2=int(input("Enter the m2 value is::"))
Enter the m2 value is::300
m3=int(input("Enter the m3 value is::"))
Enter the m3 value is::200
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
for i in range(10,20,2):
    print("I value is::",i)

    
I value is:: 10
I value is:: 12
I value is:: 14
I value is:: 16
I value is:: 18
i=0
j=1
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
i=0
j=1
for i in range(0,10,1):
    if(i%2==0):
        print("Even is::",i)
        i=i+(i+1)
    else:
        print("Odd is::",i)
        j=j*(i+1)

        
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
i=0
j=1
for i in range(0,10,1):
    if(i%2==0):
        i=i+(i+1)
        print("Even is::",i)
    else:
        j=j*(i+1)
        print("Odd is::",i)

        
Even is:: 1
Odd is:: 1
Even is:: 5
Odd is:: 3
Even is:: 9
Odd is:: 5
Even is:: 13
Odd is:: 7
Even is:: 17
Odd is:: 9
for i in range(0,2,1):
    for j in range(0,2,1):
        print("I value is::",i,"J value is::",j)

        
I value is:: 0 J value is:: 0
I value is:: 0 J value is:: 1
I value is:: 1 J value is:: 0
I value is:: 1 J value is:: 1
n=5
m=5
for i in range(0,n,1):
    for j in range(0,m,1):
        print("*",end="")
    print()

    
*****
*****
*****
*****
*****
n=5
m=5
for i in range(0,n,1):
    for j in range(0,m,1):
        print("j",end="")
    print()

    
jjjjj
jjjjj
jjjjj
jjjjj
jjjjj
n=5
m=5
for i in range(0,n,1):
    for j in range(0,m,1):
        print(j,end="")
    print()

    
01234
01234
01234
01234
01234
n=5
m=5
for i in range(0,n,1):
    for j in range(0,m,1):
        print(i,end="")
    print()

    
00000
11111
22222
33333
44444
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()

    
*
**
***
****
*****
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()

    
1
22
333
4444
55555
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()

    
1
12
123
1234
12345
for i in range(1,6):
    for j in range(1,6):
        if(j>=i):
            print("*",end="")
        else:
            print("",end="")
    print()

    
*****
****
***
**
*
for i in range(1,6):
    for j in range(1,6):
        if(j>6-i):
            print("",end="")
        else:
            print("*",end="")
    print()

    
*****
****
***
**
*
for i in range(1,6):
    for j in range(1,6):
        if(j>6-i):
            print("",end="")
        else:
            print(i,end="")
    print()

    
11111
2222
333
44
5
for i in range(1,6):
    for j in range(1,6):
        if(j>6-i):
            print("",end="")
        else:
            print(j,end="")
    print()

    
12345
1234
123
12
1
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
n=int(input("Enter the n value is::"))
Enter the n value is::512
reverse=0;
while(n!=0):
    reverse=reverse*10;
    reverse=reverse+n%10;
    n=n//10;
    print("Reverse Number is::",reverse)

    
Reverse Number is:: 2
Reverse Number is:: 21
Reverse Number is:: 215
t=int(input("Enter the value is::"))
Enter the value is::12
3t=int(input("Enter the value is::"))
Enter the value is::1234
sum=0;
while(t!=0):
    remainder=t%10;
    sum=sum+remainder;
    t=t//10;
    print("sum of Digits::",sum)

    
sum of Digits:: 4
sum of Digits:: 7
sum of Digits:: 9
sum of Digits:: 10
Fact=1
for i in range(1,4):
    Fact=fact*i;
    print("Fact value is::",fact)

    
Traceback (most recent call last):
  File "<pyshell#150>", line 2, in <module>
    Fact=fact*i;
         ^^^^
NameError: name 'fact' is not defined. Did you mean: 'Fact'?
Fact=1
for i in range(1,4):
    Fact=fact*i;
    print("Fact value is::",Fact)

    
Traceback (most recent call last):
  File "<pyshell#153>", line 2, in <module>
    Fact=fact*i;
         ^^^^
NameError: name 'fact' is not defined. Did you mean: 'Fact'?
Fact=1
for i in range(1,4):
    Fact=Fact*i;
    print("Fact value is::",Fact)

    
Fact value is:: 1
Fact value is:: 2
Fact value is:: 6
s=0;
n=int(input("Enter the n value is::"))
Enter the n value is::153
temp=n;
while(n>0):
    rem=n%10;
    s=s+rem*rem*rem;
    n=n//10;
if(temp==s):
    
SyntaxError: invalid syntax
s=0;
n=int(input("Enter the n value is::"))
Enter the n value is::153
temp=n;
while(n>0):
    rem=n%10;
    s=s+rem*rem*rem;
    n=n//10;
    if(temp==s):
        print("This is Armstrong")
    else:
        print("Not an Armstrong")

        
Not an Armstrong
Not an Armstrong
This is Armstrong
Enter the n value is ::15
NOt an Armstrong
Enter the n value is ::153
This is Armstrong
c=int(input("Enter the number of terms::"))
Enter the number of terms::3
first=0
second=1
for i in range(c):
    if i<=1:
        next=i
    else:
        next=first+second
        first=second
        second=next
        print(next)

        
1
c=int(input("Enter the number of terms::"))
Enter the number of terms::123
first=0
second=1
for i in range(c):
    if i<=1:
        next=i
    else:
        next=first+second
        first=second
        second=next
        print(next)

        
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765
10946
17711
28657
46368
75025
121393
196418
317811
514229
832040
1346269
2178309
3524578
5702887
9227465
14930352
24157817
39088169
63245986
102334155
165580141
267914296
433494437
701408733
1134903170
1836311903
2971215073
4807526976
7778742049
12586269025
20365011074
32951280099
53316291173
86267571272
139583862445
225851433717
365435296162
591286729879
956722026041
1548008755920
2504730781961
4052739537881
6557470319842
10610209857723
17167680177565
27777890035288
44945570212853
72723460248141
117669030460994
190392490709135
308061521170129
498454011879264
806515533049393
1304969544928657
2111485077978050
3416454622906707
5527939700884757
8944394323791464
14472334024676221
23416728348467685
37889062373143906
61305790721611591
99194853094755497
160500643816367088
259695496911122585
420196140727489673
679891637638612258
1100087778366101931
1779979416004714189
2880067194370816120
4660046610375530309
7540113804746346429
12200160415121876738
19740274219868223167
31940434634990099905
51680708854858323072
83621143489848422977
135301852344706746049
218922995834555169026
354224848179261915075
573147844013817084101
927372692193078999176
1500520536206896083277
2427893228399975082453
3928413764606871165730
6356306993006846248183
10284720757613717413913
16641027750620563662096
26925748508234281076009
43566776258854844738105
70492524767089125814114
114059301025943970552219
184551825793033096366333
298611126818977066918552
483162952612010163284885
781774079430987230203437
1264937032042997393488322
2046711111473984623691759
3311648143516982017180081
5358359254990966640871840
8670007398507948658051921
14028366653498915298923761
c=int(input("Enter the number of terms::"))
Enter the number of terms::12
first=0
second=1
for i in range(c):
    if i<=1:
        next=i
    else:
        next=first+second
        first=second
        second=next
        print(next)

        
1
2
3
5
8
13
21
34
55
89
>>> c=int(input("Enter the number of terms::"))
Enter the number of terms::4
>>> first=0
>>> second=1
>>> for i in range(c):
...     if i<=1:
...         next=i
...     else:
...         next=first+second
...         first=second
...         second=next
...         print(next)
... 
...         
1
2
>>> c=int(input("Enter the number of terms::"))
Enter the number of terms::7
>>> first=0
>>> second=1
>>> for i in range(c):
...     if i<=1:
...         next=i
...     else:
...         next=first+second
...         first=second
...         second=next
...         print(next)
... 
...         
1
2
3
5
8
>>> a=10
>>> b=20
>>> print("Before swapping::",a,b)
Before swapping:: 10 20
>>> a=b+a;
>>> b=a-b;
>>> a=a-b;
>>> print("After swapping::",a,b)
After swapping:: 20 10
