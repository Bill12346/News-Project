import time

import requests


api_key = "fccfcb87844246cb81c99b8ed6030de5"


url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + api_key
response = requests.get(url)


data = response.json()
for i, article in enumerate(data["articles"]):
    if i >= 5:
        break
    print(f"{i + 1}. {article['title']}")
    time.sleep(0.2)

time.sleep(69420)








