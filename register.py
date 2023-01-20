from tkinter import *
from tkinter import messagebox


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

        self.submit = Button(text="register", command=self.check_data)
        self.submit.pack(padx=20, pady=20)
        self.win.mainloop()

    def check_data(self):
        if self.password.get() != self.password_repeated.get():
            messagebox.showerror(title="Error", message="Passwords are different")


Register()
