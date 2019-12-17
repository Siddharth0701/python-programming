from tkinter import *
import sqlite3
root=Tk()
#root.geometry('500 x 500')
root.title('regestation form')
fullname =StringVar()
email=StringVar()
var=IntVar()
#c=Stringvar()
#var1= intvar()
def database():
    name1= fullname.get()
    email=email.get()
    gender=var.get()
    #count=c.get()
conn=sqlite3.connect("form.db")
    with conn:
        cursor=conn.cursor()

    cursor.execute('create table if not exists student (fullname text,email text,gender text ) ')
    cursor.execute('insert table student (fullname, email, gender ) values(?,?,?) ',(name1,gamil ,gender ,))
    conn.commit()

label_0=Label(root,text="registration form ",width=20)
label_0.place(x=90,y=50)

label_1=Label(root,text="fullname ",width=20)
label_1.place(x=80,y=130)
entry_1=Entry(root,textvar=fullname)
entry_1.place(x=240,y=130)

label_2=Label(root,text="email ",width=20)
label_2.place(x=68,y=180)

entry_2=Entry(root,textvar=email)
entry_2.place(x=240,y=180)

label_3=Label(root,text="gender ",width=20)
label_3.place(x=70,y=230)

Radiobutton(root,text="male", variable=var,value =1).place(x=235,y=230)

Radiobutton(root,text="female",variable=var, value =2).place(x=290,y=230)

Button(root,text="submit",width=20 ,bg='brown',fg='white',command=database).place(x=170,y=330)

root.mainloop()







