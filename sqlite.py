import sqlite3
conn=sqlite3.connect("mysql.db")
print("sucessful connection")
con=conn.cursor()
con.execute("create table if not exists item (Items_no not null,Item_name varchar(20)not null,Price integer not null,Quantity integer not null);")
print("database created sucessfull! ")


con.execute("insert into item values(101,'Gemoetry',50,100);")
con.execute("insert into item values(102,'Soap',100,50);")
con.execute("insert into item values(103,'Perfume',150,25);")
con.execute("insert into item values(104,'Pen',20,200);")
con.execute("insert into item values(105,'Pencil',20,100);")
conn.commit()
print("insert sucessful")

con.execute("select distinct * from item")
#print(Items_no,"\t", Item_name,"\t", Price,"\t",Quentity,"\n" )
for row in con:

    print(con.fetchall())
   # print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\n")

