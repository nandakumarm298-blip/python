s=0;
n=int(input("Enter the n value is ::"))
temp=n;
while(n>0):
    rem=n%10;
    s  =s+rem*rem*rem;
    n  =n//10;
if(temp==s):
    print("This is Armstrong")
else:
    print("Not an Armstrong")
