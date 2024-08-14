import math
# 1: first question
class Person:
    def __init__(self,name,age):
        self.age = age
        self.name = name
    def greet(self):
        print("Greetings,",self.name)

    def __str__(self):
        return f"{self.name}:{self.age}"

# third question
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def show_details(self):
        print(f"Make: {self.make}, Model: {self.model}, year: {self.year}")


# fourth Question
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def compute(self):
        area = round(math.pi * (self.radius**2),2)
        return area


# Fifth question
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def compute_area(self):
        area = self.width * self.height
        return f"area is: {area}"
    def compute_parameter(self):
        parameter = 2*(self.height + self.width)
        return f"parameter is: {parameter}"