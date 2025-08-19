import tkinter as tk
from tkinter import messagebox,Label,Entry,Button
import mysql. connector as mysql


def login():
    username=entry_username.get();
    password=entry_password.get();
    
    if username=="admin" and password=="password":
        messagebox.showinfo("LoginSuccessfull","Welcome admin")
        homepage();
    else:
        messagebox.showerror("Login Failed")

def homepage():
    root=tk.Tk()
    root.geometry("300x300")
    root.title("Login Page")
    person=Button(root,text="Person",width="20",command=open_register_window_per).place(x=70,y=40)
    product=Button(root,text="Product",width="20",command=open_register_window_prd).place(x=70,y=100)
    staff=Button(root,text="Staff",width="20",command=open_register_window_staff).place(x=70,y=160)
    root.mainloop()

def open_register_window_per():
    def Insert():
        try:
            id_val=id_entry.get();
            name_val=name_entry.get();
            phone_val=phone_entry.get();

            if id_val=="" or name_val=="" or phone_val=="":
                messagebox.showinfo("ALERT","Please enter the all fields")
            else:
                conn=mysql.connect(host="localhost",user="root",password="root",database="nandakumar")
                cursor=conn.cursor();
                cursor.execute("Insert into person values(%s,%s,%s)",(id_val,name_val,phone_val))
                conn.commit()
                messagebox.showinfo("Status","Inserted")
                conn.close()
                
        except Exception as e:
             print(e)

    def update():
        id_val=id_entry.get()
        name_val=name_entry.get()
        phone_val=phone_entry.get()
        if name_val==""or phone_val=="":
            messagebox.showinfo("ALERT","Please enter the value")
        else:
            conn=mysql.connect(host="localhost",user="root",password="root",database="nandakumar")
            cursor=conn.cursor();
            cursor.execute("update Person set name = '"+ name_val +"', phone='"+ phone_val +"' where id ='"+ id_val +"'")

            conn.commit()
            messagebox.showinfo("Status","updated")
            conn.close()
    def Del():
        if id_entry.get() == "":
            messagebox.showinfo("ALERT", "Please enter ID to delete row")
        else:
            con = mysql.connect(host="localhost", user="root", password="root", database="nandakumar")
            cursor = con.cursor()
            cursor.execute("delete from person where id='"+ id_entry.get() +"'")
            cursor.execute("commit")
      
            id_entry.delete(0, 'end')
            name_entry.delete(0, 'end')
            phone_entry.delete(0, 'end')
      
            messagebox.showinfo("Status", "Successfully Deleted")
            con.close()
            
    def Select():
        if id_entry.get() == "":
            messagebox.showinfo("ALERT","ID is required to select row!")
        else:
            con = mysql.connect(host="localhost", user="root", password="root", database="nandakumar")
            cursor = con.cursor()
            cursor.execute("select * from person where id= '" + id_entry.get() +"'")
            rows = cursor.fetchall()
  
            for row in rows:
                name_entry.insert(0, row[1])
                phone_entry.insert(0, row[2])
  
            con.close()


    register_window=tk.Toplevel()
    register_window.geometry("500x500")
    register_window.title("RegisterPage")

    # Add widgets for registration
    id_label = Label(register_window, text="Enter ID:", font=("verdana 15"))
    id_label.place(x=50, y=30)
    id_entry = Entry(register_window, font=("verdana 15"))
    id_entry.place(x=170, y=30)
    name = Label(register_window, text="Name:", font=("verdana 15"))
    name.place(x=50, y=80)
    name_entry = Entry(register_window, font=("verdana 15"))
    name_entry.place(x=170, y=80)
  
    phone = Label(register_window, text="Phone:", font=("verdana 15"))
    phone.place(x=50, y=130)
    phone_entry= Entry(register_window, font=("verdana 15"))
    phone_entry.place(x=170, y=130)
  
    btnInsert = Button(register_window, text="Add_Person", command=Insert, font=("verdana 15")).place(x=100, y=200)
    btnDelete = Button(register_window, text="Delete_Person", command=Del, font=("verdana 15")).place(x=300, y=200)
    btnUpdate = Button(register_window, text="Update_Person", command=update, font=("verdana 15")).place(x=530, y=200)
    btnSelect= Button(register_window, text="Search_Person", command=Select, font=("verdana 15")).place(x=300, y=300)
     
