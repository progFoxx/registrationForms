import sqlite3

conn = sqlite3.connect("reg_bd.db", timeout=10)
cur = conn.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS Clients(id INT PRIMARY KEY,name TEXT,surename TEXT,time TEXT);""")

conn.commit()