import sqlite3
conn=sqlite3.connect("dhoni.db")
print("connected sucessfull")
conn.execute("create table if not exists student10(id not null,name varchar(20)not null,age integer not null,address varchar(20)not null);")
print("database created sucessfull! ")


conn.execute("insert into student10 values(1,'siddharth',18,'Jaunpur');")
conn.execute("insert into student10 values(1,'shailendra',19,'Jaunpur');")
conn.execute("insert into student10 values(2,'shivam',21,'sultanpur');")
conn.execute("insert into student10 values(3,'anurag',22,'azamgarh');")
conn.execute("insert into student10 values(4,'pradeep',23,'sultanpur');")
conn.commit()
print("insert sucessful")

cursor=conn.execute("select * from student10 where age=18;")
for row in cursor:
    print("hello")
    print("id=",row[0])
    print("name=",row[1])
    print("age=",row[2])
    print("address=",row[3])
    
    print("done!")
cursor=conn.execute("select * from student10 where age=19;")
for row in cursor:
    print("hello")
    print("id=",row[0])
    print("name=",row[1])
    print("age=",row[2])
    print("address=",row[3])
    
    print("done!")



