import requests
base_url = "https://api.telegram.org/bot2126630484:AAE7_wKynuJiO7HXkvSh1tzogiCClzkOg-g/getUpdates"

final_update = {
    "limit" : "1"
}

res = requests.get(base_url, data = final_update)
print(res.text)

