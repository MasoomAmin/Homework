# second Question:
# 6: Sixth question
class Animal:
    def speak(self):
        return f"Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog Speaks"

class Cat(Animal):
    def speak(self):
        return "Cat speaks"

# Seven question
class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self,n):
        self.n = n
    def area(self):
        return f"Area of the square is: {self.n*self.n}"

class Rectangle(Shape):
    def __init__(self,n,m):
        self.n = n
        self.m = m
    def area(self):
        return F"Area of the Rectangle is: {self.m*self.n}"