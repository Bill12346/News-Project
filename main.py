import requests
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import io

class NewsApp:
    def __init__(self, master):
        self.master = master
        self.master.title("ArticyNews")
        self.master.geometry("1020x750")

        # Load the image from the link
        image_url = "https://bill12346.github.io/laprissystems/ArticyNews.png"
        image_response = requests.get(image_url)
        image_data = image_response.content
        image = Image.open(io.BytesIO(image_data))

        # Resize the image to fit in the label
        image = image.resize((210, 145), Image.ANTIALIAS)

        # Convert the image to Tkinter format and display it in a label
        tk_image = ImageTk.PhotoImage(image)
        self.image_label = tk.Label(self.master, image=tk_image)
        self.image_label.image = tk_image
        self.image_label.place(x=0, y=0)


        self.api_key = "fccfcb87844246cb81c99b8ed6030de5"

        self.frame = tk.Frame(self.master)
        self.frame.pack(pady=10)

        self.category_label = tk.Label(self.frame, text="Select a category of news to view : ")
        self.category_label.pack()

        self.categories = ["General", "Technology", "Stocks", "Science", "Economy", "Global"]
        self.category_var = tk.StringVar(value=self.categories[0])
        self.category_dropdown = ttk.Combobox(self.frame, textvariable=self.category_var, values=self.categories)
        self.category_dropdown.pack()

        self.fetch_button = tk.Button(self.frame, text="Recieve News", command=self.fetch_news)
        self.fetch_button.pack(pady=10)

        self.news_frame = tk.Frame(self.master)
        self.news_frame.pack(pady=10)

    def clear_news(self):
        for widget in self.news_frame.winfo_children():
            widget.destroy()

    def fetch_news(self):
        self.clear_news()
        category = self.category_var.get().lower()

        if category == "general":
            url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={self.api_key}"
        elif category == "technology":
            url = f"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={self.api_key}"
        elif category == "stocks":
            url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={self.api_key}&q=stocks"
        elif category == "science":
            url = f"https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey={self.api_key}"
        elif category == "economy":
            url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={self.api_key}&q=money"
        elif category == "global":
            url = f"https://newsapi.org/v2/top-headlines?language=en&category=general&apiKey={self.api_key}&q=international"

        response = requests.get(url)

        if response.status_code != 200:
            tk.messagebox.showerror("Error",
                                    "Failed to fetch news. Please refresh and if this continues, please open a support ticket.")
        else:
            data = response.json()

            articles = data['articles']
            if len(articles) == 0:
                no_news_label = tk.Label(self.news_frame, text="NO NEWS TO DISPLAY!")
                no_news_label.pack()
            else:
                articles = sorted(articles, key=lambda x: x.get('popularity', 0), reverse=True)
                top_5_articles = articles[:5]

                for i, article in enumerate(top_5_articles):
                    article_frame = tk.Frame(self.news_frame)
                    article_frame.pack(pady=10)

                    title_label = tk.Label(article_frame, text=f"Title: {article['title']}", font=("Arial", 12, "bold"),
                                           fg="#0066CC")
                    title_label.pack(pady=5)

                    description_label = tk.Label(article_frame, text=f"Description: {article['description']}",
                                                 font=("Arial", 10))
                    description_label.pack(pady=5)

                    link_button = tk.Button(article_frame, text="View Full Article",
                                            command=lambda url=article['url']: self.open_link(url), bg="#0066CC",
                                            fg="white", relief="flat")
                    link_button.pack(pady=22)

                    line_canvas = tk.Canvas(article_frame, height=2, width=800, bg="white", highlightthickness=0)
                    line_canvas.create_line(0, 1, 800, 1, width=2, fill="#0066CC")
                    line_canvas.pack()

    def open_link(self, url):
        import webbrowser
        webbrowser.open(url)


root = tk.Tk()
app = NewsApp(root)
root.mainloop()
