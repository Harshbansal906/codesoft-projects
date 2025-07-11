from tkinter import *
import tkinter.messagebox as msg
import random
import string

class PasswordGenerator(Tk):
    def _init_(self):
        super()._init_()
        self.title("Password Generator")
        self.resizable(False, False)

        # Center window
        width, height = 500, 280
        x = (self.winfo_screenwidth() - width) // 2
        y = (self.winfo_screenheight() - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")

        self.choice = StringVar(value="high")
        self._setup_ui()

    def _setup_ui(self):
        # Header
        header = Frame(self, bg="#2b2e30")
        header.pack(fill=X)
        Label(header, text="Password Generator", font=("Helvetica", 23, "bold"),
              fg="#b1ccea", bg="#2b2e30", pady=10).pack()

        # Password length
        length_frame = Frame(self, bg="#e5e7ea", pady=10, padx=20)
        length_frame.pack(fill=X)
        Label(length_frame, text="Set password length:", font=("Helvetica", 16),
              bg="#e5e7ea", fg="#1a0944").pack(side=LEFT)
        self.length_entry = Entry(length_frame, width=5, font=("Helvetica", 13))
        self.length_entry.pack(side=LEFT, padx=10)

        # Password strength
        strength_frame = Frame(self, bg="#e5e7ea", pady=10, padx=20)
        strength_frame.pack(fill=X)
        Label(strength_frame, text="Set password strength:", font=("Helvetica", 16),
              bg="#e5e7ea", fg="#1a0944").pack(anchor=W)

        for level in ("low", "medium", "high"):
            Radiobutton(strength_frame, text=level.capitalize(), value=level,
                        variable=self.choice, font=("Helvetica", 13),
                        bg="#e5e7ea").pack(side=LEFT, padx=20)

        # Generate Button
        button_frame = Frame(self, bg="#e5e7ea", pady=10)
        button_frame.pack(fill=X)
        Button(button_frame, text="GENERATE", bg="#235d48", fg="#e1e6e4",
               font=("Helvetica", 13, "bold"), padx=20, pady=5, bd=0,
               cursor="hand2", command=self._handle_generate).pack()

    def _handle_generate(self):
        try:
            length = int(self.length_entry.get().strip())
            if not 4 <= length <= 80:
                raise ValueError
            strength = self.choice.get()
            password = self._generate_password(length, strength)
            self._show_password(length, strength, password)
        except ValueError:
            msg.showwarning("Invalid Input", "Please enter a valid length between 4 and 80.")

    def _generate_password(self, length, strength):
        base_chars = string.ascii_letters
        digits = string.digits
        symbols = "!@#$%^&*"

        if strength == "low":
            chars = base_chars
        elif strength == "medium":
            chars = base_chars + digits
        else:
            chars = base_chars + digits + symbols

        while True:
            password = ''.join(random.choice(chars) for _ in range(length))
            if strength == "medium" and not any(c.isdigit() for c in password):
                continue
            if strength == "high" and (not any(c.isdigit() for c in password) or not any(c in symbols for c in password)):
                continue
            return password

    def _show_password(self, length, strength, password):
        win = Toplevel(self)
        win.geometry("700x215")
        win.title("Generated Password")

        Label(win, text=f"Generated Password\nLength: {length}   Strength: {strength}",
              font=("Helvetica", 16), fg="#1d3b64", pady=10).pack()

        textbox = Text(win, height=3, width=70, font=("Helvetica", 13),
                       fg="#1d3b64", bg="#e5e7ea", wrap=WORD)
        textbox.insert(END, password)
        textbox.config(state=DISABLED)
        textbox.pack(pady=(0, 10))

        Button(win, text="Close", font=("Helvetica", 13, "bold"), bg="#3c8bdf", fg="white",
               width=13, bd=0, command=win.destroy).pack(side=RIGHT, padx=20, pady=10)

    def run(self):
        self.mainloop()


if __name__ == "_main_":
    PasswordGenerator().run()
