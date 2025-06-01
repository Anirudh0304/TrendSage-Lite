import pandas as pd
import ast
from datetime import datetime
import pycountry
from thefuzz import fuzz

today = datetime.now().strftime("%Y-%m-%d")
df = pd.read_csv(f"output/news_keywords_spacy_{today}_ner.csv")

df['named_entities'] = df['named_entities'].apply(
    lambda x: ast.literal_eval(x) if isinstance(x, str) else []
)

# Alternate ambiguous country names
alt_names = {
    "U.S.": "United States",
    "US": "United States",
    "USA": "United States",
    "U.K.": "United Kingdom",
    "UK": "United Kingdom",
    "Britain": "United Kingdom",
    "Russia": "Russian Federation",
    "South Korea": "Korea, Republic of",
    "North Korea": "Korea, Democratic People's Republic of",
    "Vatican": "Holy See",
}

# Demonym to country name
demonym_map = {}
for c in pycountry.countries:
    if hasattr(c, 'demonym'):
        demonym_map[c.demonym.lower()] = c.name

def detect_countries(named_entities):
    matches = []
    seen = set()

    for text, label in named_entities:
        norm_text = text.strip()

        # Fuzzy match with country names
        for country in pycountry.countries:
            if fuzz.ratio(norm_text.lower(), country.name.lower()) >= 85 and country.name not in seen:
                matches.append({
                    "name": country.name,
                    "alpha_2": country.alpha_2,
                    "alpha_3": country.alpha_3
                })
                seen.add(country.name)

        # Match alternate names
        if norm_text in alt_names:
            try:
                country = pycountry.countries.lookup(alt_names[norm_text])
                if country.name not in seen:
                    matches.append({
                        "name": country.name,
                        "alpha_2": country.alpha_2,
                        "alpha_3": country.alpha_3
                    })
                    seen.add(country.name)
            except LookupError:
                continue
        
        if label == "NORP" and norm_text.lower() in demonym_map:
            try:
                country = pycountry.countries.lookup(demonym_map[norm_text.lower()])
                if country.name not in seen:
                    matches.append({
                        "name": country.name,
                        "alpha_2": country.alpha_2,
                        "alpha_3": country.alpha_3
                    })
                    seen.add(country.name)
            except LookupError:
                continue

    return matches

df['countries'] = df['named_entities'].apply(detect_countries)

for _, row in df.iterrows():
    if row['countries']:
        print(f"🗺️ {row['title'][:60]} ➜ {[c['name'] for c in row['countries']]}")

output_path = f"output/news_keywords_spacy_{today}_ner_with_countries.csv"
df.to_csv(output_path, index=False)
print(f"✅ Done — saved with ISO codes at: {output_path}")
