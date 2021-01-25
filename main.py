from tkinter import *
import mysql.connector
import tkinter as tk
from tkinter import messagebox
from datetime import *
import time
root=Tk()
root.title("Login Page")
root.geometry("450x450")
root.configure(background="yellow")


mydb = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1", database='lifechoicesonline', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

lblfrstrow = tk.Label(root, text ="Username -", )
lblfrstrow.place(x = 50, y = 20)
 
Username = tk.Entry(root, width = 35)
Username.place(x = 150, y = 20, width = 100)
  
lblsecrow = tk.Label(root, text ="Password -")
lblsecrow.place(x = 50, y = 50)
 
password = tk.Entry(root, width = 35)
password.place(x = 150, y = 50, width = 100)








 


  
 


def reguser():
    reguser = Tk()
    reguser.title('Register')
    reguser.geometry('490x230')

     
    def verify():
        try: 
            name_verify = name.get()
            user_verify = Username.get()
            pass_verify = password.get()
            sql= "INSERT INTO Student,  (full_name, username, password) VALUES(%s, %s, %s)"
            valu=(name_verify, user_verify, pass_verify)
            mycursor.execute(sql, valu)
            mydb.commit()
            messagebox.showinfo("message", "Successfully created")
        except ValueError as e:
            print(e)
            messagebox.showinfo("ERROR", "This user already exist")
            reguser.destroy()


    lbname = Label(reguser, text='Full name')
    lbname.place(x=30, y=50)


    name = Entry(reguser, width=30)
    name.place(x=130, y=50)

    lbuser = Label(reguser, text='Username')
    lbuser.place(x=30, y=90)

    Username = Entry(reguser, width=30)
    Username.place(x=130, y=90)
 
    lbpassword = Label(reguser, text='Password')
    lbpassword.place(x=30, y=130)

    password = Entry(reguser, width=30)
    password.place(x=130, y=130)

    student = tk.Button(reguser, text ="Student", 
                        bg ='blue', command = verify)
    student.place(x = 240, y = 195, width = 74)

    


    def verify2():
            try: 
                name_verify = name.get()
                user_verify = Username.get()
                pass_verify = password.get()
                sql= "INSERT INTO Employee  (full_name, username, password) VALUES(%s, %s, %s)"
                valu=(name_verify, user_verify, pass_verify)
                mycursor.execute(sql, valu)
                mydb.commit()
                messagebox.showinfo("message", "Successfully created")
            except ValueError as e:
                print(e)
                messagebox.showinfo("ERROR", "This user already exist")
                reguser.destroy()


    employee = tk.Button(reguser, text ="Employee", 
                        bg ='blue', command = verify2)
    employee.place(x = 130, y = 195, width = 84)




    def verify3():
            try: 
                name_verify = name.get()
                user_verify = Username.get()
                pass_verify = password.get()
                sql= "INSERT INTO Employee  (full_name, username, password) VALUES(%s, %s, %s)"
                valu=(name_verify, user_verify, pass_verify)
                mycursor.execute(sql, valu)
                mydb.commit()
                messagebox.showinfo("message", "Successfully created")
            except ValueError as e:
                print(e)
                messagebox.showinfo("ERROR", "This user already exist")
                reguser.destroy()


    
            try: 
                name_verify = name.get()
                user_verify = Username.get()
                pass_verify = password.get()
                sql= "INSERT INTO Vistors  (full_name, username, password) VALUES(%s, %s, %s)"
                valu=(name_verify, user_verify, pass_verify)
                mycursor.execute(sql, valu)
                mydb.commit()
                messagebox.showinfo("message", "Successfully created")
            except ValueError as e:
                print(e)
                messagebox.showinfo("ERROR", "This user already exist")
                reguser.destroy()


    Visitors = tk.Button(reguser, text ="Visitors", 
                        bg ='blue', command = verify3)
    Visitors.place(x = 350, y = 195, width = 74)



def login():
    user=Username.get()
    pws=password.get()
    sql= "select * from Student where username= %s and password= %s "
    mycursor.execute(sql, [(user),(pws)])
    result = mycursor.fetchall()
    if result:

        messagebox.showinfo('Message', 'Logged in successfully')


def login():
    user=Username.get()
    pws=password.get()
    sql= "select * from Vistors where username= %s and password= %s "
    mycursor.execute(sql, [(user),(pws)])
    result = mycursor.fetchall()
    if result:

        messagebox.showinfo('Message', 'Logged in successfully')





def login():
        user = Username.get()
        pws = password.get()
        sql = "select * from Employee where username= %s and password= %s "
        mycursor.execute(sql, [(user), (pws)])
        result = mycursor.fetchall()
        if result:
            messagebox.showinfo('Message', 'Logged in successfully')

            window = Tk()
            window.title("Sign-in Sign-out")
            window.geometry("250x100")
            signIn = datetime.now()

            x = signIn.strftime("%H:%M:%S")

            def signout():

                timeout = datetime.now()

                y = timeout.strftime("%H:%M:%S")
                z = Username.get()

                timeInfo = z, x, y

                timeComm = "INSERT INTO time_register(username, sign_in, sign_out) VALUES(%s, %s, %s)"

                mycursor.execute(timeComm, timeInfo)

                mydb.commit()
                messagebox.showinfo('Message', 'Signed out!')
                window.destroy()

            outbtn = tk.Button(window, text="Sign-out",
                                  bg='blue', command=signout)
            outbtn.place(x=10, y=10, width=68)


        else:
            messagebox.showinfo("message", "User not found")

def ad():
    if adminbtn:
        root.withdraw()
        import login
        login.login()

            
            

    


login = tk.Button(root, text ="Login", 
                    bg ='blue', command = login)
login.place(x = 165, y = 135, width = 68)


adminbtn = tk.Button(root, text ="Admin", 
                    bg ='blue', command = ad)
adminbtn.place(x = 80, y = 135, width = 68)

        

reg = tk.Button(root, text ="Register", 
                        bg ='blue', command = reguser)
reg.place(x = 250, y = 135, width = 68)





def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    
    clocklb.config(text= hour + ':' + minute + ':' + second)
    clocklb.after(1000, clock)

clocklb = Label(root, text='', fg='black')
clocklb.place(x=300, y=10)


clock()




 


root.mainloop()
