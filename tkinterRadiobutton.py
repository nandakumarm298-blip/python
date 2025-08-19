from tkinter import*
r=Tk()
v=IntVar()
Radiobutton(r,text="Male",variable=v,value=1).pack(anchor=W)
Radiobutton(r,text="Female",variable=v,value=2).pack(anchor=W)
mainloop()
