from tkinter import *
from time import *

def update(): 
    time_string = strftime('%H:%M:%S %p') 
    time_label.config(text=time_string)
    window.after(1000,update)
window = Tk()
time_label = Label(window,font=("Arial",100),fg="red",bg="black")
time_label.pack()
update()

window.mainloop()
