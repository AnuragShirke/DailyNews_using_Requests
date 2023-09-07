import requests
import json
import tkinter as tk
from tkinter import scrolledtext, simpledialog
import webbrowser
from datetime import datetime, timedelta

news = {}  # Initialize an empty news dictionary

def fetch_news():
    global news  # Use the global news dictionary
    query = query_entry.get()
    
    # Get today's date and format it as YYYY-MM-DD
    today_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    
    url = f"https://newsapi.org/v2/everything?q={query}&from={today_date}&sortBy=publishedAt&apiKey=c579bae93ec8492db9fbbc3df2a90684"
    r = requests.get(url)
    print("API Response:", r.text)  # Print the API response for debugging
    news = json.loads(r.text)

    if "articles" in news:
        news_text.config(state=tk.NORMAL)
        news_text.delete(1.0, tk.END)
        for index, article in enumerate(news["articles"], start=1):
            news_text.insert(tk.END, f"{index}. {article['title']}\n{article['description']}\n\n")
        news_text.config(state=tk.DISABLED)
    else:
        print("No articles found in response.")  # Print a message for debugging

def view_article():
    global news  # Use the global news dictionary
    try:
        selected_index = simpledialog.askinteger("Article Index", "Enter the article index:")
        if selected_index is not None and 1 <= selected_index <= len(news["articles"]):
            selected_article = news["articles"][selected_index - 1]
            article_url = selected_article["url"]
            webbrowser.open(article_url)  # Open the article URL in the default web browser
    except (ValueError, IndexError):
        pass  # Ignore errors

root = tk.Tk()
root.title("News Article Viewer")

query_label = tk.Label(root, text="Enter query:")
query_label.pack()

query_entry = tk.Entry(root)
query_entry.pack()

fetch_button = tk.Button(root, text="Fetch News", command=fetch_news)
fetch_button.pack()

news_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20, state=tk.DISABLED)
news_text.pack()

view_button = tk.Button(root, text="View Full Article", command=view_article)
view_button.pack()

root.mainloop()