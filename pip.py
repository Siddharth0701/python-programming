import mysql.connector
print("sucessfull connection")
conn=mysql.connector.connect(host="localhost",user="siddharth",passwd="singh", database="singh" )
con=conn.cursor()


"""mycursor=conn.cursor()
print("S_id \t  S_name \t  Age \t  Address \n ")
mycursor.execute("select * from student")
for row in mycursor:
    print(row[0], "\t" ,row[1], "\t", row[2], "\t", row[3], "\n")
"""

"""c=cur.execute("create table employee( emp_id integer,emp_name varchar(20),address varchar(30))")
cur.execute("select * from student")
for row in cur:
    #print(row[0],row[1],row[2],row[3])
print("table is created")

"""



con.execute("create table student2( stud_id integer,name_name varchar(20),address1 varchar(30))")
print("Table is created")

