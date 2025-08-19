from tkinter import*
m1=Tk()
W=Canvas(m1,width=40,height=60)
W.pack()
canvas_h=20
canvas_w=200
y=int(canvas_h/2)
W.create_line(0,y,canvas_w,y)
mainloop()
