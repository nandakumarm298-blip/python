n=int(input("Enter the n value is::"))
a=0
b=1
count=2
while (count<n):
    temp=b
    b=b+a
    a=temp
    count=count+1
print("value is::",b)    
