import requests
base_url = "token"

final_update = {
    "limit" : "1"
}

res = requests.get(base_url, data = final_update)
print(res.text)

