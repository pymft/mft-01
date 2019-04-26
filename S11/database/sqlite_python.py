# https://www.tutorialspoint.com/sqlite/sqlite_python.htm

import sqlite3

# pymssql

conn = sqlite3.connect("")

res = conn.execute("""
select * from tracks 
where milliseconds < 5* 60000
""")
print(list(res))
#
# for row in res:
#     print(row)
conn.close()