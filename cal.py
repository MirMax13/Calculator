from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Calculator")
root.geometry("500x500")
entry1=Entry(root)
entry2=Entry(root)
entry1.place(x=50,y=50)
entry2.place(x=100,y=50)
def bth_click1():
    global entry1
    global entry2
    a = int(entry1.get())
    b = int(entry2.get())
    messagebox.showinfo(message=(a+b))
bth=Button(root,text="+",command=bth_click1)
bth.place(x=80,y=100)
root.mainloop()
