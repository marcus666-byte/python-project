from tkinter import *
import mysql.connector
import tkinter as tk
from tkinter import messagebox
from datetime import *
import time
root=Tk()
root.title("Admin Login")
root.geometry("450x450")
root.configure(background="cyan")

mydb = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1",
                               database='lifechoicesonline', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

lblfrstrow = tk.Label(root, text="Username -", )
lblfrstrow.place(x=50, y=20)

Username = tk.Entry(root, width=35)
Username.place(x=150, y=20, width=100)

lblsecrow = tk.Label(root, text="Password -")
lblsecrow.place(x=50, y=50)

password = tk.Entry(root, width=35)
password.place(x=150, y=50, width=100)


lbluser = tk.Label(root, text="Username - Stacy_admin")
lbluser.place(x=100, y=300)

lblpass = tk.Label(root, text="Password - @Life1234")
lblpass.place(x=100, y=330)


def login():
    user=Username.get()
    pws=password.get()
    sql= "select * from Admin where username= %s and password= %s "
    mycursor.execute(sql, [(user),(pws)])
    result = mycursor.fetchall()
    if result:

        messagebox.showinfo('Message', 'Logged in successfully')


        root.withdraw()
        import admin
        admin.admin()


def close():
    ext = messagebox.askyesno(title="?", message="are you sure, you want to exit?")
    if ext == True:
        root.destroy()
    else:
        return None

#exit button
exitbtn = Button(root, command=close, text="exit")
exitbtn.place(x=220, y=135)




login = tk.Button(root, text ="Login",
                     command = login)
login.place(x = 105, y = 135, width = 68)



def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    clocklb.config(text=hour + ':' + minute + ':' + second)
    clocklb.after(1000, clock)


clocklb = Label(root, text='', fg='black')
clocklb.place(x=300, y=10)

clock()




mainloop()