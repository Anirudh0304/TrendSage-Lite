import pandas as pd
import spacy
from datetime import datetime
import ast

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load today's CSV file
today = datetime.now().strftime("%Y-%m-%d")
file_path = f"output/news_keywords_spacy_{today}.csv"
df = pd.read_csv(file_path)

# Choose which column to analyze (title is better than description for entities)
text_column = 'title'

# Replace NaNs with empty strings
df[text_column] = df[text_column].fillna('')

# Apply NER and extract entities
def extract_named_entities(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

df['named_entities'] = df[text_column].apply(extract_named_entities)

# Save updated file
updated_path = f"output/news_keywords_spacy_{today}_ner.csv"
df.to_csv(updated_path, index=False)
print(f"✅ NER complete. File saved to {updated_path}")
