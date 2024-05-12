import tkinter as tk
import math

class ScientificCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Scientific Calculator")
        self.geometry("300x400")

        self.expression = ""

        self.create_widgets()

    def create_widgets(self):
        # Entry widget to display the expression
        self.entry = tk.Entry(self, font=('Arial', 14))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

        # Buttons for numbers and operations
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("sin", 5, 0), ("cos", 5, 1), ("tan", 5, 2), ("^", 5, 3),
            ("sqrt", 6, 0), ("(", 6, 1), (")", 6, 2), ("C", 6, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self, text=text, font=('Arial', 14), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10)

    def on_button_click(self, text):
        if text == "=":
            try:
                result = eval(self.expression)
                self.expression = str(result)
            except Exception as e:
                self.expression = "Error"
        elif text == "C":
            self.expression = ""
        else:
            self.expression += text

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

if __name__ == "__main__":
    app = ScientificCalculator()
    app.mainloop()
