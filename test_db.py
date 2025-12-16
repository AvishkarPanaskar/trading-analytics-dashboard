import sqlite3

conn = sqlite3.connect("data/ticks.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM ticks LIMIT 5")
print(cursor.fetchall())
