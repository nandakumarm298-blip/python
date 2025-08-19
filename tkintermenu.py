from tkinter import*
top=Tk()
def home():
    print("Home")
def addproduct():
    print("addproduct")
#create a toplevel menu
menubar=Menu()
menubar.add_command(label="Home",command="home")
menubar.add_command(label="Addproduct",command="addproduct")
menubar.add_command(label="AboutUs",command=top.quit)
#display the menu
top.config(menu=menubar)
top.mainloop()
