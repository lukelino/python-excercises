#! python3
"""
    szuka pliku
"""

import tkinter as tk
import os


def searchfiles(extension='.txt', folder='D:\\'):
    """insert all files in the listbox"""
    for r, d, f in os.walk(folder):
        for file in f:
            if file.endswith(extension):
                lb.insert(0, r + "\\" + file)


def open_file():
    os.startfile(lb.get(lb.curselection()[0]))


root = tk.Tk()
root.geometry("600x500")
bt = tk.Button(root, text="Search", command=lambda: searchfiles('.txt', 'D:\\'))
bt.pack()
lb = tk.Listbox(root)
lb.pack(fill="both", expand=1)
lb.bind("<Double-Button>", lambda x: open_file())
root.mainloop()
