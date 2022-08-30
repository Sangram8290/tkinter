from tkinter import *
 
def harry(event):
    print(f"you clicked {event.x} and {event.y} ")


root = Tk()

root.title("Event handling")

root.geometry("600x600")


A=Button(root,text="click me plese")
A.pack()

A.bind('<Button-1>',harry)
A.bind('<B1-Motion>',quit)
















root.mainloop()