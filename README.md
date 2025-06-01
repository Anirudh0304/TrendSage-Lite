# 🌍 TrendSage Lite – Global Event & Sentiment Tracker

**TrendSage Lite** is an interactive dashboard that analyzes global news data to extract geopolitical entities, perform sentiment analysis, and display real-time trends on a choropleth map. Designed to help users monitor the emotional landscape and breaking stories across countries worldwide.

---

## 📁 Project Structure

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


🧠 Core Modules Explained
| Module                | Description                                             |
| --------------------- | ------------------------------------------------------- |
| `news.py`             | Pulls news data from APIs or datasets                   |
| `extract.py`          | Preprocesses, cleans, and analyzes news data            |
| `analyse.py`          | Runs sentiment and country/entity extraction pipelines  |
| `country.py`          | Maps named entities to standardized country codes       |
| `entities.py`         | Performs Named Entity Recognition (NER) focused on GPEs |
| `extract_keywords.py` | Extracts keywords/topics from news headlines            |
| `streamlit.py`        | Implements the Streamlit UI and visualization logic     |
