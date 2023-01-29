import time

import requests

api_key = "fccfcb87844246cb81c99b8ed6030de5"
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

response = requests.get(url)
data = response.json()

top_3_articles = data['articles'][:5]

for article in top_3_articles:
    print("Title: ", article['title'])
    print("Description: ", article['description'])
    print("Article: ", article['content'])
    print("\n")
time.sleep(6500)