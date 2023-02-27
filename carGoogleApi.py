import requests
import pandas as pd
import numpy as np

url_api = 'https://maps.googleapis.com/maps/api/directions/json?'
origin = 'origin=37.573184,126.982093'
destination = 'destination=37.554073,126.970702'
departure_time = '1343614500'
api_key = 'AIzaSyBk0aszBg5zJAt_Ajkr9ZmFpPgyWWC8Dck'

headers = {}
payload = {}

url_final = url_api + origin + "&" + destination + "&" + departure_time + "&key=" + api_key

# url1 = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=37.554073,126.970702&radius=1&key=AIzaSyBk0aszBg5zJAt_Ajkr9ZmFpPgyWWC8Dck'
response = requests.request("GET", url_final, headers=headers, data=payload)
result = response.json()

print(response.text)