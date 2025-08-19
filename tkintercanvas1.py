from tkinter import*
top=Tk()
top.geometry("600x600")
#creating a simple canvas
c=Canvas(top,bg="pink",height="400",width=400)
arc=c.create_arc((20,40,250,300),start=0,extent=250,fill="lightblue")
c.pack()
top.mainloop()
