import requests
import pandas as pd
import math

def placeid_search(lat, lon, radius, api_key):
    url_api = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
    location  = "location=" + str(lat) + ',' + str(lon)
    radius = "radius=" + str(radius)
    api_key = "key=" + api_key

    url = url_api + location + "&" + radius + "&" + api_key

    headers = {}
    payload = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    result = response.json()
    geos = result['results']
    dists = []
    if len(geos) != 0:
        for i in range(len(geos)):
            res_geo = (geos[i]["geometry"]['location']['lat'], geos[i]["geometry"]['location']['lng'])
            geo = (lat, lon)
            dists.append(math.dist(res_geo, geo))
        # print(dists)
        idx = dists.index(min(dists))
        return  geos[idx]['place_id']
    else:
        return 'N/A'

    

dtf = pd.read_csv("C:/Users/hyorim/Desktop/연구실/[논문]KTX역사분류/문화시설/철도역인근문화시설_KTX_6000/철도역인근문화시설_KTX_3.csv", encoding='cp949')
print(dtf.head())

sisul_placeid = []

api_key = 'AIzaSyBk0aszBg5zJAt_Ajkr9ZmFpPgyWWC8Dck'
# results = dtf.apply(placeid_search, axis = 1, args = (1, api_key))
for index, row in dtf.iterrows():
    lon = row['시설경도']
    lat = row['시설위도']
    placeid = placeid_search(lat, lon, 1, api_key)
    print(row['시설명'])
    print(placeid)
    sisul_placeid.append(placeid)

dtf['시설_placeid'] = sisul_placeid
dtf.to_csv("C:/Users/hyorim/Desktop/연구실/[논문]KTX역사분류/문화시설/철도역인근문화시설_KTX_6000/철도역인근문화시설_KTX_3_placeid.csv", encoding='cp949')
