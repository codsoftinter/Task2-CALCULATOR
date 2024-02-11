import tkinter as tk

# Function to update the entry field
def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(symbol))

# Function to perform the calculation
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry field for input and display
entry = tk.Entry(root, width=20, font=('Arial', 16), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons for numbers and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Create buttons and add them to the grid
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 16), command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

# Clear button
clear_button = tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 16), command=clear)
clear_button.grid(row=5, column=0, columnspan=3)

# Exit button
exit_button = tk.Button(root, text='Exit', padx=20, pady=20, font=('Arial', 16), command=root.destroy)
exit_button.grid(row=5, column=3)

# '=' button
equal_button = tk.Button(root, text='=', padx=20, pady=20, font=('Arial', 16), command=calculate)
equal_button.grid(row=4, column=3)

# Run the Tkinter event loop
root.mainloop()
