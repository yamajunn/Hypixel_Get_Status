import requests
from pprint import pprint

def getuuid(call):
    r = requests.get(call,timeout=10)
    return r.json()

name = "A_miton"
name_link = f"https://api.mojang.com/users/profiles/minecraft/{name}"
uuid = getuuid(name_link)["id"]

API_KEY = ""
url = f"https://api.hypixel.net/resources/achievements?key={API_KEY}&uuid={uuid}"

response = requests.get(url)
data = response.json()

# レスポンスから同じゲーム内のプレイヤー情報を取得
active_players = data

pprint(active_players)
