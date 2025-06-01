# 🌍 TrendSage Lite – Global Event & Sentiment Tracker

**TrendSage Lite** is an interactive dashboard that analyzes global news data to extract geopolitical entities, perform sentiment analysis, and display real-time trends on a choropleth map. Designed to help users monitor the emotional landscape and breaking stories across countries worldwide.

---

## 📁 Project Structure
```
SUPPLYCHAIN/
│
├── output/ # Folder for storing generated outputs like CSVs or logs
├── venv/ # Virtual environment (excluded from version control)
│
├── analyse.py # Main pipeline to run analysis
├── country.py # Country extraction & country-code utilities
├── entities.py # Named Entity Recognition using spaCy (GPE focus)
├── extract.py # Combined data extraction pipeline
├── extract_keywords.py # Extracts keywords/topics from headlines
├── news.py # News scraping logic or API integration
├── streamlit.py # Main dashboard UI (Streamlit app)
```

---

## 🔍 Features

- 🌐 **Choropleth Map:** Visualizes average sentiment scores across countries  
- 🧠 **NLP-Powered Sentiment & Entity Extraction:**  
  - GPE (countries, cities, geopolitical entities) extraction using spaCy  
  - Sentiment analysis using TextBlob or VADER  
- 📰 **Interactive UI:** Clickable countries display relevant headlines  
- 📤 **Export Filtered Data:** Download filtered news results as CSV files  
- 🎨 **Clean, Minimal UI:** Polished interface with company icons/logos  

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Git

### Installation

```bash
git clone https://github.com/yourusername/trendsage-lite.git
cd SUPPLYCHAIN

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Download required NLP models
python -m nltk.downloader vader_lexicon
python -m spacy download en_core_web_sm
```
---

## 📂 Execution Order

To ensure proper data flow between modules, run the scripts in this order:

1. `news.py` – Fetches global news headlines  
2. `analyse.py` – Performs sentiment analysis  
3. `extract_keywords.py` – Extracts significant keywords  
4. `entities.py` – Identifies named entities (GPEs, Orgs)  
5. `country.py` – Matches entities to country names and codes  
6. `streamlit.py` – Runs the interactive visualization dashboard

---

## 💻 Running the Dashboard

```bash
streamlit run streamlit.py
