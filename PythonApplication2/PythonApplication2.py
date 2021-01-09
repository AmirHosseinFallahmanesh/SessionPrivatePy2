from tkinter import *

window = Tk()

window.geometry("200x250")

lbl = Label(window, text="List of Programming Languages")

listbox = Listbox(window)

listbox.insert(1,"Python")

listbox.insert(1, "Java")

listbox.insert(1, "C")



listbox.grid(column=0, row=0)

  
window.mainloop()
