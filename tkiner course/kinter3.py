from tkinter import *
from PIL import Image, ImageTk 

root= Tk()
root.title("XXX Dance classes")


def getvals():
    print(f"{namevalue.get()},{phonevalue.get()},{gendervalue.get()},{emergencyvalue.get()},{paymentmodevalue.get()},{foodservicevalue.get()}")
    with open("A.txt","a") as f:
        f.write(f"{namevalue.get()},{phonevalue.get()},{gendervalue.get()},{emergencyvalue.get()},{paymentmodevalue.get()},{foodservicevalue.get()} \n")

root.geometry("644x344")
#Heading
Label(root, text="Welcome to Harry Travels", font="comicsansms 13 bold", pady=15).grid(row=0,padx=22,pady=12, column=7)



image=Image.open("1.jpg")
# TODO:"gfhgvhjnbjhg"
image=image.resize((70,80),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)


#Text for our form
name = Label(root, text="Name12")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency Contact")
paymentmode = Label(root, text="Payment Mode")

#Pack text for our form
name.grid(row=1,padx=22,pady=12, column=5)
phone.grid(row=2, padx=22,pady=12,column=5)
gender.grid(row=3,padx=22,pady=12, column=5)
emergency.grid(row=4,padx=22,pady=12, column=5)
paymentmode.grid(row=5,padx=22,pady=12, column=5)

# Tkinter variable for storing entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()


#Entries for our form
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentmodeentry = Entry(root, textvariable=paymentmodevalue)

# Packing the Entries
nameentry.grid(row=1, padx=22,pady=12,column=7)
phoneentry.grid(row=2,padx=22,pady=12, column=7)
genderentry.grid(row=3, padx=22,pady=12,column=7)
emergencyentry.grid(row=4,padx=22,pady=12, column=7)
paymentmodeentry.grid(row=5, padx=22,pady=12,column=7)

#Checkbox & Packing it
foodservice = Checkbutton(text="Want to prebook your meals?", variable = foodservicevalue)
foodservice.grid(row=6, padx=22,pady=22,column=7)

#Button & packing it and assigning it a command
Button(text="Jai mharana prtap",fg="red",font="ITALIC 12 bold",command=getvals).grid(padx=22,pady=22,row=7, column=7)
Button(image=photo,command=getvals).grid(padx=22,pady=22,row=8, column=7)


root.mainloop()
