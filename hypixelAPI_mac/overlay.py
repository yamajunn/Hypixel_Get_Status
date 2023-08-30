import time
from overlay_status import bedwars_status
import tkinter
from tkinter import messagebox
from overlay_app import overlay_app
import json
#[01:02:03] [Client thread/INFO]: [CHAT] ONLINE: 2chanfy, Starcity200415, Cwaminator, A_miton, YaBoyNOOBI


def who(s):
    l = s.split("\n")
    who_list = []
    for item in l:
        if item[40:47] == "ONLINE:":
            who_list = item[48:].split(", ")
    return who_list

def save_who(who_list, data_dic):
    with open("save_who_list.json") as j:
            j_update = json.load(j)
            j_update["who_list"] = who_list
            j_update["player_data"] = data_dic
    with open("save_who_list.json", "w") as j:
        json.dump(j_update, j)

def read_who():
    with open("save_who_list.json") as f:
        load_f = json.load(f)
    return load_f



path = "/Users/chinq500/Library/Application Support/minecraft/versions/1.8.9/logs/latest.log"
f = open(path)

root = tkinter.Tk()
root.title("my overlay")
root.geometry("480x320")

data = ""
label = tkinter.Label(root, text="none data")
label.pack(expand=True, anchor=tkinter.NW)
# update()
# root.mainloop()
# label = tkinter.Label(root, text=f"aaa\naaaaaaaa")
# label.pack(expand=True)
# update()
# root.mainloop()

def update():
    s = f.read()
    who_list = who(s)
    if len(who_list) != 0:
        data = ""
        data_dic = {}
        read_dic = read_who()
        dont_read_list = list(set(who_list) & set(read_dic["who_list"]))
        for name in who_list:
            if not name in dont_read_list:
                get_data = bedwars_status(name)
                data += get_data
                data_dic[name] = get_data
            else:
                data += read_dic["player_data"][name]
                data_dic[name] = read_dic["player_data"][name]
        save_who(who_list, data_dic)
        label.configure(text=data)
    label.after(1000, update)

update()
root.mainloop()