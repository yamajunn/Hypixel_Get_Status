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
        API_KEY = "04092887-a47c-4609-a6aa-433d2407ebf5"
        uuid_link = f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}"

        data_dic = getinfo(uuid_link)
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
                
                data += f"Name : {name}\n"
                data += f"Star : {data_list[0]}\n"
                data += f"Wins : {data_list[1]}, Losses : {data_list[2]}, WLR : {round(data_list[1] / data_list[2], 2)}\n"
                data += f"Final Kills : {data_list[3]}, Final Deaths : {data_list[4]}, FKDR : {round(data_list[3] / data_list[4], 2)}\n"
                data += f"Kills : {data_list[5]}, Deaths : {data_list[6]}, KDR : {round(data_list[5] / data_list[6], 2)}\n"
                data += f"Bed Broken : {data_list[7]}, Bed Lost : {data_list[8]}, BBLR : {round(data_list[7] / data_list[8], 2)}\n"
                return data
            else:
                return "couldn't get data"
        else:
            return "error"

    except KeyError:
        return "name error"
# print(bedwars_status("A_miton"))
