import sqlite3
# connect to database
conn =sqlite3.connect('test.db')

# create a cursor
c = conn.cursor()

# query the Database

c.execute("SELECT rowid, * FROM customers")
#print(c.fetchone())
#c.fetchmany()
#print(c.fetchmany(2))
items = c.fetchall()
for item in items:
    print(item)


# Looping through the DATA
""" items = c.fetchall()
for item in items:
    print(f"{item[0]} -- {item[1]} -- {item[2]}") """




""" many_customers = [
    ('John','Doe','johndoe@gmail.com'),
    ('Andy','Jones','andyjones@gmail.com'),
    ('Jake','Jess','jakejess@gmail.com'),] """
# create a table
# Insert multiple data
""" c.executemany("INSERT INTO customers VALUES (?,?,?)",many_customers) """



print('Query executed successfully')

# DATA TYPE:
# INTEGER
# REAL
# TEXT
# BLOB

#Commit our command
conn.commit()
 
# Close our connection
conn.close()


