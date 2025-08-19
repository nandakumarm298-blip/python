
from tkinter import*

t1=Tk()
t1.geometry("500x500")
enterid=Label(t1,text="Enter ID:").grid(row=1,column=0)
e1=Entry(t1).grid(row=1,column=1)
name=Label(t1,text="Name:").grid(row=2,column=0)
e2=Entry(t1).grid(row=2,column=1)
phone=Label(t1,text="phone:").grid(row=3,column=0)
e3=Entry(t1).grid(row=3,column=1)
insert=Button(t1,text="Insert").place(x=70,y=70)
delete=Button(t1,text="Delete").place(x=120,y=70)
update=Button(t1,text="Update").place(x=180,y=70)
select=Button(t1,text="Select").place(x=120,y=110)
t1.mainloop()

"""

t2=Tk()
t2.geometry("250x250")
person=Button(t2,text="Person",width="20").place(x=70,y=40)
product=Button(t2,text="Product",width="20").place(x=70,y=100)
staff=Button(t2,text="Staff",width="20").place(x=70,y=160)
t2.mainloop()
"""
