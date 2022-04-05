import sqlite3 as sql

conn = sql.connect("database.db")

conn.execute("CREATE TABLE students (name TEXT, address TEXT, city TEXT, pin TEXT)")

conn.close()

print("Table created successfully")
