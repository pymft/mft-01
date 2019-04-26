import sqlite3


conn = sqlite3.connect("./new_databse.db")

conn.execute('''CREATE TABLE IF NOT EXISTS Employee
         ( ID INTEGER PRIMARY KEY AUTOINCREMENT,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')

#
# conn.execute('''
# INSERT INTO Employee (NAME,AGE,ADDRESS,SALARY)
# VALUES ('Paul', 32, 'California', 20000.00 )''')

name = "john"
conn.execute("""
UPDATE Employee set NAME = '{name}' WHERE id = 2
""".format(name='John'))

conn.commit()

res = conn.execute('''SELECT * FROM Employee''')
print(list(res))


conn.close()