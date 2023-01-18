import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog

HOST = "127.0.0.1"
PORT = 9090

class Client:
    def __init__(self, host, port):
        self.sock =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        msg = tkinter.Tk()
        msg.withdraw()

        self.nickname = simpledialog.askstring("Nickname ", "choose nickname", parent=msg)
        self.gui_done = False
        self.running = True

        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive)

        gui_thread.start()
        receive_thread.start()

    def gui_loop(self):
        self.win = tkinter.Tk()
        self.win.configure(bg="dark")
        self.chat_label = tkinter.Label(self.win, text="Chat", bg="dark")
        self.chat_label.config(font=("Arial", 12))
        self.chat_label.pack(padx=20, pady=10)

        self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
        self.text_area.pack(padx=20, pady=10)
        self.text_area.config(state='disabled')

        self.msg_label = tkinter.Label(self.win, text="message", bg="dark")
        self.msg_label.config(font=("Arial", 12))
        self.msg_label.pack(padx=20, pady=10)

        self.input_area = tkinter.Text(self.win, height=3)
        self.input_area.pack(padx=20, pady=10)

        self.send_button = tkinter.Button(self.win, text="send", command=self.write())
        self.send_button.config(font=("Arial", 12))
        self.send_button.pack(padx=20, pady=10)

        self.gui_done = True
        self.win.protocol("WM_DELETE_WINDOW", self.stop)
        self.win.mainloop()

    def receive(self):
        pass

