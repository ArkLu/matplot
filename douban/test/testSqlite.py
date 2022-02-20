import sqlite3

# ## Create Table
# conn = sqlite3.connect("test.db")
#
# print("Created Test DB ok")
#
# c = conn.cursor()
#
# sql = '''
#         create table company
#             (id int primary key not null,
#             name text not null,
#             age int not null,
#             address char(50),
#             salary real);
#         '''
#
# c.execute(sql)
#
# conn.commit()
#
# conn.close()


###  Insert record
# conn = sqlite3.connect("test.db")
#
# print("Created Test DB ok")
#
# c = conn.cursor()
#
# sql1 = '''
#         insert into company
#             (id,name,age,address,salary)
#         values(1, 'Andy', 28, 'Beijing', 12000.23)
#         '''
#
# sql2 = '''
#         insert into company
#             (id,name,age,address,salary)
#         values(2, 'Benjamin', 38, 'Shanghai', 15000.23)
#         '''
#
# c.execute(sql1)
# c.execute(sql2)
# conn.commit()
#
# conn.close()

# Search Result from database

conn = sqlite3.connect("test.db")

print("to search data from database")

c = conn.cursor()

sql1 = '''
        select  id,name,age,address,salary from company 
        '''

cursor = c.execute(sql1)

# print(cursor)
for row in cursor:
    print("id=", row[0])
    print("name=", row[1])
    print("Age=", row[2])

conn.close()
