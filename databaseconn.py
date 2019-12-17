import sqlite3
from tkinter import *
conn=sqlite3.connect("information.db")
def add():
    conn.execute("create table if not exists student (s_rollno integer ,student_name varchar(20),standard varchat(20),div varchar(20));")
    srollno=int(e1.get())
    name=e2.get()
    standard=e3.get()
    div=e4.get()
    conn.execute=("insert into student(s_rollno,student_name,standard,di) values(?,?,?,?);", (srollno,name,standard,div))
    print("inserted")
    conn.commit()

def show():
    print("s_rollno \t \t",end="")
    print("student_name \t\t ",end="")
    print("standard \t \t",end="")
    print("div \t \t",end="")
    cursor=conn.execute("select * from student;")
    for row in cursor:
        print(row[0],end="\t \t")
        print(row[1],end="\t \t")
        print(row[2],end="\t \t")
        print(row[3],end="\t \t")
        conn.commit()

    
def close():
    conn.close()
    print("close")
root=Tk()
root.title("student records")


srollno=Label(root,text="Student Rollno:",font=("bold",18))
srollno.place(x=80,y=130)
e1=Entry(root,width=30)
e1.place( x=240,y=130)


name=Label(root,text=" Student Name:",font=("bold",18))
name.place(x=68,y=180)
e2=Entry(root,width=30)
e2.place(x=240,y=180)

standard=Label(root,text="Standard:",font=("bold",18))
standard.place(x=70,y=210)
e3=Entry(root,width=30)
e3.place(x=235,y=230)

div=Label(root,text="Div :",font=("bold",18))
div.place(x=70,y=250)
e4=Entry(root,width=30)
e4.place(x=240,y=255)

add=Button(root,text ="Add", bg="red", command =add)
add.place(x=180,y=380)


show=Button(root,text ="Show", bg="red", command =show)
show.place(x=250,y=390)

c1=Button(root,text="close",bg="red",command=close)
c1.place(x=300,y=400)

root.mainloop()
