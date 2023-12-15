import tkinter as tk

class Calculatrice:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculatrice")
        self.window.geometry("500x500")
        self.window.resizable(False, False)

        self.entry = tk.Entry(self.window, font=("Arial", 20), bd=5, justify=tk.RIGHT)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        self.create_buttons()

        self.window.bind("<Key>", self.key_press)

    def create_buttons(self):
        row = 1
        col = 0

        for button in self.buttons:
            tk.Button(self.window, text=button, width=6, height=3, font=("Arial", 14, "bold"),
                      command=lambda button=button: self.button_click(button)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

        tk.Button(self.window, text="C", width=6, height=3, font=("Arial", 14, "bold"),
                  command=self.clear_entry).grid(row=row, column=col, padx=5, pady=5)

    def button_click(self, value):
        if value == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Erreur")
        else:
            self.entry.insert(tk.END, value)

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def key_press(self, event):
        key = event.char
        if key in self.buttons:
            self.button_click(key)
        elif key == '\r':
            self.button_click('=')
        elif key == '\x08':
            self.clear_entry()

    def run(self):
        self.window.mainloop()

# Création de l'instance de la classe Calculatrice
#calculatrice = Calculatrice()
#calculatrice.run()