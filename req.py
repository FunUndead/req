import requests
import json
from pprint import pprint

TOKEN = "2619421814940190"

def iq(name):
    url = "https://superheroapi.com/api/"
    link = "/search/"
    x = name
    res = requests.get(url+TOKEN+link+x)
    data = res.json()
    #print(data['results'])
    for i in data['results']:
        if i['name'] == x:
            iq = i['powerstats']['intelligence']
    return int(iq)

hulk = iq("Hulk")
captain_america = iq("Captain America")
thanos = iq("Thanos")
#print (hulk, captain_america, thanos)
print ('Самый умный герой Танос!')

