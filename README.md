# 🗺️ Google Maps Business Scraper

A Python-based project that automates the extraction of **business data from Google Maps** using the [ScraperAPI Structured Data endpoint](https://www.scraperapi.com/structured-data/).  
This tool allows users to search any business category in any city, retrieve detailed listings, filter by ratings, and export the top results to CSV for further analysis.

---

## 🚀 Features

- 🔍 Fetch structured business data (name, address, type, rating, etc.)
- 🌍 Uses **ScraperAPI** to bypass CAPTCHAs and Google restrictions
- 💾 Automatically saves results to `.json` and `.csv` files
- 🧹 Filters and sorts businesses by rating
- 📊 Converts data into clean Pandas DataFrames for easy analysis

---

## 🧠 Project Overview

This script leverages the **ScraperAPI structured endpoint** to collect business listings directly from Google Maps.  
It converts the retrieved JSON data into a structured table using **NumPy** and **Pandas**, filters results by a minimum rating, and exports the final dataset for reporting or research purposes.

---

## 🧰 Technologies Used

- **Python 3.10+**
- **Requests** – for API requests  
- **NumPy** – for structured data arrays  
- **Pandas** – for data processing and export  
- **ScraperAPI** – for Google Maps structured scraping  

---
## ▶️ Usage

Run the main script:  
`python web_scrapping.py`

When prompted, enter a search query such as:  
`Enter the business category and city : coffee shops Paris`

The program will:

- Fetch data from Google Maps using ScraperAPI  
- Save the raw JSON to `offres_emploi.json` (or `data.json`)  
- Extract business names, addresses, ratings, reviews, and types  
- Filter and sort top-rated businesses  
- Save the clean results to `filtered_businesses.csv`

