import tkinter
from tkinter import messagebox

def overlay_app(data, root):
    label = tkinter.Label(root, text=data)
    label.pack(anchor=tkinter.W)