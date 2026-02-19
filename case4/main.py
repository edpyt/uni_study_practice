# pyright: basic

import tkinter as tk
from tkinter import ttk

DEFAULT_FONT = "Arial"


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Кейс-задача №4")
        self.root.geometry("450x400")
        self.root.resizable(False, False)

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.bg_color = "#2c3e50"
        self.fg_color = "#ecf0f1"
        self.button_color = "#3498db"
        self.button_active = "#2980b9"
        self.result_bg = "#34495e"

        self.root.configure(bg=self.bg_color)

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(
            self.root,
            text="Калькулятор",
            font=(DEFAULT_FONT, 20, "bold"),
            bg=self.bg_color,
            fg=self.fg_color,
        )
        title_label.pack(pady=20)

        input_frame = tk.Frame(self.root, bg=self.bg_color)
        input_frame.pack(pady=10)

        tk.Label(
            input_frame,
            text="число 1:",
            font=(DEFAULT_FONT, 12),
            bg=self.bg_color,
            fg=self.fg_color,
        ).grid(row=0, column=0, padx=10, pady=5)

        self.num1_entry = tk.Entry(
            input_frame,
            font=(DEFAULT_FONT, 12),
            width=15,
            bg="white",
            fg="black",
            relief=tk.FLAT,
            bd=5,
        )
        self.num1_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(
            input_frame,
            text="число 2:",
            font=(DEFAULT_FONT, 12),
            bg=self.bg_color,
            fg=self.fg_color,
        ).grid(row=1, column=0, padx=10, pady=5)

        self.num2_entry = tk.Entry(
            input_frame,
            font=(DEFAULT_FONT, 12),
            width=15,
            bg="white",
            fg="black",
            relief=tk.FLAT,
            bd=5,
        )
        self.num2_entry.grid(row=1, column=1, padx=10, pady=5)

        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(pady=20)

        operations = [
            ("сумма", self.add),
            ("разность", self.subtract),
            ("произведение", self.multiply),
            ("деление", self.divide),
        ]

        for i, (text, command) in enumerate(operations):
            btn = tk.Button(
                button_frame,
                text=text,
                command=command,
                font=(DEFAULT_FONT, 11, "bold"),
                bg=self.button_color,
                fg="white",
                activebackground=self.button_active,
                activeforeground="white",
                relief=tk.FLAT,
                bd=0,
                padx=20,
                pady=10,
                cursor="hand2",
            )
            btn.grid(row=0, column=i, padx=5)

            btn.bind("<Enter>", lambda e, b=btn: b.configure(bg=self.button_active))
            btn.bind("<Leave>", lambda e, b=btn: b.configure(bg=self.button_color))

        result_frame = tk.Frame(self.root, bg=self.bg_color)
        result_frame.pack(pady=20)

        tk.Label(
            result_frame,
            text="результат:",
            font=(DEFAULT_FONT, 14, "bold"),
            bg=self.bg_color,
            fg=self.fg_color,
        ).pack()

        self.result_label = tk.Label(
            result_frame,
            text="0",
            font=(DEFAULT_FONT, 18, "bold"),
            bg=self.result_bg,
            fg=self.fg_color,
            width=20,
            height=2,
            relief=tk.FLAT,
            bd=5,
        )
        self.result_label.pack(pady=10)

        self.num1_entry.bind("<Return>", lambda e: self.num2_entry.focus())
        self.num2_entry.bind("<Return>", lambda e: self.add())

    def get_numbers(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            return num1, num2
        except ValueError:
            self.show_error("Ошибка: введите числа!")
            return None, None

    def show_error(self, message):
        self.result_label.config(text=message, fg="#e74c3c")
        self.root.after(2000, lambda: self.result_label.config(fg=self.fg_color))

    def show_result(self, result):
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        self.result_label.config(text=str(result))

    def add(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            self.show_result(num1 + num2)

    def subtract(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            self.show_result(num1 - num2)

    def multiply(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            self.show_result(num1 * num2)

    def divide(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            if num2 == 0:
                self.show_error("Ошибка: деление на ноль!")
            else:
                self.show_result(num1 / num2)


def main():
    root = tk.Tk()
    _app = CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

