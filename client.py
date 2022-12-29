import socket
import random
import tkinter.messagebox
from threading import Thread
from datetime import datetime
from colorama import Fore, init
from tkinter import *
from tkinter.simpledialog import askstring

COLORS = \
    [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX,
     Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,
     Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX,
     Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW]

client_color = random.choice(COLORS)


def create_message(message):
    data_now = data_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    to_send = f"{client_color}[{data_now}] {name}{separator_token}{message}{Fore.RESET}"
    return to_send


def send_message():
    message = text_box.get("1.0", END)
    to_send = create_message(message)
    s.send(to_send.encode())


chat = Tk()
chat.config(height=600, width=600, pady=10, padx=10, background="black")
chat.title("Chat room by Forg")
text_box = Text(bg="white", width=20, height=1)
send_button = Button(text="send", command=send_message)
wall = Label(height=20, width=60, background="#b5f0f3", text="Enter your name")
wall.grid(columnspan=2, row=1, pady=50)
send_button.grid(row=2, column=1)
text_box.grid(row=2, column=0)
name = askstring('Name', 'What is your name?')
tkinter.messagebox.showinfo('Hello!', 'Hi, {}'.format(name))


init()


SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5002
separator_token = "<SEP>"

s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST} : {SERVER_PORT}...")
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected")


chat.mainloop()



def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print('\n' + message)


t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

s.close()
