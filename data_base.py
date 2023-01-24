import sqlite3
import hashlib
from tkinter import messagebox

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    admin INTEGER(8) NOT NULL
)
""")

def if_used(login):
    if cur.execute("SELECT * FROM userdata WHERE username = ?", (login,)).fetchone() is None:
        return 1
    else:
        messagebox.showerror(title="Error", message="login not available")
        return 0


def register_client(login, password):
    password = hashlib.sha256(password.encode()).hexdigest()
    cur.execute("INSERT INTO userdata (username, password, admin) VALUES (?, ?, ?)", (login, password, 0))
    conn.commit()

def log_in(login, password):
    if cur.execute("SELECT * FROM userdata WHERE username = ?", (login,)).fetchone() is None:
        return 0

    if hashlib.sha256(password.encode()).hexdigest() == cur.execute(
            "select * from (select * from (SELECT password FROM userdata WHERE username = ?))", (login,)).fetchone()[0]:
        return 1
    else:
        return 0


