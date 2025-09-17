import requests
import time

API_KEY = "TU_GOOGLE_PLACES_API_KEY"
NEARBY_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

def count_restaurants_near(lat, lon, radius=250):
    params = {
        "key": API_KEY,
        "location": f"{lat},{lon}",
        "radius": radius,
        "type": "restaurant"   # o 'food' / keywords
    }
    resp = requests.get(NEARBY_URL, params=params)
    resp.raise_for_status()
    j = resp.json()
    count = len(j.get("results", []))
    # paginación: si hay next_page_token, hacer más requests (respetando límites)
    return count

# Ejemplo rápido
lat, lon = 40.423, -3.688  # sustituye por coordenadas reales
print("Restaurants ~250m:", count_restaurants_near(lat, lon, radius=250))
