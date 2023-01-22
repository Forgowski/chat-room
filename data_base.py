import sqlite3
import hashlib
from tkinter import messagebox

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")

username1, password1 = "forgowski", hashlib.sha256("password".encode()).hexdigest()

cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
conn.commit()


def if_used(login):
    if cur.execute("SELECT * FROM userdata WHERE username = ?", (login,)).fetchone() is None:
        pass
    else:
        messagebox.showerror(title="Error", message="login not available")


if_used("forgowsk")
