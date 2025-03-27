import json 
import requests
import numpy as np 
import pandas as pd

API_KEY="868041c800d6dc1c24abbd8c48f73eaa"
QUERY = input("Enter the business category and city : ").strip()
SCRAPERAPI_URL =f"https://api.scraperapi.com/structured/google/mapssearch?api_key={API_KEY}&query={QUERY}"

try:
    response = requests.get(SCRAPERAPI_URL)
    response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)


    data = response.json()
    print("Data retrieved successfully!")
    
except requests.exceptions.RequestException as e:
    print(f"Error during the request: {e}")
except ValueError:
    print("Error: Could not decode JSON response.")

JSON_PATH = "offres_emploi.json"
with open(JSON_PATH, "w", encoding="utf-8") as json_file:
 json.dump(response.json(), json_file, ensure_ascii=False, indent=4)

data
def process_data():
    with open(JSON_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    
    businesses = data.get("results", [])
    extracted_data = []
    for business in businesses:
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

        extracted_data.append((name, address, rating, reviews, business_type, district))

    return extracted_data

# data = process_data()
# for item in data[:5]:  # Display first 5 businesses
#     print(item)

data = process_data()

# Define NumPy structured array type
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
df = pd.DataFrame(np_table)

print("Table of Businesses:\n")
print(df)

def filter_and_sort_data(df, min_rating=4.0):

    filtered_df = df[df["Rating"] >= min_rating]
    sorted_df = filtered_df.sort_values(by="Rating", ascending=False)
    return sorted_df

new_df= filter_and_sort_data(df, min_rating=5)
print(new_df)

new_df.to_csv("filtered_businesses.csv", index=False, encoding="utf-8")
print("saved to 'filtered_businesses.csv'")