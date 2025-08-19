from tkinter import*
t=Tk()
t.geometry("200x200")
checkvar1=IntVar()
checkvar2=IntVar()

chkbtn1=Checkbutton(t,text="C",variable=checkvar1,onvalue=1,offvalue=0,height=2,width=10)
chkbtn2=Checkbutton(t,text="Java",variable=checkvar2,onvalue=1,offvalue=0,height=2,width=10)
chkbtn1.pack()
chkbtn2.pack()
t.mainloop()
