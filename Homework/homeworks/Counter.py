from tkinter import *
root = Tk()
root.title("Counter Machine")
root.geometry('600x400')

# Question number 1
counter = 0
class CounterApp:

    def increment(self):
        global counter
        counter += 1
        label.config(text=counter)

    def decrement(self):
        global counter
        if counter <= 1:
            counter = 0
        else:
            counter -= 1
        label.config(text=counter)


app = CounterApp()
# Text Label
label = Label(root,text=counter,font=("Times new roman",40))
# Buttons
increment_button = Button(root,text="INCREMENT",font=("Times New Roman",20),command=app.increment)
decrement_button = Button(root,text="DECREMENT",font=("Times New roman",20),command=app.decrement)
# Packing buttons
increment_button.pack(pady=20)
decrement_button.pack(pady=20)
label.pack()
root.mainloop()