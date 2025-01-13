from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def time():
    String = strftime('%H:%M:%S %p')
    label.config(text=String)
    label.after(1000,time)

label = Label(root,font=("ds_digital",80),background="black",foreground="cyan")
label.pack(anchor='center')
time()

mainloop()