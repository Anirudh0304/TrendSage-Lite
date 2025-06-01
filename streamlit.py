import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import datetime
import ast

today = datetime.now().strftime("%Y-%m-%d")

# Page Configuration

st.set_page_config(
    page_title="📊 TrendSage Lite Dashboard",
    layout="wide",
)

# Load and Cache the Data
@st.cache_data
def load_data():
    path = f"output/news_keywords_spacy_{today}_ner_with_countries.csv"
    df = pd.read_csv(path)
    df['publishedAt'] = pd.to_datetime(df['publishedAt'], errors='coerce')
    return df

df = load_data()

# Sidebar - Filters

st.sidebar.header("🔍 Filter News")

# Unique countries from 'countries' column
def extract_country_names(countries_str):
    try:
        countries = ast.literal_eval(countries_str)
        return [c['name'] for c in countries if isinstance(c, dict) and 'name' in c]
    except Exception:
        return []

df['country_names'] = df['countries'].apply(extract_country_names)

all_countries = sorted(set(
    c for sublist in df['country_names'].dropna().tolist()
    for c in sublist
))
# Unique sentiment labels
sentiments = df['sentiment_label'].unique().tolist()

# Sidebar selection widgets
selected_countries = st.sidebar.multiselect("🌍 Country", all_countries, default=all_countries)
selected_sentiments = st.sidebar.multiselect("📈 Sentiment", sentiments, default=sentiments)

# Convert 'countries' string to list
df['countries_list'] = df['country_names']


# Apply filters
filtered_df = df[
    df['sentiment_label'].isin(selected_sentiments) &
    df['countries_list'].apply(lambda x: any(c in selected_countries for c in x))
]

# Dashboard Title and KPIs

st.title("📡 TrendSage Lite – Global Event & Sentiment Tracker")
st.markdown("Visualize global news sentiment and trends interactively.")

# Top KPIs
col1, col2 = st.columns(2)
col1.metric("📰 Headlines", len(filtered_df))
col2.metric("📍 Countries", len(selected_countries))

# Choropleth Map Section
# Explode filtered_df on 'countries_list' to one country per row
df_exploded = filtered_df.explode('countries_list')

# Remove null or empty countries
df_exploded = df_exploded[df_exploded['countries_list'].notnull() & (df_exploded['countries_list'] != '')]

# Group by country and calculate average sentiment_score
df_country_sentiment = (
    df_exploded.groupby('countries_list')['sentiment_score']
    .mean()
    .reset_index()
    .rename(columns={'countries_list': 'country', 'sentiment_score': 'average_sentiment'})
)

# Plot choropleth map
fig = px.choropleth(
    df_country_sentiment,
    locations='country',
    locationmode='country names',
    color='average_sentiment',
    color_continuous_scale=["red", "orange", "yellow", "lightgreen", "green"],
    title="Global News Sentiment by Country",
)

fig.update_layout(
    geo=dict(showframe=False, showcoastlines=False),
    coloraxis_colorbar=dict(title="Sentiment")
)

st.plotly_chart(fig, use_container_width=True)

# Country-wise Headlines Table
st.subheader("🌐 Country-wise Headlines")

for country in selected_countries:
    country_df = filtered_df[filtered_df['countries_list'].apply(lambda x: country in x)]
    if not country_df.empty:
        with st.expander(f"📌 {country} — {len(country_df)} articles"):
            st.dataframe(
                country_df[['title', 'sentiment_label', 'publishedAt', 'source', 'url']],
                use_container_width=True
            )

# Export Option
st.subheader("📦 Export Filtered Data")
st.download_button(
    label="📥 Download as CSV",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_trendsage_data.csv",
    mime="text/csv"
)
