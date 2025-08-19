Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> i=0
>>> while(i<=5):
...     print("I value is ::",i)
...     i=i+1
... 
...     
I value is :: 0
I value is :: 1
I value is :: 2
I value is :: 3
I value is :: 4
I value is :: 5
>>> n=int(input("Enter the n value is ::"))
Enter the n value is ::
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    n=int(input("Enter the n value is ::"))
ValueError: invalid literal for int() with base 10: ''
>>> n=int(input("Enter the n value is ::"))
Enter the n value is ::531
>>> reverse=0;
>>> while(n!=0):
...     reverse=reverse*10;
...     reverse=reverse+n%10;
...     n=n//10;
...     print("Reverse number is ::",reverse)
... 
...     
Reverse number is :: 1
Reverse number is :: 13
Reverse number is :: 135
>>> t=int(input("Enter the value is ::"))
Enter the value is ::12345
>>> sum=0;
>>> while(t!=0):
...     remainder=t%10;
...     sum      =sum+remainder;
...     t        =t//10;
...     print("sum of digits ::",sum)
... 
...     
sum of digits :: 5
sum of digits :: 9
sum of digits :: 12
sum of digits :: 14
sum of digits :: 15
fact=1
for i in range (1,4):
    fact=fact*i;
    print("Fact value is ::",fact)

    
Fact value is :: 1
Fact value is :: 2
Fact value is :: 6
s=0;
n=int(input("Enter the n value is ::"))
Enter the n value is ::153
temp=n;
while(n>0):
    rem=n%10;
    s  =s+rem*rem*rem;
    n  =n//10;
if(temp==s):
    
SyntaxError: invalid syntax

===================================================== RESTART: C:/Users/User/AppData/Local/Programs/Python/Python313/Armstrong1.py =====================================================
Enter the n value is ::153
This is Armstrong

================================================== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\fibonocci series.py ==================================================
Enter the number of terms ::123
0
1
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

================================================== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\fibonocci series.py ==================================================
Enter the number of terms ::8
0
1
1
2
3
5
8
13

======================================================== RESTART: C:\Users\User\AppData\Local\Programs\Python\Python313\swap.py ========================================================
Before swapping :: 10 20
After swapping :: 20 10
Before swapping :: 25 50
After swapping :: 50 25
