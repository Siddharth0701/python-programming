import sqlite3
from tkinter import *
conn=sqlite3.connect("studentid.db")

def add():
    conn.execute("create table if not exists students(name varchar(30),course varchar(20),s_rollno integer,date_of_birth integer,gender varchar(20),aadharno integer,s_phoneno integer,address varchar(70));",)
    name=e1.get()
    course=e2.get()
    srollno=int(e3.get())
    dateofbirth=int(e4.get())
    gender=e5.get()
    aadharno=int(e6.get())
    sphoneno=int(e7.get())
    address=e8.get()
    conn.execute("insert into student(name,course,s_rollno,date_of_birth,gender,aadharno,s_phoneno,address) values(?,?,?,?,?,?,?,?);",(name,course,srollno,dateofbirth,gender,aadharno,sphoneno,address))
    print("inserted")
    conn.commit()
def show():
    print("name \t \t",end=" ")
    print("course \t \t",end=" ")
    print("s_rollno \t \t",end=" ")
    print("date_of_birth \t \t",end=" ")
    print(" gender\t \t",end=" ")
    print("aadharno \t \t",end=" ")
    print("S_phonrno \t \t",end=" ")
    print("address \t \t",end=" ")
    for row in cursor:
        print(row[0],end="\t \t")
        print(row[1],end="\t \t")
        print(row[2],end="\t \t")
        print(row[3],end="\t \t")
        print(row[4],end="\t \t")
        print(row[5],end="\t \t")
        print(row[6],end="\t \t")
        print(row[7],end="\t \t")
def close():
    conn.close()
    print("close")
root=Tk()
root.geometry('700x700')
root.title=("Pvg college student records")

e0=Label(root,text="Regestraction Form",width=30,font=("bold",20))
e0.place(x=90,y=53)

        
    
name=Label(root,text="Student name:",font=("bold",18))
name.place(x=80,y=130)
e1=Entry(root,width=30)
e1.place( x=240,y=130)


course=Label(root,text=" Student course:",font=("bold",18))
course.place(x=68,y=180)
e2=Entry(root,width=30)
e2.place(x=240,y=180)

srollno=Label(root,text="Student rollno:",font=("bold",18))
srollno.place(x=70,y=200)
e3=Entry(root,width=30)
e3.place(x=150,y=200)

dateofbirth=Label(root,text="Date of birth :",font=("bold",18))
dateofbirth.place(x=85,y=270)
e4=Entry(root,width=30)
e4.place(x=200,y=270)

gender=Label(root,text="Gender:",font=("bold",18))
gender.place(x=70,y=220)
Radiobutton(root,text="Male", padx=5,value=1).place(x=235,y=220)
Radiobutton(root,text="Female",padx=5,value=2).place(x=290,y=220)


aadharno=Label(root,text="Student Aadharno:",font=("bold",18))
aadharno.place(x=150,y=300)
e6=Entry(root,width=30)
e6.place(x=300,y=300)

sphoneno=Label(root,text="Student phoneno:",font=("bold",18))
srollno.place(x=230,y=350)
e7=Entry(root,width=30)
e7.place(x=240,y=350)

address=Label(root,text="Student address:",font=("bold",18))
srollno.place(x=300,y=400)
e8=Entry(root,width=30)
e8.place(x=360,y=400)




add=Button(root,text ="Add", bg="red", command =add)
add.place(x=500,y=600)


show=Button(root,text ="Show", bg="red", command =show)
show.place(x=530,y=600)

c1=Button(root,text="close",bg="red",command=close)
c1.place(x=570,y=600)

root.mainloop()

   


                 
      
