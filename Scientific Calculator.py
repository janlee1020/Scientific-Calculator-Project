#Create a Scientific Calculator

from tkinter import *
from math import *

win = Tk()
win.title("Scientific Calculator")
input = Entry(win, width = 40, fg = "White", bg = "Black")
input.grid(column = 0, row = 0, padx = 5, pady = 5, columnspan = 5)
win.mainloop()
