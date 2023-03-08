import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Калькулятор")
        self.master.geometry("300x400")

        # текстовое поле
        self.entry = tk.Entry(self.master, font=("Arial", 16))
        self.entry.pack(padx=10, pady=10)

        # кнопки
        buttons_frame = tk.Frame(self.master)
        buttons_frame.pack()

        # Кнопки цифр и точки
        digits = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0', '.', '+/-']
        row, col = 0, 0
        for digit in digits:
            tk.Button(buttons_frame, text=digit, font=("Arial", 16), width=5, height=2, command=lambda x=digit: self.button_click(x)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 2:
                col = 0
                row += 1

        # Кнопки операций
        operations = ['+', '-', '*', '/', '(', ')', 'C', '=']
        row, col = 0, 3
        for operation in operations:
            tk.Button(buttons_frame, text=operation, font=("Arial", 16), width=5, height=2, command=lambda x=operation: self.button_click(x)).grid(row=row, column=col, padx=5, pady=5)
            row += 1

    def button_click(self, button):
        if button == 'C':
            self.entry.delete(0, tk.END)
        elif button == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, 'Ошибка')
        elif button == '+/-':
            try:
                value = float(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, -1 * value)
            except Exception as e:
                pass
        else:
            self.entry.insert(tk.END, button)

if __name__ == '__main__':
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
