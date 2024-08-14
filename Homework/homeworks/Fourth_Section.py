# FOURTH QUESTION

# Sixteen Question
class Library:
    def __init__(self,name,*books):
        self.name = name
        self.books = []
        for i in books:
            self.books.append(i)

    def add(self,book):
        self.books.append(book)
        print(f"Books: {self.books}")
    def remove(self,book):
        a = self.books.index(book)
        self.books.pop(a)

    def show(self):
        print(f"Your name: {self.name}\nBooks: {self.books}")

# Seventeen Question

class School:
    def __init__(self,name,*students):
        self.name = name
        self.students = []
        for i in students:
            self.students.append(i)
    def add(self,who):
        self.students.append(who)

    def remove(self,who):
        w = self.students.index(who)
        self.students.pop(w)
    def show(self):
        print(f"Name: {self.name}\nStudents: {self.students}")

# Eighteen Question
class Team:
    def __init__(self,name,*members):
        self.name = name
        self.members = []
        for i in members:
            self.members.append(i)

    def remove(self,who):
        a = self.members.index(who)
        self.members.pop(a)
    def add(self,who):
        self.members.append(who)

    def show(self):
        print(f"Name: {self.name}\nMembers: {self.members}")

# Nineteen Question
class Company:
    def __init__(self,name,*employees):
        self.name = name
        self.employees = []
        for i in employees:
            self.employees.append(i)

    def add(self,who):
        self.employees.append(who)

    def remove(self,who):
        self.employees.remove(who)

    def show(self):
        print(f"Name: {self.name}\nEmployees: {self.employees}")

# Twenty Question
class Zoo:

    def __init__(self,name,*animals):
        self.name = name
        self.animals = []
        for i in animals:
            self.animals.append(i)

    def add(self,who):
        self.animals.append(who)

    def remove(self,who):
        self.animals.remove(who)

    def show(self):
        print(f"Name: {self.name}\nEmployees: {self.animals}")
