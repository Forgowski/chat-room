from tkinter import *
from tkinter import messagebox
import data_base


class Register:
    def __init__(self):
        self.win = Tk()
        self.win.configure(bg="lightgray")
        self.l1 = Label(text="Login", bg="lightgray")
        self.l1.pack(padx=20, pady=1)

        self.login = Entry()
        self.login.pack(padx=20, pady=5)

        self.l2 = Label(text="Password", bg="lightgray")
        self.l2.pack(padx=20, pady=1)

        self.password = Entry()
        self.password.pack(padx=20, pady=5)

        self.l3 = Label(text="Repeat password", bg="lightgray")
        self.l3.pack(padx=20, pady=1)

        self.password_repeated = Entry()
        self.password_repeated.pack(padx=20, pady=5)

        self.submit = Button(text="register", command=self.try_register)
        self.submit.pack(padx=20, pady=20)
        self.win.mainloop()

    def compare_passwords(self):
        if self.password.get() != self.password_repeated.get():
            messagebox.showerror(title="Error", message="Passwords are different")
            return 0
        else:
            return 1

    def try_register(self):
        if self.compare_passwords():
            if data_base.if_used(self.login.get()):
                data_base.register_client(self.login.get(), self.password.get())
                self.win.destroy()
        else:
            pass

Register()
