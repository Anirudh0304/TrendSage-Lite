import requests
import pandas as pd
from datetime import datetime

API_KEY = 'f8995c41d39e4487bad4fec01a7d3c45'
response = requests.get("https://newsapi.org/v2/everything?q=tesla&from=2025-04-30&sortBy=publishedAt&apiKey=f8995c41d39e4487bad4fec01a7d3c45")

if response.status_code == 200:
    data = response.json()
    articles = data.get("articles", [])
else:
    print("Failed to fetch news:", response.status_code)
    articles = []

news_list = []

for article in articles:
    news_list.append({
        "title": article["title"],
        "description": article["description"],
        "publishedAt": article["publishedAt"],
        "source": article["source"]["name"],
        "url": article["url"]
    })

df = pd.DataFrame(news_list)

today = datetime.now().strftime("%Y-%m-%d")
df.to_csv(f"output/news_data_{today}.csv", index=False)

print(f"Saved {len(df)} articles to output/news_data_{today}.csv")
