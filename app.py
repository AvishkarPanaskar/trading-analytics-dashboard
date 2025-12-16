from fastapi import FastAPI, WebSocket
import sqlite3
import json

app = FastAPI()

conn = sqlite3.connect("ticks.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS ticks (
    ts TEXT,
    symbol TEXT,
    price REAL,
    size REAL
)
""")
conn.commit()

@app.websocket("/ws")
async def ws_endpoint(ws: WebSocket):
    await ws.accept()
    while True:
        data = await ws.receive_text()
        tick = json.loads(data)
        cur.execute(
            "INSERT INTO ticks VALUES (?,?,?,?)",
            (tick["ts"], tick["symbol"], tick["price"], tick["size"])
        )
        conn.commit()
