import socket
import threading
import tkinter
import tkinter.scrolledtext
import logging

HOST = "127.0.0.1"
PORT = 9090


class Client:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        if not logging.Logging(self.sock):
            exit()
        msg = tkinter.Tk()
        msg.withdraw()

        self.gui_done = False
        self.running = True

        gui_thread = threading.Thread(target=self.gui_loop)
        gui_thread.start()


    def gui_loop(self):
        self.win = tkinter.Tk()
        self.win.title("Chat")
        self.win.configure(bg="lightgray")

        self.chat_label = tkinter.Label(self.win, text="Chat", bg="lightgray")
        self.chat_label.config(font=("Arial", 12))
        self.chat_label.pack(padx=20, pady=10)

        self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
        self.text_area.pack(padx=20, pady=10)
        self.text_area.config(state='disabled')

        self.msg_label = tkinter.Label(self.win, text="message", bg="lightgray")
        self.msg_label.config(font=("Arial", 12))
        self.msg_label.pack(padx=20, pady=10)

        self.input_area = tkinter.Text(self.win, height=3)
        self.input_area.pack(padx=20, pady=10)

        self.send_button = tkinter.Button(self.win, text="send", command=self.write)
        self.send_button.config(font=("Arial", 12))
        self.send_button.pack(padx=20, pady=10)

        self.gui_done = True
        self.start_receive()
        self.win.protocol("WM_DELETE_WINDOW", self.stop)
        self.win.mainloop()

    def write(self):
        message = f"{self.input_area.get('1.0', 'end')}".encode("utf-8")
        self.sock.send(message)
        self.input_area.delete('1.0', 'end')

    def stop(self):
        self.running = False
        self.win.destroy()
        self.sock.close()
        exit(0)

    def receive(self):
        while self.running:
            try:
                message = self.sock.recv(1024).decode("utf-8")
                if self.gui_done:
                    self.text_area.config(state='normal')
                    self.text_area.insert('end', message)
                    self.text_area.yview('end')
                    self.text_area.config(state="disabled")
            except ConnectionAbortedError:
                break
            except:
                print("error")
                self.sock.close()
                break

    def start_receive(self):
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()


client = Client(HOST, PORT)
