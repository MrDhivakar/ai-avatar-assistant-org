
import sqlite3
import os

db_path = os.path.join("..","database","memory.db")

conn = sqlite3.connect(db_path, check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS chat(
id INTEGER PRIMARY KEY AUTOINCREMENT,
user TEXT,
ai TEXT
)
""")

def save_chat(user, ai):
    cursor.execute(
        "INSERT INTO chat(user, ai) VALUES(?, ?)",
        (user, ai)
    )
    conn.commit()

def get_memory():
    cursor.execute(
        "SELECT user FROM chat ORDER BY id DESC LIMIT 5"
    )
    rows = cursor.fetchall()
    return [r[0] for r in rows]
