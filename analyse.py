import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from datetime import datetime
import os

# Load news CSV
today = datetime.now().strftime("%Y-%m-%d")
file_path = f"output/news_data_{today}.csv"

if not os.path.exists(file_path):
    print(f"News file not found: {file_path}")
    exit()

df = pd.read_csv(file_path)

# Init VADER
sid = SentimentIntensityAnalyzer()

# Apply sentiment scoring
df['sentiment_score'] = df['title'].apply(lambda x: sid.polarity_scores(str(x))['compound'])
df['sentiment_label'] = df['sentiment_score'].apply(
    lambda score: 'positive' if score > 0.05 else ('negative' if score < -0.05 else 'neutral')
)

# Save results
output_file = f"output/news_sentiment_{today}.csv"
df.to_csv(output_file, index=False)
print(f"Saved sentiment scores to {output_file}")
