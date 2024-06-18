from tkinter import *
import math
import re

root=Tk()
root.title("Calculator")
root.geometry("400x300")


entry=Entry(root)
entry.grid(row=0, column=0, columnspan=4)
#TODO: Fix edit input
def click(btn):
    text = btn
    if text == "=":
        try:
            expr = entry.get()
            # Replace "^" with "**"
            expr = expr.replace("^", "**")
            # Replace "5!" with "factorial(5)"
            expr = re.sub(r"(\d+)!", r"factorial(\1)", expr)
            # Replace "(2+3)!" with "factorial(2+3)"
            expr = re.sub(r"\(([^)]+)\)!", r"factorial(\1)", expr)
            #TODO:Fix factorial with power

            result = eval(expr, {'__builtins__': None, 'factorial': factorial, 'sin': sin, 'cos': cos, 'tan': tan, 'cot': cot, 'ln': ln, 'sqrt': sqrt})
            entry.delete(0, END)
            entry.insert(END, result)
        except Exception as e:
            entry.delete(0, END)
            entry.insert(END, "Error")
    elif text in ["sin", "cos", "tan", "cot", "ln", "sqrt"]:
        entry.insert(END, text + "(" )
    elif text == "exit":
        root.destroy()
    elif text == "C":
        entry.delete(0, END)
    elif text == "del":
        entry.delete(len(entry.get())-1, END)
    elif text == "pi": #TODO: Fix pi and e input
        entry.insert(END, math.pi) 
    elif text == "e":
        entry.insert(END, math.e)
    else:
        entry.insert(END, text)

def key_press(event):
    if event.char.isdigit() or event.char in ['.', '+', '-', '*', '/', '!', '(', ')','=']:
        click(event.char)
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
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '.', '0', '=', '+',
    '(', ')', 'pi', 'e',
    'ln', 'sqrt', '^',
    'C', '!', 'sin', 'cos', 'tan', 'cot', 'exit', 'del'
] #TODO: Add logo instead of text

i = 0
for btn in buttons:
    def command(btn=btn):
        click(btn)
    Button(root, text=btn, width=10,activebackground='orange', command=command).grid(row=i//4+1, column=i%4)
    i += 1
#TODO: Upgrade style
root.bind('<Key>', key_press)

root.mainloop()
