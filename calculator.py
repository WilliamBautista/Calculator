import tkinter as tk
from tkinter.messagebox import showerror
from tkinter.constants import RAISED

window = tk.Tk()
window.title("Calculator")
window.geometry("750x500")
window.configure(bg="#FFC0CB")

frame = tk.Frame(master=window, padx=10)
frame.pack()

entry = tk.Entry(master=frame, relief=RAISED, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)

def click(enter):
    entry.insert(tk.END,enter)

def solve():
    try:
        x = str(eval(entry.get()))
        entry.delete(0,tk.END)
        entry.insert(0,x)
    except:
        window.withdraw()
        showerror(title="Error", message="Syntax Error")

def delete():
    entry.delete(0,tk.END)



button1 = tk.Button(
    master = frame,
    text = "1",
    fg = "red",
    bg = "blue",
    height=2,
    width=2,
    command = lambda:
    click(1)
)
button1.grid(row=1, column=0, pady=3)

button2 = tk.Button(
    master = frame,
    text = "2",
    fg = "red",
    bg = "blue",
    height = 2,
    width = 2,
    command = lambda:
    click(2)
)
button2.grid(row=1, column=1, pady=3)

button3 = tk.Button(
    master = frame,
    text = "3",
    fg = "red",
    bg = "blue",
    height = 2,
    width = 2,
    command = lambda:
    click(3)
)
button3.grid(row=1, column=2, pady=3)

button4 = tk.Button(
    master = frame,
    text = "4",
    fg = "red",
    bg = "blue",
    height = 2,
    width = 2,
    command = lambda:
    click(4)
)
button4.grid(row=2, column=0, pady=3)

button5 = tk.Button(
    master = frame,
    text = "5",
    fg = "red",
    bg = "blue",
    height = 2,
    width = 2,
    command = lambda:
    click(5)
)
button5.grid(row=2, column=1, pady=3)

button6 = tk.Button(
    master = frame,
    text = "6",
    fg = "red",
    bg = "blue",
    height = 2,
    width = 2,
    command = lambda:
    click(6)
)
button6.grid(row=2, column=2, pady=3)

button7 = tk.Button(
    master = frame,
    text = "7",
    fg = "red",
    bg = "blue",
    height = 2,
    width = 2,
    command = lambda:
    click(7)
)
button7.grid(row=3, column=0, pady=3)

button8 = tk.Button(
    master = frame,
    text = "8",
    fg = "red",
    bg = "blue",
    height = 2,
    width = 2,
    command = lambda:
    click(8)
)
button8.grid(row=3, column=1, pady=3)

button9 = tk.Button(
    master = frame,
    text = "9",
    fg = "red",
    bg = "blue",
    height = 2,
    width = 2,
    command = lambda:
    click(9)
)
button9.grid(row=3, column=2, pady=3)

button0 = tk.Button(
    master = frame,
    text = "0",
    fg = "red",
    bg = "blue",
    height = 2,
    width = 2,
    command = lambda:
    click(0)
)
button0.grid(row=5, column=1, pady=3)

compile = tk.Button(
    master=frame,
    text="Solve",
    fg="red",
    bg="blue",
    height=2,
    width=2,
    command=solve
)

compile.grid(row=7, column=1, pady=3)

add = tk.Button(
    master = frame,
    text = "+",
    fg = "red",
    bg = "blue",
    height = 2,
    width = 2,
    command = lambda:
    click("+")
)
add.grid(row=6, column=0, pady=3)

sub = tk.Button(
    master = frame,
    text = "-",
    fg = "red",
    bg = "blue",
    height = 2,
    width = 2,
    command = lambda:
    click("-")
)
sub.grid(row=6, column=1, pady=3)

mult = tk.Button(
    master = frame,
    text = "*",
    fg = "red",
    bg = "blue",
    height = 2,
    width = 2,
    command = lambda:
    click("*")
)
mult.grid(row=6, column=2, pady=3)

div = tk.Button(
    master = frame,
    text = "/",
    fg = "red",
    bg = "blue",
    height = 2,
    width = 2,
    command = lambda:
    click("/")
)
div.grid(row=5, column=2, pady=3)

exp = tk.Button(
    master = frame,
    text = "x^2",
    fg = "red",
    bg = "blue",
    height = 2,
    width = 2,
    command = lambda:
    click("**2")
)
exp.grid(row=5, column=0, pady=3)

clear = tk.Button(
    master = frame,
    text = "Clear",
    fg = "red",
    bg = "blue",
    height = 2,
    width = 2,
    command = delete
)
clear.grid(row=7, column=0, pady=3)


window.mainloop()