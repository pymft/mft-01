import sqlite3


conn = sqlite3.connect("./new_databse.db")

conn.execute('''CREATE TABLE Employee
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')

conn.close()