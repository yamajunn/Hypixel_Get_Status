import requests
# from pprint import pprint

def bedwars_status(name):
    try:
        def getuuid(call):
            r = requests.get(call,timeout=10)
            return r.json()

        def getinfo(call):
            r = requests.get(call,timeout=10)
            return r.json()

        name_link = f"https://api.mojang.com/users/profiles/minecraft/{name}"
        uuid = getuuid(name_link)["id"]
        API_KEY = "4eaa90b7-e9c2-4ea9-990e-6b4cf0b5853f"
        uuid_link = f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}"

        data_dic = getinfo(uuid_link)
        # print(data_dic)
        data_list = []
        data = ""
        if data_dic["success"] == True:
            if data_dic["player"] != None:
                dic_list = ['wins_bedwars', 
                            'losses_bedwars', 
                            'final_kills_bedwars', 
                            'final_deaths_bedwars', 
                            'kills_bedwars', 
                            'deaths_bedwars', 
                            'beds_broken_bedwars' , 
                            'beds_lost_bedwars'
                            ]
                
                data_list.append(data_dic["player"]['achievements']['bedwars_level'])
                for item in dic_list:
                    data_list.append(data_dic["player"]["stats"]["Bedwars"][item])
                
                data += f"★{data_list[0]},  "
                data += f"{name},  "
                data += f"FKDR: {round(data_list[3] / data_list[4], 2)},  "
                data += f"KDR: {round(data_list[5] / data_list[6], 2)},  "
                data += f"BBLR: {round(data_list[7] / data_list[8], 2)},  "
                data += f"WLR: {round(data_list[1] / data_list[2], 2)}\n"
                return data
            else:
                return f"error name [{name}]\n"
        else:
            return f"Invalid API key\n"

    except KeyError:
        return "error\n"
# print(bedwars_status("A_miton"))