def open_register_window_prd():
    def Insert():
        try:
            id_val=id_entry.get();
            name_val=productname_entry.get();
            price_val=productprice_entry.get();

            if id_val=="" or name_val=="" or price_val=="":
                messagebox.showinfo("ALERT","Please enter the all fields")
            else:
                conn=mysql.connect(host="localhost",user="root",password="root",database="nandakumar")
                cursor=conn.cursor();
                cursor.execute("Insert into product values(%s,%s,%s)",(id_val,name_val,price_val))
                conn.commit()
                messagebox.showinfo("Status","Inserted")
                conn.close()
                
        except Exception as e:
             print(e)
             
    def update():
        id_val=id_entry.get()
        name_val=name_entry.get()
        phone_val=phone_entry.get()
        if name_val==""or phone_val=="":
            messagebox.showinfo("ALERT","Please enter the value")
        else:
            conn=mysql.connect(host="localhost",user="root",password="root",database="nandakumar")
            cursor=conn.cursor();
            cursor.execute("update Product set name = '"+ name_val +"', price='"+ price_val +"' where id ='"+ id_val +"'")

            conn.commit()
            messagebox.showinfo("Status","updated")
            conn.close()
    def Del():
        if id_entry.get() == "":
            messagebox.showinfo("ALERT", "Please enter ID to delete row")
        else:
            con = mysql.connect(host="localhost", user="root", password="root", database="nandakumar")
            cursor = con.cursor()
            cursor.execute("delete from product where id='"+ id_entry.get() +"'")
            cursor.execute("commit")
      
            id_entry.delete(0, 'end')
            name_entry.delete(0, 'end')
            price_entry.delete(0, 'end')
      
            messagebox.showinfo("Status", "Successfully Deleted")
            con.close()
            
    def Select():
        if id_entry.get() == "":
            messagebox.showinfo("ALERT","ID is required to select row!")
        else:
            con = mysql.connect(host="localhost", user="root", password="root", database="nandakumar")
            cursor = con.cursor()
            cursor.execute("select * from product where id= '" + id_entry.get() +"'")
            rows = cursor.fetchall()
  
            for row in rows:
                name_entry.insert(0, row[1])
                price_entry.insert(0, row[2])
  
            con.close()



    register_window=tk.Toplevel()
    register_window.geometry("500x500")
    register_window.title("RegisterPage")

    # Add widgets for registration
    id_label = Label(register_window, text="Product ID:", font=("verdana 15"))
    id_label.place(x=10, y=30)
    id_entry = Entry(register_window, font=("verdana 15"))
    id_entry.place(x=200, y=30)

    productname = Label(register_window, text="Product Name:", font=("verdana 15"))
    productname.place(x=10, y=80)
    productname_entry = Entry(register_window, font=("verdana 15"))
    productname_entry.place(x=200, y=80)
  
    productprice = Label(register_window, text="Product price:", font=("verdana 15"))
    productprice.place(x=10, y=130)
    productprice_entry= Entry(register_window, font=("verdana 15"))
    productprice_entry.place(x=200, y=130)
  
    btnInsert = Button(register_window, text="Add_Product", command=Insert, font=("verdana 15")).place(x=100, y=200)
    btnDelete = Button(register_window, text="Delete_Product", command=Del, font=("verdana 15")).place(x=300, y=200)
    btnUpdate = Button(register_window, text="Update_Product", command=update, font=("verdana 15")).place(x=530, y=200)
    btnSelect= Button(register_window, text="Search_Product", command=Select, font=("verdana 15")).place(x=300, y=300)
     


