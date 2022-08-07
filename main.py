import pyodbc 

# connection string
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=127.0.0.1,1433;'
                      'Database=myDB;'
                      'UID=morteza;'
                      'PWD=morteza1365;'
                      )

# read data ----------------
def read(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM product')
    for i in cursor:
        print(f'row = {i}')
read(conn)

# update data ----------------
#name=input("enter name product: ")
def update(conn,name):
    cursor = conn.cursor()
    cursor.execute('update product set name=? where id=?',(name, 2))
    conn.commit()
    print("update")
    read(conn)
#update(conn,name)

# create ----------------
# add=input("enter name product: ")
def create(conn,add):
    cursor = conn.cursor()
    cursor.execute('insert into product(name) values(?);',(add))
    conn.commit()
    print("inserted!!")
    read(conn)
# create(conn,add)

# delete ----------------
product_name=input("enter name product: ")# or id 
def delete(conn,product_name):
    cursor = conn.cursor()
    cursor.execute('delete from product where name = ?;',(product_name))
    conn.commit()
    print("deleted pekh pekh!!")
    read(conn)
delete(conn,product_name)

conn.close()