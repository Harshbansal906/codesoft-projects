import tkinter as tk

class Calculator:
    def _init_(self, root):
        self.root = root
        self.root.title("🧮 Calculator")
        self.root.geometry("320x430")
        self.root.configure(bg="#f5f5f5")
        self.expression = ""
        
        self.text_input = tk.StringVar()
        
        # Entry widget to show expression/result
        self.entry = tk.Entry(root, textvariable=self.text_input, font=('arial', 22), bd=10, insertwidth=2,
                              width=16, borderwidth=4, relief='sunken', justify='right', bg="white")
        self.entry.grid(row=0, column=0, columnspan=4, pady=10)
        
        # Buttons config
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('=', 5, 0, 4)
        ]
        
        for (text, row, col, colspan) in [(*btn, 1) if len(btn) == 3 else btn for btn in buttons]:
            self.create_button(text, row, col, colspan)
        
    def create_button(self, text, row, col, colspan=1):
        btn_color = "#e0e0e0" if text not in "+-*/=C" else "#d0d0d0"
        button = tk.Button(self.root, text=text, width=7, height=2, font=('arial', 16),
                           bg=btn_color, relief='raised',
                           activebackground="#cccccc",
                           command=lambda: self.button_click(text))
        button.grid(row=row, column=col, columnspan=colspan, padx=4, pady=4)
    
    def button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.text_input.set("")
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.text_input.set(result)
                self.expression = result
            except:
                self.text_input.set("Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.text_input.set(self.expression)

if __name__ == "_main_":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
