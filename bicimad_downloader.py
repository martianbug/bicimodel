import requests
import pandas as pd

# Ejemplo general: descargar JSON desde un endpoint público (ajusta la URL real según docs EMT)
STATIONS_URL = "https://datos.emtmadrid.es/v1/transport/bicimadgo/bikes/availability/"
resp = requests.get(STATIONS_URL, timeout=15)
resp.raise_for_status()
data = resp.json()

# Suponiendo que data contiene una lista de estaciones con 'id','lat','lon','name','capacity'
stations = pd.json_normalize(data['stations'])
stations.to_csv("bicimad_stations.csv", index=False)
print("Estaciones guardadas:", stations.shape[0])
