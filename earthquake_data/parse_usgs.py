import requests
import json
import pdb
import pymysql



#set up DB stuff

endpoint = 'shrub-earthquake.cluster-cq8uib2zuvo7.us-west-1.rds.amazonaws.com'
username = 'admin'
password = 'admin'
database_name = 'shrub_earthquake'



connection = pymysql.connect(host=endpoint, user=username, passwd=password, db=database_name)



response = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson")

geo_json = json.loads(response.content)

earthquakes = geo_json['features']




for item in earthquakes:

    #check if item exists in table


    #parse relevant properties
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

