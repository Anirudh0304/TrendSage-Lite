import pycountry
from thefuzz import fuzz

# Prepare country name set for quick access
country_names = [country.name for country in pycountry.countries]

def extract_countries_from_entities(named_entities):
    matched_countries = []

    # If named_entities is a string representation of a list of tuples, evaluate it
    if isinstance(named_entities, str):
        import ast
        try:
            named_entities = ast.literal_eval(named_entities)
        except:
            return []

    for ent in named_entities:
        text = ent[0] if isinstance(ent, tuple) else ent
        for country in country_names:
            if fuzz.ratio(text.lower(), country.lower()) >= 90:
                matched_countries.append(country)
                break

    return list(set(matched_countries))
