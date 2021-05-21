import requests
import json
import pdb

response = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson")

geo_json = json.loads(response.content)

earthquakes = geo_json['features']

for item in earthquakes:
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    id = item["id"]
    print(id)
    place = item["properties"]["place"]
    print(place)
    magnitude = item["properties"]["mag"]
    print(magnitude)
    longitude = item["geometry"]["coordinates"][0]
    print(longitude)
    latitude = item["geometry"]["coordinates"][1]
    print(latitude)

