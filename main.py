import random
import time
import requests

base_url = "https://api.telegram.org/bot2126630484:AAE7_wKynuJiO7HXkvSh1tzogiCClzkOg-g"


def read_messages():
    parameters = {
        "offset" : "308642777"
    }
    res = requests.get(base_url + "/getUpdates", data=parameters)
    data = res.json()

    for result in data["result"]:
        if ("monos" or "mono") in result["message"]["text"]:
            send_stickers()

def send_stickers():
    monos = ["Chimpancé", "Orangután", "Gorila", "Bonobo"]

    stickers_monos = [
        "CAACAgQAAxkBAANLYZQR6SnW5pDFJGmYbBl92ol6Aj8AAi0LAALa06FQCDJJwCkiDgEiBA",
        "CAACAgQAAxkBAANEYZQObtIWuSuJP2NhGMliRwKaEXkAAtoMAAL8b6BQtpM2C2_n4xMiBA",
        "CAACAgQAAxkBAANFYZQObw0G8hs6L6-7wa8lbZ5MFOQAAtkLAAIMgKBQgwRB7CpsmBkiBA"
    ]

    sticker_ban = "AAMCBAADGQEAAz1hlAzpxOG_V9fFR6D87GPJoW8q8AACZA0AAuG4oVBvSyb1GyPd1gEAB20AAyIE"

    parameters = {
            "chat_id": "1568379163",
            "sticker": stickers_monos[random.randint(0, 2)],
        }
    res = requests.get(base_url + "/sendSticker", data=parameters)

    #for sticker_mono in stickers_monos:
    #    parameters = {
    #        "chat_id": "-698515563",
    #        "sticker": sticker_mono,
    #    }
    #    res = requests.get(base_url, data=parameters)
    #    print(res.text)

read_messages()
