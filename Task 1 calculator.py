import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Calculator")
        self.master.geometry("450x600")
        self.master.configure(bg='powder blue')

        self.expression = ""
        self.input_text = tk.StringVar()
        
        self.create_widgets()
        
        # Allow resizing
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

    def create_widgets(self):
        # Display frame
        input_frame = tk.Frame(self.master, bg='powder blue')
        input_frame.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # Input field inside the display frame
        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=('arial', 24, 'bold'), fg='black', bg='#eee', bd=10, insertwidth=2, borderwidth=4, justify='right')
        input_field.grid(row=0, column=0, ipadx=20, ipady=20, sticky='nsew')

        # Buttons frame
        button_frame = tk.Frame(self.master, bg='powder blue')
        button_frame.grid(row=1, column=0, sticky='nsew')

        # Define buttons
        numbers = [
            '7', '8', '9',
            '4', '5', '6',
            '1', '2', '3',
            '0', '.'
        ]
        operators = [
            '/', '*',
            '-', '+',
            '√', '^',
            'C', '='
        ]

        # Arrange number buttons in a grid
        row = 0
        col = 0
        for number in numbers:
            self.create_button(number, row, col, button_frame)
            col += 1
            if col > 2:
                col = 0
                row += 1

        # Arrange operator buttons in a 2x4 grid
        row = 0
        col = 3
        for i in range(len(operators)):
            self.create_button(operators[i], row, col, button_frame)
            row += 1
            if row > 3:
                row = 0
                col += 1

        # Allow resizing for input frame and button frame
        input_frame.grid_rowconfigure(0, weight=1)
        input_frame.grid_columnconfigure(0, weight=1)

        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_rowconfigure(i, weight=1)

    def create_button(self, text, row, col, frame):
        button = tk.Button(frame, text=text, font=('arial', 16, 'bold'), fg='black', bg='#ccc', bd=4, relief='raised', command=lambda: self.on_button_click(text), activebackground='#bbb', height=3, width=6)
        button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.input_text.set(self.expression)
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
                self.input_text.set(self.expression)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
                self.expression = ""
        elif char == '√':
            try:
                self.expression = str(math.sqrt(eval(self.expression)))
                self.input_text.set(self.expression)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
                self.expression = ""
        elif char == '^':
            self.expression += '**'
            self.input_text.set(self.expression)
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
