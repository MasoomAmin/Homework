from tkinter import *
from tkinter import messagebox
class Login(Tk):
    def __init__(self):
        super().__init__()
        self.login_frame = Frame(self)
        self.sign_frame = Frame(self)
        self.users = {}


    def sign_up(self):
        self.login_frame.pack_forget()
        self.sign_frame.pack()

    def login(self):
        username = self.name_entry.get()
        password = self.pass_entry.get()
        if username in self.users and self.users[username] == password:
            messagebox.showinfo("Login Success",f"Welcome {username}.")
        else:
            messagebox.showerror("Login Failed","Invalid Credentials, please try again.")


    def create_account(self):
        username = self.new_name_entry.get()
        password = self.new_pass_entry.get()
        if username in self.users:
            messagebox.showerror("Error","Name already exist.")
        elif not username or not password:
            messagebox.showerror("Error","Username and password cannot be empty.")
        else:
            messagebox.showinfo("Account Created","Congradualations, your account has been successfully activated.")

        self.users[username] = password



    def show_login(self):
        self.sign_frame.pack_forget()
        self.login_frame.pack()

    def create_forms(self):
        name_label = Label(self.login_frame,text="Username",font=('times new roman',15),width=20,height=2)
        name_label.pack()

        self.name_entry = Entry(self.login_frame,width=40)
        self.name_entry.pack()

        pass_label = Label(self.login_frame,text="Password",font=('times new roman',15),width=18,height=2)
        pass_label.pack()

        self.pass_entry = Entry(self.login_frame,show='*',width=40)
        self.pass_entry.pack()

        button_frame = Frame(self.login_frame)
        button_frame.pack()

        login_button = Button(button_frame,text='Login',command=self.login)
        login_button.pack(pady=10)

        sign_button = Button(button_frame,text='Sign Up',command=self.sign_up)
        sign_button.pack(pady=10)

        # Sign Up form
        name_label = Label(self.sign_frame, text="New Username", font=('times new roman', 15), width=20, height=2)
        name_label.pack()

        self.new_name_entry = Entry(self.sign_frame, width=40)
        self.new_name_entry.pack()

        pass_label = Label(self.sign_frame, text="New Password", font=('times new roman', 15), width=18, height=2)
        pass_label.pack()

        self.new_pass_entry = Entry(self.sign_frame, show='*', width=40)
        self.new_pass_entry.pack()

        button_frame2 = Frame(self.sign_frame)
        button_frame2.pack()

        login_button = Button(button_frame2, text='Create Account',command=self.create_account)
        login_button.pack(pady=10)

        sign_button = Button(button_frame2, text='Back To Login', command=self.show_login)
        sign_button.pack(pady=10)


l = Login()
l.show_login()
l.create_forms()
l.mainloop()