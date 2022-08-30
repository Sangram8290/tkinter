
from tkinter import *
from turtle import left

from PIL import Image, ImageTk 


root = Tk()
root.title("News Paper")
root.geometry("1200x600")

def every_100(text):
    final_text=""
    for i in range(0,len(text)) :
        final_text+=text[i]
        if i%100==0 and i!=0:
            final_text+="\n"
    return final_text
    

texts=[]
photo=[]
for i in range(0,3): 
    with open(f"{i+1}.txt") as f:
     text=f.read()
     texts.append( every_100(text))

image=Image.open(f"{i+1}.jpg")
# TODO:"gfhgvhjnbjhg"
image=image.resize((200,200),Image.ANTIALIAS)
photo.append(ImageTk.PhotoImage(image))


f0=Frame(root,width=800,height=70)
Label(f0,text="Times of India ",fg="black",font=" ITALIC 33 bold").pack()
Label(f0,text="20-1-2022 ",fg="black",font=" ITALIC 13 bold").pack()
f0.pack() 


f1=Frame(root,width=900,height=100,pady=14)
Label(f1,text=texts[0],fg="black",padx=22,pady=22).pack(side="left")
Label(f1,image=photo[0],anchor="e").pack()
f1.pack(anchor="w")

f2=Frame(root,width=900,height=100,pady=14)
Label(f2,text=texts[1],fg="black",padx=22,pady=22).pack(side="right")
Label(f2,image=photo[0],anchor="e").pack()
f2.pack(anchor="w")

f3=Frame(root,width=900,height=100,pady=14)
Label(f3,text=texts[1],fg="black",padx=22,pady=22).pack(side="left")
Label(f3,image=photo[0],anchor="e").pack()
f3.pack(anchor="w")

root.mainloop()