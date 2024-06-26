from tkinter import *
import math
import re
from ttkthemes import ThemedTk
from tkinter import ttk

root = ThemedTk(theme="radiance")
root.title("Calculator")
root.geometry("600x300")

del_image = PhotoImage(file="del.png")
del_image = del_image.subsample(20, 20)

entry=ttk.Entry(root, width=50)
entry.grid(row=0, column=0, columnspan=5)
entry.insert(0, "0")
def ignore_click(event):
    return "break"

entry.bind("<Button-1>", ignore_click)
def click(btn):
    text = btn
    if text == "=":
        try:
            expr = entry.get()

            expr = expr.replace(u'\u221A', "sqrt")
            expr = expr.replace("^", "**")

            expr = re.sub(r"(\d+)([πe]|sin|cos|tan|ln|sqrt|\()", r"\1*\2", expr)
            
            # Add multiplication between consecutive "π" or "e"
            expr = re.sub(r"([πe])+", lambda m: '*'.join(m.group(0)), expr)

            # Replace "π" with "math.pi" and "e" with "math.e"
            expr = expr.replace("π", str(math.pi)).replace("e", str(math.e))
            

            # Replace "5**2!" with "factorial(5**2)"
            expr = re.sub(r"(\d+)\*\*(\d+)!", r"factorial((\1)**(\2))", expr)
            # Replace "5**(2+1)!" with "factorial(5**3)"
            expr = re.sub(r"(\d+)\*\*\(([^)]+)\)!", r"factorial((\1)**(\2))", expr)
            # Replace "5!" with "factorial(5)"
            expr = re.sub(r"(\d+)!", r"factorial(\1)", expr)
            # Replace "(2+3)!" with "factorial(2+3)"
            expr = re.sub(r"\(([^)]+)\)!", r"factorial(\1)", expr)

            result = eval(expr, {'__builtins__': None, 'factorial': factorial, 'sin': sin, 'cos': cos, 'tan': tan, 'cot': cot, 'ln': ln, 'sqrt': sqrt})
            entry.delete(0, END)
            entry.insert(END, result)
        except Exception as e:
            entry.delete(0, END)
            entry.insert(END, "Error")
    else:
        if (entry.get() == "Error" or entry.get() == "0" or entry.get() == "0.0") and (text.isdigit() or text in ["sin", "cos", "tan", "cot", "ln", u"\u221A"]):
            entry.delete(0, END)
        if text in ["sin", "cos", "tan", "cot", "ln", u"\u221A"]:
            entry.insert(END, text + "(" )
        elif text == "exit":
            root.destroy()
        elif text == "C":
            entry.delete(0, END)
            entry.insert(0, "0")
        elif text == "del":
            entry_text = entry.get()
            if entry_text.endswith(("sin(", "cos(", "tan(", "cot(", "ln(", u"\u221A(")):
                entry.delete(len(entry_text)-len("sin"), END)
            else:
                entry.delete(len(entry_text)-1, END)
            if entry.get() == "":
                entry.insert(0, "0")
        else:
            entry.insert(END, text)

def key_press(event):
    if event.char.isdigit() or event.char in ['.', '+', '-', '*', '/', '!', '(', ')','=']:
        click(event.char)
    elif event.keysym.lower() == "return":
        click("=")
    elif event.keysym == "BackSpace":
        click("del")

def factorial(n):
    return math.factorial(int(n))

def sin(n):
    return math.sin(n)

def cos(n):
    return math.cos(n)

def tan(n):
    return math.tan(n)

def cot(n):
    return 1 / math.tan(n)

def ln(n):
    return math.log(n)

def sqrt(n):
    return math.sqrt(n)
buttons = [
    '7', '8', '9', 'C', 'del',
    '4', '5', '6', '*', '/',
    '1', '2', '3', '+', '-',
    '.', '0', '=', '(', ')',
    'π', 'e', 'ln', u'\u221A', '^',
    '!', 'sin', 'cos', 'tan', 'cot'
]

i = 0
for btn in buttons:
    def command(btn=btn):
        click(btn)
    if btn == 'del':
        ttk.Button(root, image=del_image, width=10, command=lambda: click("del")).grid(row=i//5+1, column=i%5)
    else:
        ttk.Button(root, text=btn, width=10, command=command).grid(row=i//5+1, column=i%5)
    i += 1
#TODO: Upgrade style
root.bind('<Key>', key_press)

root.mainloop()
