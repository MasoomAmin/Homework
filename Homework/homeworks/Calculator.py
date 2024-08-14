from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Caculator")
        self.font = 15

        self.expression = ""
        self.equal_to = False
        self.width = 10
        self.height = 2
        self.bg = "lightblue"
        self.fg = "black"


        self.entry = Entry(self,font=("Times new roman",self.font+10),bg="lightgray",borderwidth=0,fg=self.fg)
        self.entry.grid(row=0,column = 0,columnspan = 5,sticky="ew")

    def clear(self):
        self.entry.delete(0,END)
        self.expression = ""


    def click_button(self,number):
        operators = ["-", "+", "*", "/"]
        self.entry.config(fg="black")
        if self.equal_to == True:
            self.equal_to = False
            self.entry.delete(0, END)
        if len(self.expression) > 0:
            if self.expression[0] == "0":
                self.entry.delete(0,END)
                self.expression = self.expression[0:]



            if number in operators  and self.expression[-1] in operators:
                self.expression = self.expression[:-1] + number
                return True
            first_no = ["*", "/", "."]
            if self.expression[0] in first_no:
                self.expression = self.expression[1:]
                self.entry.delete(0,END)
            if number =="." and self.expression[-1] == ".":
                self.expression = self.expression[:-1]
                return True

        self.entry.insert(END,number)
        self.expression += number

    def equal(self):
        try:
            self.equal_to = True
            self.entry.delete(0,END)
            result = eval(self.expression)
            self.entry.delete(0,END)
            self.entry.insert(END,result)
            self.expression = ""
        except:
            self.entry.config(fg="red")
            self.entry.delete(0,END)
            self.entry.insert(END,"Invalid Expression!")
            self.equal_to = True


    def create_buttons(self,text="",row=0,column=0,column_span=1,command=None,stick=None,type="b"):
        if text == "=":
            button = Button(self,text=f"{text}", width=self.width, height=self.height, command=self.equal,bg=self.bg,font=("Times new roman",self.font))
            button.grid(row=row,column=column)
        elif text == "C":
            button = Button(self,text=f"{text}", width=self.width, height=self.height, command=self.clear,bg=self.bg,font=("Times new roman",self.font))
            button.grid(row=row, column=column,columnspan=column_span,sticky=stick)
        else:
            button = Button(self,text=f"{text}",width=self.width,height=self.height,command=lambda : self.click_button(f"{text}"),bg=self.bg,font=("Times new roman",self.font))
            button.grid(row=row,column=column,columnspan=column_span,sticky=stick)



    def special_buttons(self):
        self.create_buttons("+",row=4,column=4)
        self.create_buttons(text="-",row=3,column=4)
        self.create_buttons(text="*",row=2,column=4)
        self.create_buttons(text="/",row=1,column=4)
        self.create_buttons(text="C",row=1,column=0,column_span=2,stick="ew",command=self.clear)
        self.create_buttons(text=".",row=5,column=4)
        self.create_buttons(text="=",row=1,column=2,stick="ew",command=self.equal)
        self.create_buttons(text="0",row=5,column=0,column_span=3,stick="ew")
        j = 1
        for i in range(2,5):
            b = 0
            for _ in range(3):
                self.create_buttons(f"{j}",row=i,column=b)
                b += 1
                j += 1

a = GUI()
a.special_buttons()
a.mainloop()
