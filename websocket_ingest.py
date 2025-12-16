import json
import sqlite3
from datetime import datetime

conn = sqlite3.connect("data/ticks.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ticks (
    ts TEXT,
    symbol TEXT,
    price REAL,
    size REAL
)
""")
conn.commit()

def save_tick(tick):
    cursor.execute(
        "INSERT INTO ticks VALUES (?, ?, ?, ?)",
        (tick["ts"], tick["symbol"], tick["price"], tick["size"])
    )
    conn.commit()
