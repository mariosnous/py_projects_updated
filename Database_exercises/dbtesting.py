import sqlite3
from sqlite3 import Error


import sqlite3
conn = sqlite3.connect('test.db')

def create_database():
    print ("Opened database successfully")
    return conn
    
def create_table(conn):
    conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
    print ("Table created successfully")
    
    conn.close()
    
def insert_db_values(conn):
    """ Here you Enter your data to INSERT data to the db"""
    conn.execute()

    conn.commit()
    print("Records updated ")
    conn.close()

   
create_database()
insert_db_values(conn)



