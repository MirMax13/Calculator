from tkinter import *
import math

root=Tk()
root.title("Calculator")
root.geometry("400x300")


entry=Entry(root)
entry.grid(row=0, column=0, columnspan=4)

def click(btn):
    text = btn
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, END)
            entry.insert(END, result)
        except Exception as e:
            entry.delete(0, END)
            entry.insert(END, "Error")
    elif text == "C":
        entry.delete(0, END)
    elif text == "!":
        try:
            result = factorial(int(entry.get()))
            entry.delete(0, END)
            entry.insert(END, result)
        except Exception as e:
            entry.delete(0, END)
            entry.insert(END, "Error")
    elif text in ["sin", "cos", "tan", "cot"]:
        try:
            result = getattr(math, text)(float(entry.get()))
            entry.delete(0, END)
            entry.insert(END, result)
        except Exception as e:
            entry.delete(0, END)
            entry.insert(END, "Error")
    elif text == "exit":
        root.destroy()
    elif text == "del":
        entry.delete(len(entry.get())-1, END)
    else:
        entry.insert(END, text)

def key_press(event):
    if event.char.isdigit() or event.char in ['.', '+', '-', '*', '/', '!', '(', ')','=']:
        click(event.char)
    elif event.keysym == "BackSpace":
        click("del")

def factorial(n):
    return math.factorial(n)

def sin(n):
    return math.sin(n)

def cos(n):
    return math.cos(n)

def tan(n):
    return math.tan(n)

def cot(n):
    return 1 / math.tan(n)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '.', '0', '=', '+',
    '(', ')',
    'C', '!', 'sin', 'cos', 'tan', 'cot', 'exit', 'del'
]

i = 0
for btn in buttons:
    def command(btn=btn):
        click(btn)
    Button(root, text=btn, width=10, relief='ridge', activebackground='orange', command=command).grid(row=i//4+1, column=i%4)
    i += 1

root.bind('<Key>', key_press)

root.mainloop()
