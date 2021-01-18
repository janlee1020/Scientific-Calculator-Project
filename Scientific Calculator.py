#Create a Scientific Calculator

from tkinter import *
from math import *

win = Tk()
win.title("Scientific Calculator")
input = Entry(win, width = 40, fg = "White", bg = "Black")
input.grid(column = 0, row = 0, padx = 5, pady = 5, columnspan = 5)

def clear():
    input.delete(0, END)

def stringtoAnswer():
    result = input.get()
    result = eval(result)
    input.delete(0, END)
    input.insert(0, result)


log = Button(win, )
win.mainloop()
