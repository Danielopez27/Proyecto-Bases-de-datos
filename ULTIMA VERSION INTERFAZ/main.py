import tkinter as tk
from login_window import LoginWindow

class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.app = LoginWindow(self.root)
        self.root.mainloop()

if __name__ == "__main__":
    Main()