import requests
import tkinter as tk

class NewsApp:
    def __init__(self, master):
        self.master = master
        self.master.title("ArticyNews")
        self.master.geometry("1500x800")

        self.api_key = "fccfcb87844246cb81c99b8ed6030de5"

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.country_label = tk.Label(self.frame, text="Country:")
        self.country_label.pack()

        self.country_var = tk.StringVar(value="US")
        self.country_entry = tk.Entry(self.frame, textvariable=self.country_var)
        self.country_entry.pack()

        self.fetch_button = tk.Button(self.frame, text="Fetch News", command=self.fetch_news)
        self.fetch_button.pack()

        self.news_frame = tk.Frame(self.master)
        self.news_frame.pack()

    def fetch_news(self):
        url = f"https://newsapi.org/v2/top-headlines?country={self.country_var.get()}&apiKey={self.api_key}"
        response = requests.get(url)

        if response.status_code != 200:
            tk.messagebox.showerror("Error", "Failed to push origin news. If this continues to happen contact the creator.")
        else:
            data = response.json()

            articles = data['articles']
            articles = sorted(articles, key=lambda x: x.get('popularity', 0), reverse=True)
            top_3_articles = articles[:5]

            for i, article in enumerate(top_3_articles):
                article_frame = tk.Frame(self.news_frame)
                article_frame.pack()

                rank_label = tk.Label(article_frame, text=f"Rank {i + 1}:")
                rank_label.pack()

                title_label = tk.Label(article_frame, text=f"Title: {article['title']}")
                title_label.pack()

                description_label = tk.Label(article_frame, text=f"Description: {article['description']}")
                description_label.pack()

                content_label = tk.Label(article_frame, text=f"Article: {article.get('content', 'Not available.')}")
                content_label.pack()

root = tk.Tk()
app = NewsApp(root)
root.mainloop()