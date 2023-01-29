import requests

api_key = "fccfcb87844246cb81c99b8ed6030de5"
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

response = requests.get(url)

if response.status_code != 200:
    print("Error: Failed to retrieve news articles.")
    print("Status code: ", response.status_code)
else:
    data = response.json()

    articles = data['articles']
    articles = sorted(articles, key=lambda x: x.get('popularity', 0), reverse=True)
    top_3_articles = articles[:3]

    for i, article in enumerate(top_3_articles):
        print(f"Rank {i + 1}:")
        print("Title: ", article['title'])
        print("Description: ", article['description'])
        if 'content' in article:
            print("Article: ", article['content'])
        else:
            print("Article: Not available.")
        print("\n")