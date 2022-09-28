from cProfile import label
from tkinter import *
import calendar

text = calendar.Calendar(2023)
root = Tk()
root.geometry('500x600')
root.title('CALENDAR')
label1 = label(root, text='CALENDAR')
