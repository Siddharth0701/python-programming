"""import sqlite3
conn=sqlite3.connect("singh")
#cur=conn.cursor();
conn.execute("create table pqr(id integer,name varchar(20))")
conn.execute("insert into pqr values(10,'siddharth')" )
cur=conn.execute select* from abc
for row in cursor  :
    print(cursor)
    print(row0)
    print(row1)
conn.close()

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="siddharth",password="singh")
"""
import sqlite3
conn=sqlite3.connect("singh")
print("connected")
cursor=conn.execute( "show databases")#"select * from customer;")
for i in cursor: 
                     print(i)
"""for row in cursor:
    print("id=",row[0])
    print("name=",row[1])
    print("age=",row[2])
    print("address=",row[3])
print("done !")
conn.close()"""
"""conn.execute("create table customer (id integer,name varchar(20),age integer,address varchar(20))")
conn.cxecute("insert into customer (101,'singh'18,'thane')")
cursor =conn.execute select * from customer
"""
"""cursor.execute("show databases")
for i in cursor :
    print(i)
    
"""
import sqlite3
conn=sqlite3.connect("text.db")
