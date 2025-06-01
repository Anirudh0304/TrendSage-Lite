import pandas as pd
import spacy
from datetime import datetime
import os

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load your existing sentiment news file
today = datetime.now().strftime("%Y-%m-%d")
file_path = f"output/news_sentiment_{today}.csv"

if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
    exit()

df = pd.read_csv(file_path)

# Prepare new columns
noun_phrases = []
named_entities = []

# Process each headline
for title in df['title']:
    doc = nlp(str(title))

    # Extract noun chunks (noun phrases)
    np = [chunk.text for chunk in doc.noun_chunks]

    # Extract named entities
    ents = [ent.text for ent in doc.ents if ent.label_ in ['PERSON', 'ORG', 'GPE', 'EVENT']]

    noun_phrases.append(", ".join(np))
    named_entities.append(", ".join(ents))

# Add new columns
df['noun_phrases'] = noun_phrases
df['named_entities'] = named_entities

# Save enriched CSV
output_path = f"output/news_keywords_spacy_{today}.csv"
df.to_csv(output_path, index=False)
print(f"Saved enriched file with noun phrases and named entities to {output_path}")
