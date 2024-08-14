# SIXTH QUESTION
# 26 Question
class Ticket:

    def __init__(self,movie_name,seat_name,price):
        self.movie_name = movie_name
        self.seat_name = seat_name
        self.price = price

    def discount(self,amount):
        discount = (self.price * amount)/100
        self.price = self.price - discount
        print(f"You have {amount}% off.")
        print(f"You have received {discount}$ discount, your total price is: {self.price}")

    def shou_details(self):
        print(f"Movie name: {self.movie_name}\nSeat: {self.seat_name}\nPrice: {self.price}")

# 27 Question

class Item:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def __str__(self):
        print(f"Name: {self.name}, Price: {self.price}.")


class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_item(self,item):
        self.items.append(item)
        print(f"{item.name} is added to the shoppingcart.")

    def remove_item(self,item):
        if item not in self.items:
            print("Item doesn't exist.")
            return
        else:
            print(f"{item.name} removed.")
            self.items.remove(item)

    def display_items(self):
        if len(self.items) == 0:
            print("No Items is inside the shopping cart.")
        else:
            total = 0
            print("Items in the cart:")
            for i,values in enumerate(self.items):
                print(f"{i+1}:{values.name}:{values.price}")
                total += values.price
            print(f"The total amount is: {total}")



# 28: Question
class Item:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def __str__(self):
        print(f"Name: {self.name}, Price: {self.price}.")



class Restaurant:
    def __init__(self,name,*menu):
        self.menu = []
        for i in menu:
            self.menu.append(i)

    def add_item(self,item):
        self.menu.append(item)
        print(f"{item.name} added.")

    def remove_item(self,item):
        if item not in self.menu:
            print("Item doesn't exist.")
        else:
            print(f"{item.name} removed.")
            self.menu.remove(item)

    def display(self):
        if len(self.menu) == 0:
            print("Nothing in the menu.")
        else:
            total = 0
            print("The items in the menu:")
            for i,item in enumerate(self.menu):
                print(f"{i+1}:{item.name}: {item.price}.")
                total += item.price
            print(f"The total amount is: {total}.")


# 29 Question
class passenger:
    def __init__(self,name,ticket):
        self.name = name
        self.ticket = ticket
class Flight:

    def __init__(self,flight_number,destination,*passengers):
        self.passenger = []
        for i in passengers:
            self.passenger.append(i)

    def add_pass(self,passe):
        self.passenger.append(passe)
        print(f"{passe.name} Added.")

    def remove_pass(self,passe):
        if passe not in self.passenger:
            print(f"{passe.name} does not exist.")
        else:
            self.passenger.remove(passe)
            print(f"{passe.name} is removed.")
    def display(self):
        if len(self.passenger) == 0:
            print("No passenger.")
        else:
            total = 0
            print("All the passengers:")
            for i,item in enumerate(self.passenger):
                print(f"{i+1}:{item.name}: {item.ticket}.")
                total += item.ticket
            print(f"The total tickets are: {total}.")

# 30 Question
class Room:
    def __init__(self,room_number,is_occupied):
        self.room_number = room_number
        self.is_occupied = is_occupied
class Hotel:

    def __init__(self,name,*rooms):
        self.rooms = []
        for i in rooms:
            self.rooms.append(i)

    def Book(self,room):
        if room in self.rooms:
            if not room.is_occupied:
                room.is_occupied = True
                print(f"You have booked this room {room.room_number}.")
            else:
                print("This room is occupied.")
        else:
            print("This room doesn't exist.")
