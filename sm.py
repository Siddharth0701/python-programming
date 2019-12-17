import sqlite3
conn=sqlite3.connect("std.db")
print("database is created")
conn.execute("create table if not exists student( s_id integer, s_name varchar(20),age integer, address varchar(20))")
print("Table is created")



conn.execute("insert into student values( 1, 'Siddharth',18,'Jaunpur')")
conn.execute("insert into student values( 2, 'Singh',    19, 'Mumbai')")


conn.execute("insert into student values( 3, 'Anurag',   20,   'Delhi')")
conn.execute("insert into student values( 4, 'Thakur',   21, 'Patna')")
conn.commit()
cursor=conn.execute( "select distinct * from student")
for row in cursor:
    print( row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\n")


cursor=conn.execute("delete from student where s_id=3 ")
print("Delete is sucessfull !")
   
   
conn.commit()
