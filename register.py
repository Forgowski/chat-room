from tkinter import *


class Register:
    def __init__(self):
        self.win = Tk()
        self.win.configure(bg="lightgray")
        self.l1 = Label(text="Login", bg="lightgray")
        self.l1.pack()

        self.login = Entry()
        self.login.pack()

        self.l2 = Label(text="Password", bg="lightgray")
        self.l2.pack()

        self.password = Entry()
        self.password.pack()

        self.l3 = Label(text="Repeat password", bg="lightgray")
        self.l3.pack()

        self.password_repeated = Entry()
        self.password_repeated.pack()

        self.win.mainloop()


Register()
