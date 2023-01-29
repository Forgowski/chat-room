from tkinter import *
from tkinter import messagebox
import register


class Logging:
    def __init__(self, sock):
        self.flag = 1
        self.sock = sock
        self.win = Tk()
        self.win.title("login")
        self.win.configure(bg="lightgray")
        self.nickname = None

        self.l1 = Label(text="Login", bg="lightgray")
        self.l1.pack(padx=20, pady=1)

        self.login = Entry()
        self.login.pack(padx=20, pady=5)

        self.l2 = Label(text="Password", bg="lightgray")
        self.l2.pack(padx=20, pady=1)

        self.password = Entry(show="*")
        self.password.pack(padx=20, pady=5)

        self.try_log = Button(text="log in", command=self.log_in)
        self.try_log.pack(padx=20, pady=5)

        self.reg = Button(text="register", command=self.register)
        self.reg.pack(padx=20, pady=5)
        self.win.mainloop()

    def __del__(self, flag=0):
        return flag

    def log_in(self):
        self.sock.send(f"L {self.login.get()} {self.password.get()}".encode("utf-8"))
        is_ok = self.sock.recv(1024).decode("utf-8")
        if is_ok == "1":
            messagebox.showinfo(title="Hello", message=f"Hi {self.login.get()}")
            self.win.destroy()
            self.__del__(1)
        elif is_ok == '0':
            messagebox.showerror(title="Error", message="Wrong login or password")
        else:
            messagebox.showerror(title="Error", message="Too many mistakes try again later")
            self.win.destroy()
            self.__del__(0)

    def register(self):
        register.Register(self.win, self.sock)
