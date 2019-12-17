#(9) Write a sourse code in python to read single and multiple result query  exexuation

import sqlite3
conn=sqlite3.connect("fetch.db")
print("connected sucessfull")
conn.execute("create table if not exists student(Roll_no  integer  not null,Name_name varchar(20)not null,Age integer not null,Address varchar(20) not null);")
print("Table created sucessfull! ")

conn.execute("insert into student values(160,'Siddharth',18,'Jaunpur');")
conn.execute("insert into student values(161,'Shailendra',19,'Jaunpur');")
conn.execute("insert into student values(162,'Anurag',20,'Azamgarh');")
conn.execute("insert into student values(163,'Pradeep',21,'Sultanpur');")
print("Record inserted Sucessfull !")
conn.commit()

cursor=conn.execute("select * from student ;")
singlerecord=cursor.fetchone()
print(singlerecord[1])

multirecord=cursor.fetchmany()
#print(multirecord[])
for row in multirecord:
    print('{0}:{1}'.format(row[0],row[1]))


allrecord=cursor.fetchall()
for row in allrecord:
    print(row[0])
    print(row[1])
    print(row[2])




"""print(cursor.fetchone())

print( cursor.fetchmany(2))

print(cursor.fetchall())"""
conn.close()

