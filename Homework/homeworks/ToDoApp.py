from tkinter import *
from tkinter import  messagebox
# ToDo App
class todoApp(Tk):
    def __init__(self):
        super().__init__()

    def Add_task(self):
        task = self.entry.get()
        if task:
            self.list_box.insert(END,task)
            self.entry.delete(0,END)
        else:
            messagebox.showwarning("Warning","you have to write something")

    def remove(self):
        selected = self.list_box.curselection()
        if selected:
            self.list_box.delete(END,selected)
        else:
            messagebox.showwarning('Warning',"Select before deleting!")

    def clear(self):
        self.list_box.delete(0,END)
    def create(self):
        self.above_frame = Frame(self)
        self.above_frame.pack(pady=10)

        self.entry = Entry(self.above_frame,width=40)
        self.entry.pack(side=LEFT,padx=10)

        self.list_box = Listbox(self,width=50,height=10)
        self.list_box.pack(pady=10)

        self.add_button = Button(self.above_frame,text="Add Task",command=self.Add_task)
        self.add_button.pack(side=LEFT)

        self.button_frame = Frame(self)
        self.button_frame.pack()

        self.remove_button = Button(self.button_frame,text="Remove Task",command=self.remove)
        self.remove_button.pack(side=LEFT,padx=10,pady=10)

        self.clear_button = Button(self.button_frame,text="Clear All",command=self.clear)
        self.clear_button.pack(side=LEFT)

to = todoApp()
to.create()
to.mainloop()

