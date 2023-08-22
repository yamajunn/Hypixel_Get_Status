import time
from overlay_status import bedwars_status
import tkinter
from tkinter import messagebox
from overlay_app import overlay_app

def who(s):
    l = s.split("\n")
    who_list = []
    for item in l:
        if item[40:47] == "ONLINE:":
            who_list = item[48:].split(", ")
    return who_list

def update():
    s = f.read()
    who_list = who(s)
    data = ""

    if len(who_list) != 0:
        for name in who_list:
            data += bedwars_status(name)
        label.configure(text=data)

    label.after(1000, update)
    return who_list

path = "/Users/chinq500/Library/Application Support/minecraft/versions/1.8.9/logs/latest.log"
f = open(path)
root = tkinter.Tk()
root.title("my overlay")
root.geometry("480x320")

data = ""
label = tkinter.Label(root, text=time.time())
label.pack(expand=True, anchor=tkinter.NW)
# update()
# root.mainloop()
# label = tkinter.Label(root, text=f"aaa\naaaaaaaa")
# label.pack(expand=True)
# update()
# root.mainloop()
count = 0
while True:
    s = f.read()
    who_ = who(s)
    if len(who_) != 0:
        break

who_list = who_
while True:
    return_who_list = update()
    root.mainloop()
    if who_list != return_who_list and len(return_who_list) != 0:
        who_list = return_who_list
    # time.sleep(1)

# import tkinter as tk
# from tkinter import ttk
# import time

# def update():
#     label.configure(text=time.time())
#     label.after(10, update)

# root = tk.Tk()
# root.title("Digital Clock")
# root.geometry("250x80")


# label = ttk.Label(root, text=time.time())
# label.pack(expand=True)

# label.after(10, update)

# # time.sleep(2)
# root.mainloop()