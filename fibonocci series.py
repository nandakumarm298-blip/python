c=int(input("Enter the number of terms ::"))
first=0
second=1
for i in range (c):
    if i<=1:
        next=i
    else:
        next=first+second
        first=second
        second=next
    print(next)
