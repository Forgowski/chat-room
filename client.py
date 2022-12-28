import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back
from tkinter import *

chat = Tk()
chat.config(height=600, width=600, pady=10, padx=10, background="black")
chat.title("Chat room by Forg")
text_box = Text(bg="white", width=20, height=1)
send_button = Button(text="send", )
wall = Canvas(height=300, width=300, background="#b5f0f3")
wall.grid(columnspan=2, row=1, pady=50)
send_button.grid(row=2, column=1)
text_box.grid(row=2, column=0)

init()

colors = \
    [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX,
     Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,
     Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX,
     Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW]

client_color = random.choice(colors)

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5002
separator_token = "<SEP>"

s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST} : {SERVER_PORT}...")
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected")

chat.mainloop()
name = input("Enter your name: ")


def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print('\n' + message)


t = Thread(target=listen_for_messages)
t.daemon = True
t.start()


while True:
    to_send = input()
    if to_send.lower() == 'q':
        break
    data_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    to_send = f"{client_color}[{data_now}] {name}{separator_token}{to_send}{Fore.RESET}"
    s.send(to_send.encode())

s.close()
