# Third Section
# Eleventh Question
class Account:

    def __init__(self,balance):
        self.balance = balance

    def deposite(self,amount):
        self.balance += amount
        print(f"You have deposited ${amount}. you have ${self.balance} in your account")

    def withdraw(self,amount):
        self.balance -= amount
        print(f"You have retrieved ${amount}. you have ${self.balance} in your account")

# 12 question
class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.pages = 0

    def show_book(self):
        print(f"Book: {self.title}\nauthor: {self.author}\npages: {self.pages}")

    def init_book(self,title,author,pages):
        self.pages = pages
        self.author = author
        self.title = title
# thirteen

class Laptop:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def discount(self,percentage):
        self.discount = self.price * percentage
        self.price = self.price - self.discount

    def details(self):
        print(f"You have {self.discount} discount.")
        print(f"Brand: {self.brand}\nModel: {self.model}\nPrice: {self.price}")

# Fourteen Question

class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self,amount):
        print(f"You have deposited: {amount}")
        self.balance += amount
        print(f"Your current amount is {self.balance}")

    def withdraw(self,amount):
        print(f"You have retrieved: {amount}")
        self.balance -= amount
        print(f"Your current amount is {self.balance}")
    def check(self):
        print("Balance: ",self.balance)

# Fifteen
class Student:
    def __init__(self,name,grade,age):
        self.age = age
        self.name = name
        self.grade = grade

    def get(self,what):
        print(f"your {what} is {self.what}")

    def set(self,what,to_what):
        if what == "age":
            self.age = to_what
        if what == "name":
            self.name = to_what
        if what == "grade":
            self.grade = to_what
    def details(self):
        print(f"name: {self.name}\nage: {self.age}\nGrade: {self.grade}\n")

