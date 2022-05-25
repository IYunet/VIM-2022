import pandas as pd
import requests

vk_config = {
    "token": "7483c7cd85f1d630acbe0a27a4b189ae6989c322bbef89895a1af0b0a4ba089c4ca6909b79bcd97c833a5",  # временный токен или вечный токен
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
