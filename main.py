#!/usr/bin/env python3

import tkinter as tk
from login import Login

class Main(tk.Tk):
    def __init__(self, **kwargs):
        tk.Tk.__init__(self, **kwargs)
        self.geometry("500x500+0+0")
        self.resizable(False, False)

        b = Login(self)
        b.pack(fill=tk.BOTH, expand=True)

def main():
    root = Main() # the window!
    root.mainloop()

if __name__ == "__main__":
    main()

