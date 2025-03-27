# ScraperAPI is used to bypass restrictions and simplify web scraping*
# ScraperAPI automates handling these problems by rotating IPs, bypassing CAPTCHAs,
#  and fetching data directly as structured JSON, so you don’t have to deal with raw HTML

# 1. Installation des bibliothèques nécessaires
import json 
import requests
import numpy as np 
import pandas as pd

# 2. Obtenir une clé API ScraperAPI
API_KEY="868041c800d6dc1c24abbd8c48f73eaa"

# 4.2 Gerer les erreurs, et prendre la valeur au clavier
#  akteb l query ta3 l business category w city , example IT Cunsulting Turronto
QUERY = input("Enter the business category and city : ").strip()

# 4.1 Effectuer une requête GET
SCRAPERAPI_URL =f"https://api.scraperapi.com/structured/google/mapssearch?api_key={API_KEY}&query={QUERY}"

# 4.2 Gerer les erreurs, et prendre la valeur au clavier
try:
    response = requests.get(SCRAPERAPI_URL)
    response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
    data = response.json()
    print("Data retrieved successfully!")
    
except requests.exceptions.RequestException as e:
    print(f"Error during the request: {e}")
except ValueError:
    print("Error: Could not decode JSON response.")

JSON_PATH = "data.json"

# 4.3 Sauvegarder la response dans un fichier json
with open(JSON_PATH, "w", encoding="utf-8") as json_file:
 json.dump(response.json(), json_file, ensure_ascii=False, indent=4)

# 4.4 Analyser le fichier json, sa structure et determiner comment recuperer les informations importantes
# response
# the important features :"name" "address" "stars" "ratings" "type" "district" "latitude" "longitude"

# 4.5 Ouvrir le fichier, et recuperer les valeurs desirees
def process_data():
    with open(JSON_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    
    businesses = data.get("results", [])
    extracted_data = []

    for business in businesses:
        # yjib l values ta3 features li fl json . kaml feature 3ndhom 1 value , ghir "address" raho list w tkoun list fargha y7bss . so dert hdik kta3 if li ta7tha  
        name = business.get("name", "N/A")
        address = business.get("address", "")
        
        if isinstance(address, list):  
            address = ", ".join(address)
            
        rating = business.get("stars", 0.0)
        reviews = business.get("ratings", 0)
        business_type = ", ".join(business.get("type", []))
        district = business.get("district", "Unknown")
#         latitude = business.get("latitude", None)
#         longitude = business.get("longitude", None)
#         first_image = business.get("images", [None])[0]  # Get the first image

#  ylem features kaml w y7othom f list "extracted_data"
        extracted_data.append((name, address, rating, reviews, business_type, district)) 
    return extracted_data

data = process_data()

# Define NumPy structured array type
# rj3tha f tableau numpy babch tji mafroza
dtype = np.dtype([
    ('Name', 'U100'),      
    ('Address', 'U200'),   
    ('Rating', 'f4'),      
    ('Reviews', 'i4'),     
    ('Type', 'U200'),      
    ('District', 'U100'),  
#     ('Latitude', 'f8'),  
#     ('Longitude', 'f8'), 
#     ('Image_URL', 'U300')  
])

np_table = np.array(data, dtype=dtype)
#  affichitha b pandas
df = pd.DataFrame(np_table)

print("Table of Businesses:\n")
print(df)


# 4.6 Trier et filtrer les résultats avant de les sauvegarder
def filter_and_sort_data(df, min_rating=4.0):

    filtered_df = df[df["Rating"] >= min_rating]
    sorted_df = filtered_df.sort_values(by="Rating", ascending=False)
    return sorted_df

new_df= filter_and_sort_data(df, min_rating=5)
print(new_df)

new_df.to_csv("filtered_businesses.csv", index=False, encoding="utf-8")
print("saved to 'filtered_businesses.csv'")