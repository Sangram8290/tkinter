from logging import exception
from tkinter import *
from tkinter.messagebox import *
def clear():
    ex=scvalue.get()
    ex=ex[0:len(ex)-1]
    scvalue.delete(0,END)
    scvalue.insert(0,ex)


def allclear():
    scvalue.delete(0,END)
             

def click(event):
    print("clicked")
    b=event.widget
    text1=b['text']
    print(text1)
    
    if text1=="x":
        text1=="*"
        return

    if text1=="=":
        try:     
             ex=scvalue.get()
             ans=eval(ex)
             scvalue.delete(0,END)
             scvalue.insert(0,ans)

        except exception as e:
            print("erorrr...")
            showerror("Error",e)
        return


   






    scvalue.insert(END,text1)


root = Tk()
root.title("MY Calclutor")
root.geometry("680x444")
root.wm_iconbitmap("1.icon.png")
root.configure(background="grey")



l1=Label(root,text="Welcom to my app",font="ITALIC 23 bold ",)
l1.pack(side=TOP,fill=X)


scvalue=Entry(root,font="lucida 25 bold",justify=CENTER)
scvalue.pack(side=TOP,fill=X,padx=12,pady=12)




btnframe=Frame(root)
btnframe.pack(side=TOP)
texts=1
for i in range(0,3):
    for j in range(0,3):
     b=Button(btnframe,text=str(texts),fg="black",font="lucida 25 bold" ,relief=RIDGE,width=8,activebackground="blue",activeforeground="white")
     b.grid(row=i,column=j)
     texts+=1
     b.bind('<Button-1> ', click)






b0=Button(btnframe,text="C",font="lucida 25 bold",relief=RIDGE,width=8,activebackground="blue",activeforeground="white",command=clear)
b0.grid(row=3,column=0)
b.bind('<Button-1> ', click)

b1=Button(btnframe,text="0",font="lucida 25 bold",relief=RIDGE,width=8,activebackground="blue",activeforeground="white")
b1.grid(row=3,column=1)
b.bind('<Button-1> ', click)

b2=Button(btnframe,text="=",font="lucida 25 bold",relief=RIDGE,width=8,activebackground="blue",activeforeground="white")
b2.grid(row=3,column=2)
b2.bind('<Button-1> ', click)


b3=Button(btnframe,text="%",font="lucida 25 bold",relief=RIDGE,width=8,activebackground="blue",activeforeground="white")
b3.grid(row=4,column=0)
b3.bind('<Button-1> ', click)

b4=Button(btnframe,text=".",font="lucida 25 bold",relief=RIDGE,width=8,activebackground="blue",activeforeground="white")
b4.grid(row=4,column=1)
b4.bind('<Button-1> ', click)

b5=Button(btnframe,text="00",font="lucida 25 bold",relief=RIDGE,width=8,activebackground="blue",activeforeground="white")
b5.grid(row=4,column=2)
b5.bind('<Button-1> ', click)

b6=Button(btnframe,text="+",font="lucida 25 bold",relief=RIDGE,width=8,activebackground="blue",activeforeground="white")
b6.grid(row=0,column=3)
b6.bind('<Button-1> ', click)

b7=Button(btnframe,text="-",font="lucida 25 bold",relief=RIDGE,width=8,activebackground="blue",activeforeground="white")
b7.grid(row=1,column=3)
b7.bind('<Button-1> ', click)

b8=Button(btnframe,text="/",font="lucida 25 bold",relief=RIDGE,width=8,activebackground="blue",activeforeground="white")
b8.grid(row=2,column=3)
b8.bind('<Button-1> ', click)
b9=Button(btnframe,text="x",font="lucida 25 bold",relief=RIDGE,width=8,activebackground="blue",activeforeground="white")
b9.grid(row=3,column=3)
b9.bind('<Button-1> ', click)

b10=Button(btnframe,text="Ac",font="lucida 25 bold",relief=RIDGE,width=8,activebackground="blue",activeforeground="white",command=allclear)
b10.grid(row=4,column=3)
# b10.bind('<Button-1> ', click)














































# def display():
 
#     print(f"this wimdow size is ")
#     root.geometry(f"{widvalue.get() }x{heighvalue.get()}")


# root.geometry("455x233")

# wid=Label(root,text="width")
# heigh=Label(root,text="height")


# wid.grid()
# heigh.grid(row=1)


# widvalue=StringVar()
# heighvalue=StringVar()

# widentry=Entry(root,textvariable=widvalue)
# heighentry=Entry(root,textvariable=heighvalue)

# widentry.grid(row=0,column=1)
# heighentry.grid(row=1,column=1)


# Button(root,text="Submit",command=display).grid()





root.mainloop()
