from tkinter import *
import tkinter
from tkinter import messagebox as tsmg



root=Tk()
root.geometry("644x244")
root.title("Mneu bar")


def myfunc():
    print("Anything you want to express")

def help():
    print("i will help")
    value=tsmg.askyesno("help","will you help me too")
    if value=="No":
        msg="good you are"
    else:
        msg="fuck off"
    tsmg.showinfo("what",msg)        

mymenu=Menu(root)
m1=Menu(mymenu,tearoff=0)
m1.add_command(label=("tum"),command=myfunc)
m1.add_command(label=("ram"),command=myfunc)
m1.add_separator()
m1.add_command(label=("shyam"),command=myfunc)
m1.add_command(label=("gita"),command=myfunc)
root.config(menu=mymenu)
mymenu.add_cascade(label=("file"),menu=m1)


m2=Menu(mymenu,tearoff=0)
m2.add_command(label=("Quit"),command=help)
m2.add_command(label=("Quit"),command=help)

root.config(menu=mymenu)
mymenu.add_cascade(label=("exit"),menu=m2)


root.mainloop()