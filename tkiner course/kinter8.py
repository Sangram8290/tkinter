
from tkinter import *
from turtle import left
from tkinter import messagebox as tmsg 


root = Tk()
root.title("News Paper")
root.geometry("900x600")


def any():
    print("Thanks ")
    tmsg.showinfo("Hotel review",f"You rate us {myslider.get()} star")
    with open("record1.txt","a") as f:
        f.write(f"You Rrate us {myslider.get()} star\n")

Label(root,text="Thanks for orderring food",fg="blue",font="ITALIC 23 bold").pack()
Label(root,text="Plese rate us from 0 - 10 ",fg="black",font="ITALIC 10 bold").pack()
myslider=Scale(root,from_=0,to=10,length=150,orient=HORIZONTAL,tickinterval=2)
myslider.set(4)
myslider.pack()


Button(root,text="Sbmit",fg="red",command=any).pack()



















root,mainloop()