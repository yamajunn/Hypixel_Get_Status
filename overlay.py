import time
from api_contact import bedwars_status

def who(s):
    l = s.split("\n")
    who_list = []
    for item in l:
        if item[40:47] == "ONLINE:":
            who_list = item[48:].split(", ")
    return who_list

path = "/Users/chinq500/Library/Application Support/minecraft/versions/1.8.9/logs/latest.log"
f = open(path)

while True:
    s = f.read()
    who_list = who(s)
    if len(who_list) != 0:
        for item in who_list:
            data = bedwars_status(item)
            print(data)
    time.sleep(3)