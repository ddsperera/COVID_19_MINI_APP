import requests
import json
from datetime import datetime

def get_corona_update(country):
    url = 'https://api.covid19api.com/summary'
    r = requests.get(url)

    dict1 = r.json()

    dict2 =(dict1["Countries"])

    for line in dict2:
        if line["Country"] == country:
                dat = line["Date"]

                new_dat = datetime.strptime(dat,"%Y-%m-%dT%H:%M:%SZ")


                print(f"\n-----------last update:{new_dat}-----------")
                print(f"-confirmed cases on: {line['Country']}")
                print(f"-new confirmed: {line['NewConfirmed']}")
                print(f"-deaths: {line['NewDeaths']}")
                print(f"-recovered: {line['NewRecovered']}")


while True:
    country = input("enter country name to get updates -('q' to quit)-: ")

    if country != "q":
        get_corona_update(country)
    else:
        break