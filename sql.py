from operator import index
import sqlite3
import pandas as pd
from sqlalchemy import false

# try:
#     connection=sqlite3.connect('D://testDB.db')
#     print("opened db successfully")
# except:
#     print("error")

# results=connection.execute("select *from customers")
# for row in results:
#     print(row)

# connection.close()


# command1="""create table if not exists stores(store_id integer primary key,location text)"""
# connection.execute(command1)
# results=connection.execute("select *from stores")
# for row in results:
#  print(row)



# cursor=connection.cursor()

# command1="""create table if not exists stores(store_id integer primary key,location text)"""
# cursor.execute(command1)

# command2="""create table if not exists purchases(purchase_id integer primary key,store_id integer,total_cost float,foreign key(store_id) references stores(store_id))"""
# cursor.execute(command2)

# cursor.execute("insert into stores values(21,'Italy')")
# cursor.execute("insert into stores values(22,'Russia')")
# cursor.execute("insert into stores values(23,'India')")

# cursor.execute("insert into purchases values(31,21,13.9)")
# cursor.execute("insert into purchases values(32,23,19.9)")













db=sqlite3.connect('D://testDB.db')
cur=db.cursor()
# cur.execute('''create table if not exists student(id integer primary key,name text not null,address text not null);''' )

# cur.execute('''insert into purchases values(32,22,99.5)''')

# cust_list=[(4,'kavya','malpe','udupi'),
#            (5,'ashwitha','kundapura','udupi'),
#            (6,'lachmi','kateel','mangalore'),
#            (7,'vinu','hejmadi','udupi')

# ]

# cur.executemany("insert into Customers (CID,Cname,Address,City) values(?,?,?,?)",cust_list)
# cur.execute('select *from Customers')
# print(cur.fetchall())
# db.commit()
# db.close()


cur.execute("select *from Customers")
for x in cur.fetchall():
    print(x)
db.commit()
# db.close()



# data=pd.read_sql_query('select *from Customers',db)
# print(data)

# new_row={'CID':8,'Cname':'yashu','Address':'surathkal','City':'Mangalore'}
# data=data.append(new_row,ignore_index=True)
# print(data)

# data.to_sql('Customers',db,if_exists='replace',index=False)




