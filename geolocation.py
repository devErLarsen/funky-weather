import requests

URL = "https://nominatim.openstreetmap.org/search"

def get_lat_long():
    PARAMS = { 'country': 'norway', 'city': 'oslo', 'format': 'jsonv2' }
    request = requests.get(url = URL, params = PARAMS)

    data = request.json()

    lat = data[0]['lat']
    long = data[0]['lon']

    return lat, long
