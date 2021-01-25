    
from tkinter import *
import mysql.connector
from datetime import *
from tkinter import ttk






mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                                host='127.0.0.1', database='lifechoicesonline',
                                auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

root = Tk()
root.geometry("700x500")
root.title("admin")
root.configure(background="yellow")

regLb = Label(root, text="Users:")
regLi = Listbox(root, width=60)
tmLb = Label(root, text="Time:")
tmLi = Listbox(root, width=60)

def reg ():
    u = "SELECT * FROM Employee"
    mycursor.execute(u)
    x = mycursor.fetchall()
    for i in x:
        regLi.insert(END, i)


def stud():
    u = "SELECT * FROM Student"
    mycursor.execute(u)
    x = mycursor.fetchall()
    for i in x:
        regLi.insert(END, i)


def visit():
    u = "SELECT * FROM Vistors"
    mycursor.execute(u)
    x = mycursor.fetchall()
    for i in x:
        regLi.insert(END, i)







def times():
    u = "SELECT * FROM time_register"
    mycursor.execute(u)
    x = mycursor.fetchall()
    for i in x:
         tmLi.insert(END, i)


click = ttk.Combobox(root, width=35, value=["Employee", "Student", "Visitors"])
click.place(x=470, y=400, width=100)
btnSh = Button(root, text="Show users", command=reg)
btnSh.place(x=629, y=400, width=100)
btntm = Button(root, text="Show register", command=times)
btntm.place(x=800, y=400, width=100 )
regLb.pack()
regLi.pack()
tmLi.pack()


root.mainloop()