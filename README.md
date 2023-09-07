# DailyNews_using_Requests
# News Article Viewer

This Python application allows users to search for and view news articles using the [News API](https://newsapi.org/). It provides a simple graphical user interface (GUI) built with Tkinter to enter a search query, fetch news articles related to the query, and view full articles in a web browser.

## Features

- Fetch news articles based on user-provided search queries.
- Display a list of articles with titles and descriptions in a scrollable text area.
- Allow users to click on an article to view the full article in their default web browser.
- Automatically retrieve news articles from the News API, sorted by publication date.

## Prerequisites

Before running the application, you'll need to:

1. Sign up for a [News API](https://newsapi.org/) account.
2. Obtain your News API key.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone 



1.Open the main.py file in a text editor.

2.Replace "ENTER_YOUR_OWN_API_KEY" with your actual News API key in the fetch_news function.
# Replace "ENTER_YOUR_OWN_API_KEY" with your actual News API key
api_key = "ENTER_YOUR_OWN_API_KEY"


3.Save the main.py file.

## USAGE
1.Run the application:
   python main.py
   Enter a search query in the provided text field.

2.Click the "Fetch News" button to retrieve news articles related to the query.

3.The retrieved articles will be displayed in the scrollable text area.

4.To view the full article, select an article from the list and click the "View Full Article" button. This will open the article in your default web browser.
