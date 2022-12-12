import requests
from bs4 import BeautifulSoup
import json

while True:
    weapon_data = ""
    base_url = "https://www.csgodatabase.com/weapons/"

    soup = BeautifulSoup(requests.get(base_url).text, 'html.parser')
    weapon_classes = soup.find_all(class_="item-box-header ConsumerSkinBox")

    _conditions = ["Factory New", "Minimal Wear", "Field-Tested", "Well-Worn", "Battle-Scarred"]

    for _class in weapon_classes:
        print("***** Searching in class: " + _class.text + " *****")

        _class_url = base_url + _class.text

        _class_soup = BeautifulSoup(requests.get(_class_url).text, 'html.parser').find_all(class_="skin-box")

        for weapon in _class_soup:
            print("***** Searching in weapon: " + weapon.find_all('a')[0].text + " *****")

            weapon_name = weapon.find_all('a')[0].text
            weapon_name_strip = (weapon_name.split("|")[0][:-1] + weapon_name.split("|")[1]).replace(" ", "-").lower()

            url = "https://www.csgodatabase.com/skins/" + weapon_name_strip

            round_box_soup = BeautifulSoup(requests.get(url).text, 'html.parser').find(class_="round-box-content")

            if(round_box_soup == None):
                for i in range(5):
                    weapon_data += "StatTrak™ " + weapon_name + ":" + _conditions[i] + ":" + "None" + ","
                    weapon_data += weapon_name + ":" + _conditions[i] + ":" + "None" + ","

                continue

            conditions = round_box_soup.find_all(class_="steam-pricing-name")
            prices = round_box_soup.find_all(class_="steam-pricing-buy")

            pairs = []

            for i in range(len(conditions)):

                _name = weapon_name

                condition = conditions[i].text

                if(condition.startswith("StatTrak™ ")):
                    condition = condition[len("StatTrak™ "):]

                    _name =  "StatTrak™ " + _name

                if(i >= len(prices)):
                    weapon_data += "StatTrak™ " + _name + ":" + condition + ":" + "None" + ","
                    weapon_data += _name + ":" + condition + ":" + "None" + ","

                else:
                    weapon_data += _name + ":" + condition + ":" + prices[i].text + ","

    weapon_data = weapon_data[:-1]

    with open('csgoDB.txt', 'w', encoding='utf-8') as f:
        f.write(weapon_data)
        f.close()


