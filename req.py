import requests
import json
from pprint import pprint

TOKEN = "2619421814940190"

def iq(name):
    url = "https://superheroapi.com/api/"
    dict_iq = {}
    link = "/search/"
    x = name
    for hero in x:
        res = requests.get(url+TOKEN+link+hero)
        data = res.json()
        #print(data['results'])
        for i in data['results']:
            if i['name'] == hero:
                iq = i['powerstats']['intelligence']
                dict_iq[hero] = int(iq)
    list_d = list(dict_iq.items())
    list_d.sort(reverse= True)

    return print(f"Самый умный герой {list_d[0][0]}, у него {list_d[0][1]}IQ !")

list_hero = ["Hulk", "Captain America", "Thanos"]
iq(list_hero)