def open_register_window_staff():
    def Insert():
        try:
            id_val=id_entry.get();
            name_val=staffname_entry.get();
            age_val=staffage_entry.get();

            if id_val=="" or name_val=="" or age_val=="":
                messagebox.showinfo("ALERT","Please enter the all fields")
            else:
                conn=mysql.connect(host="localhost",user="root",password="root",database="nandakumar")
                cursor=conn.cursor();
                cursor.execute("Insert into staff values(%s,%s,%s)",(id_val,name_val,age_val))
                conn.commit()
                messagebox.showinfo("Status","Inserted")
                conn.close()
                
        except Exception as e:
             print(e)

    def update():
        id_val=id_entry.get()
        name_val=staffname_entry.get()
        age_val=staffage_entry.get()
        if name_val==""or age_val=="":
            messagebox.showinfo("ALERT","Please enter the value")
        else:
            conn=mysql.connect(host="localhost",user="root",password="root",database="nandakumar")
            cursor=conn.cursor();
            cursor.execute("update staff set name = '"+ name_val +"', age='"+ age_val +"' where id ='"+ id_val +"'")

            conn.commit()
            messagebox.showinfo("Status","updated")
            conn.close()
    def Del():
        if id_entry.get() == "":
            messagebox.showinfo("ALERT", "Please enter ID to delete row")
        else:
            con = mysql.connect(host="localhost", user="root", password="root", database="nandakumar")
            cursor = con.cursor()
            cursor.execute("delete from staff where id='"+ id_entry.get() +"'")
            cursor.execute("commit")
      
            id_entry.delete(0, 'end')
            name_entry.delete(0, 'end')
            age_entry.delete(0, 'end')
      
            messagebox.showinfo("Status", "Successfully Deleted")
            con.close()
            
    def Select():
        if id_entry.get() == "":
            messagebox.showinfo("ALERT","ID is required to select row!")
        else:
            con = mysql.connect(host="localhost", user="root", password="root", database="nandakumar")
            cursor = con.cursor()
            cursor.execute("select * from staff where id= '" + id_entry.get() +"'")
            rows = cursor.fetchall()
  
            for row in rows:
                name_entry.insert(0, row[1])
                age_entry.insert(0, row[2])
  
            con.close()    
     
    register_window=tk.Toplevel()
    register_window.geometry("500x500")
    register_window.title("RegisterPage")

    # Add widgets for registration
    id_label = Label(register_window, text="Staff ID:", font=("verdana 15"))
    id_label.place(x=10, y=30)
    id_entry = Entry(register_window, font=("verdana 15"))
    id_entry.place(x=200, y=30)

    staffname = Label(register_window, text="Staff Name:", font=("verdana 15"))
    staffname.place(x=10, y=80)
    staffname_entry = Entry(register_window, font=("verdana 15"))
    staffname_entry.place(x=200, y=80)
  
    staffage = Label(register_window, text="Staff age:", font=("verdana 15"))
    staffage.place(x=10, y=130)
    staffage_entry= Entry(register_window, font=("verdana 15"))
    staffage_entry.place(x=200, y=130)
  
    btnInsert = Button(register_window, text="Add_Staff", command=Insert, font=("verdana 15")).place(x=100, y=200)
    btnDelete = Button(register_window, text="Delete_Staff", command=Del, font=("verdana 15")).place(x=300, y=200)
    btnUpdate = Button(register_window, text="Update_Staff", command=update, font=("verdana 15")).place(x=530, y=200)
    btnSelect= Button(register_window, text="Search_Staff", command=Select, font=("verdana 15")).place(x=300, y=300)
     



# create main window
root=tk.Tk()
root.title("Login Page")


# create username label and entry
label_username=tk.Label(root,text="Username:")
label_username.grid(row=0,column=0,padx=10,pady=5)
entry_username=tk.Entry(root)
entry_username.grid(row=0,column=1,padx=10,pady=5)


# create password label and entry
label_password=tk.Label(root,text="Password:")
label_password.grid(row=1,column=0,padx=10,pady=5)
entry_password=tk.Entry(root,show="*")
entry_password.grid(row=1,column=1,padx=10,pady=5)

# create login button
login_button=tk.Button(root,text="Login",command=login)
login_button.grid(row=2,column=0,columnspan=2,padx=10,pady=10)

# create register button
#register_button=tk.Button(root,text="Register",command=open_register_window_per,command=open_register_window_prd,command=open_register_window_staff)
#register_button.grid(row=3,column=0,columnspan=2,padx=10,pady=10)
root.mainloop()
    
    
