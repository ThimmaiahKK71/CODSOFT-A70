import tkinter as tk
from tkinter import messagebox

def click(event):
    current = entry.get()
    button_text = event.widget.cget("text")
    
    if button_text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")
            entry.delete(0, tk.END)
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=16, font=("Arial", 24), bd=8, insertwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    'C', '√', 'x^y', '%',
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    '0', '.', '=', '/'
]

row_value = 1
col_value = 0
for button in buttons:
    btn = tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18))
    btn.grid(row=row_value, column=col_value, sticky="nsew")
    btn.bind("<Button-1>", click)
    col_value += 1
    if col_value > 3:
        col_value = 0
        row_value += 1

root.mainloop()
