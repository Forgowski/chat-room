from tkinter import *
from tkinter import messagebox
import register


class Logging:
    def __init__(self):
        self.win = Tk()
        self.win.title("login")
        self.win.configure(bg="lightgray")

        self.l1 = Label(text="Login", bg="lightgray")
        self.l1.pack(padx=20, pady=1)

        self.login = Entry()
        self.login.pack(padx=20, pady=5)

        self.l2 = Label(text="Password", bg="lightgray")
        self.l2.pack(padx=20, pady=1)

        self.password = Entry()
        self.password.pack(padx=20, pady=5)

        self.try_log = Button(text="log in", command=self.log_in)
        self.try_log.pack(padx=20, pady=5)

        self.reg = Button(text="register", command=self.register)
        self.reg.pack(padx=20, pady=5)
        self.win.mainloop()

    def log_in(self):
        pass

    def register(self):
        register.Register(self.win)


Logging()
