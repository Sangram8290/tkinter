
from tkinter import *
from turtle import left
from tkinter import messagebox as tmsg 

def any():
    global i

    lbx.insert(ACTIVE,f"{i}")
    i+=1
i=0

root = Tk()
root.title("News Paper")
root.geometry("900x600")

lbx=Listbox(root)
lbx.pack()
lbx.insert(END,"firt item of box")

lbx.delete(first=2,last=4)
Button(root,text="Add item",command=any).pack()

   
root.mainloop()