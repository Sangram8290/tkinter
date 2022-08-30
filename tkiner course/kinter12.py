from tkinter import *
root = Tk()
root.geometry("455x233")
root.title("Scrollbar tutorial")

def upload():
   statusvar.set("Busy") 
   st.update() 
   import time
   time.sleep(3)
   statusvar.set("Ready")




statusvar=StringVar()
statusvar.set("Ready")

st=Label(root,textvariable=statusvar,relief=SUNKEN,anchor="w")
st.pack(side=BOTTOM,fill=X)

Button(root,text="upload",command=upload).pack()


















root.mainloop()
