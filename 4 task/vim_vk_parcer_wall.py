import pandas as pd
import requests

vk_config = {
    "token": "589a90f5309ad76d7898eb3263d08bbc3f1d453bf8b8af3844bfa59e0656d46dc589e587a21e7a2d5384a",  # временный токен
    "client_id": "7861998",  # ID приложения
    "version": "5.131",
    "domain": "https://api.vk.com/method/",
}

list_text = []
for i in range(100, 2500, 100):
    req = requests.get(
        vk_config["domain"] + "wall.get",
        params={
            "access_token": vk_config["token"],
            "v": vk_config["version"],
            "owner_id": -105021375,
            "count": 100,
            "offset": i,
        },
    )

    data = req.json()["response"]["items"]
    for item in data:
        # print(item["text"], "-------------", sep="\n")
        list_text.append(item["text"])


df1 = pd.DataFrame({"message": list_text})
# df1.to_csv("vk_wine.csv")
