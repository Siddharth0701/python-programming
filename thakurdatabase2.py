import sqlite3
from tkinter import *
conn=sqlite3.connect("record7.db")
def add():
    conn.execute("create table if not exists student (s_rollno integer ,student_name varchar(20),standard varchat(20),div varchar(20));")
    srollno=int(e1.get())
    name=e2.get()
    standard=e3.get()
    div=e4.get()
    conn.execute("insert into student(s_rollno,student_name,standard,div) values(?,?,?,?);", (srollno,name,standard,div))
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

    
def close():
    conn.close()
    print("close")
root=Tk()
root.title("student records")


srollno=Label(root,text="Student Rollno:",font=("bold",18))
srollno.grid(row=0,column=0)
e1=Entry(root,width=30)
e1.grid(row=0,column=1)


name=Label(root,text=" Student Name:",font=("bold",18))
name.grid(row=1,column=0)
e2=Entry(root,width=30)
e2.grid(row=1,column=2)

standard=Label(root,text="Standard:",font=("bold",18))
standard.grid(row=2,column=0)
e3=Entry(root,width=30)
e3.grid(row=2,column=3)

div=Label(root,text="Div :",font=("bold",18))
div.grid(row=3,column=0)
e4=Entry(root,width=30)
e4.grid(row=3,column=4)

add=Button(root,text ="Add", bg="red", command =add)
add.grid(row=4,column=5)


show=Button(root,text ="Show", bg="red", command =show)
show.grid(row=5,column=6)

c1=Button(root,text="close",bg="red",command=close)
c1.grid(row=6,column=7)

root.mainloop()
