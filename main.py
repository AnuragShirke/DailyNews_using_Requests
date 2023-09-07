# Import necessary libraries
import requests
import json
import tkinter as tk
from tkinter import scrolledtext, simpledialog
import webbrowser
from datetime import datetime, timedelta

# Initialize an empty news dictionary
news = {}

# Function to fetch news based on user query
def fetch_news():
    global news  # Use the global news dictionary
    query = query_entry.get()
    
    # Get yesterday's date and format it as YYYY-MM-DD
    today_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    
    # Replace "ENTER_YOUR_OWN_API_KEY" with your actual News API key
    api_key = "ENTER_YOUR_OWN_API_KEY"
    url = f"https://newsapi.org/v2/everything?q={query}&from={today_date}&sortBy=publishedAt&apiKey={api_key}"
    
    # Send a GET request to the News API
    r = requests.get(url)
    print("API Response:", r.text)  # Print the API response for debugging
    news = json.loads(r.text)

    # Check if there are articles in the response
    if "articles" in news:
        news_text.config(state=tk.NORMAL)
        news_text.delete(1.0, tk.END)
        # Display article titles and descriptions in the scrolled text widget
        for index, article in enumerate(news["articles"], start=1):
            news_text.insert(tk.END, f"{index}. {article['title']}\n{article['description']}\n\n")
        news_text.config(state=tk.DISABLED)
    else:
        print("No articles found in response.")  # Print a message for debugging

# Function to view the full article in a web browser
def view_article():
    global news  # Use the global news dictionary
    try:
        # Ask the user for the index of the article they want to view
        selected_index = simpledialog.askinteger("Article Index", "Enter the article index:")
        if selected_index is not None and 1 <= selected_index <= len(news["articles"]):
            selected_article = news["articles"][selected_index - 1]
            article_url = selected_article["url"]
            # Open the article URL in the default web browser
            webbrowser.open(article_url)
    except (ValueError, IndexError):
        pass  # Ignore errors

# Create the main tkinter window
root = tk.Tk()
root.title("News Article Viewer")

# Label and entry for user query
query_label = tk.Label(root, text="Enter query:")
query_label.pack()
query_entry = tk.Entry(root)
query_entry.pack()

# Button to fetch news
fetch_button = tk.Button(root, text="Fetch News", command=fetch_news)
fetch_button.pack()

# Scrolled text widget to display news
news_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20, state=tk.DISABLED)
news_text.pack()

# Button to view the full article
view_button = tk.Button(root, text="View Full Article", command=view_article)
view_button.pack()

# Start the main tkinter event loop
root.mainloop()
