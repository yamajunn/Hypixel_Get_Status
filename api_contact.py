import requests
import json
from pprint import pprint

def bedwars_status(name):
    import requests
    import json
    from pprint import pprint

    if type(name) == str:
        
        def getuuid(call):
            r = requests.get(call,timeout=10)
            return r.json()

        def getinfo(call):
            r = requests.get(call,timeout=10)
            return r.json()

        name_link = f"https://api.mojang.com/users/profiles/minecraft/{name}"

        uuid = getuuid(name_link)["id"]

        API_KEY = "a6d34c13-e3f8-423d-b3b0-a59a02ab3d2b"

        uuid_link = f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}"


        # pprint(getinfo(uuid_link))

        if getinfo(uuid_link)["success"] == True:
            data = ""
            dic_list = ['wins_bedwars', 'losses_bedwars', 'final_kills_bedwars', 'final_deaths_bedwars', 'kills_bedwars', 'deaths_bedwars', 'beds_broken_bedwars' , 'beds_lost_bedwars']
            data += "star:" + str(getinfo(uuid_link)["player"]['achievements']['bedwars_level']) + "\n"
            for item in dic_list:
                data += f"{item}:" + str(getinfo(uuid_link)["player"]["stats"]["Bedwars"][item]) + "\n"
        return data
    else:
        return "name error"
    