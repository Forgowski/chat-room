import tkinter
from tkinter import *
from tkinter import messagebox

class Register(tkinter.Toplevel):
    def __init__(self, root, sock):
        self.sock = sock
        super().__init__(root)
        self.geometry("300x250")
        self.title("registration")
        self.configure(bg="lightgray")
        self.l1 = Label(self, text="Login", bg="lightgray")
        self.l1.pack(padx=20, pady=1)

        self.login = Entry(self)
        self.login.pack(padx=20, pady=5)

        self.l2 = Label(self, text="Password", bg="lightgray")
        self.l2.pack(padx=20, pady=1)

        self.password = Entry(self, show="*")
        self.password.pack(padx=20, pady=5)

        self.l3 = Label(self, text="Repeat password", bg="lightgray")
        self.l3.pack(padx=20, pady=1)

        self.password_repeated = Entry(self, show="*")
        self.password_repeated.pack(padx=20, pady=5)

        self.submit = Button(self, text="register", command=self.try_register)
        self.submit.pack(padx=20, pady=20)
        self.mainloop()

    def compare_passwords(self):
        if self.password.get() != self.password_repeated.get():
            messagebox.showerror(title="Error", message="Passwords are different")
            return 0
        else:
            return 1

    def try_register(self):
        if self.compare_passwords():
            try:
                self.sock.send(f"R {self.login.get()} {self.password.get()}".encode("utf-8"))
                recv = self.sock.recv(1024).decode("utf-8")
                if recv == "1":
                    messagebox.showinfo(title="Well done", message="registered successfully")
                    self.destroy()
                elif recv == '0':
                    messagebox.showerror(title="Error", message="This login is unavailable")

            except:
                print("cos nie tak")
