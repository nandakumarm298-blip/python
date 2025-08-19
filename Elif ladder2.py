m1=int(input("Enter the m1 value is ::"))
m2=int(input("Enter the m2 value is ::"))
m3=int(input("Enter the m3 value is ::"))
tot=m1+m2+m3
if(tot>=900 and tot<=1200):
    print("Grade-A")
elif(tot>=700 and tot<900):
    print("Grade-B")
elif(tot>=500 and tot<700):
    print("Grade-C")
else:
    print("Fail")
    
