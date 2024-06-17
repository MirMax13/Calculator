from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Calculator")
root.geometry("500x500")
entry1=Entry(root)
entry2=Entry(root)
entry1.place(x=50,y=50)
entry2.place(x=100,y=50)

def action(entry1,entry2,action):
    a = float(entry1.get())
    b = float(entry2.get())
    if action == '+':
        messagebox.showinfo(message=(a+b))
    elif action == '-':
        messagebox.showinfo(message=(a-b))
    elif action == '*':
        messagebox.showinfo(message=(a*b))
    elif action == '/':
        messagebox.showinfo(message=(a/b))
    elif action == '^':
        messagebox.showinfo(message=(a**b))
    elif action == 'clear':
        entry1.delete(0,END)
        entry2.delete(0,END)
    else:
        messagebox.showinfo(message="Invalid action")

bth=Button(root,text="+",command=lambda: action(entry1, entry2, '+'))
bth.place(x=20,y=100)

bth=Button(root,text="-",command=lambda: action(entry1, entry2, '-'))
bth.place(x=40,y=100)

bth=Button(root,text="*",command=lambda: action(entry1, entry2, '*'))
bth.place(x=60,y=100)

bth=Button(root,text="/",command=lambda: action(entry1, entry2, '/'))
bth.place(x=80,y=100)

bth=Button(root,text="^",command=lambda: action(entry1, entry2, '^'))
bth.place(x=100,y=100)

bth=Button(root,text="Clear",command=lambda:action(entry1, entry2, 'Clear'))
bth.place(x=120,y=100)
root.mainloop()
