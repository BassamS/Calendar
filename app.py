from cProfile import label
from tkinter import *
import calendar

text = calendar.Calendar(2023)
root = Tk()
root.geometry('500x600')
root.title('CALENDAR')
label1 = Label(root, text='CALENDAR', bg='dark gray',
               font=('times', 28, 'bold'))
label1.grid(row=1, column=1)
root.config(background='white')
l1 = Label(root, text=text, font='Consoles 10')
