import requests

URL = "https://nominatim.openstreetmap.org/search"

def get_lat_long(city):
    PARAMS = { 'city': city, 'format': 'jsonv2' }
    request = requests.get(url = URL, params = PARAMS)

    data = request.json()

    if not data:
        raise CityNotFoundException(f"Fant ikke by med navn '{city}'")

    lat = data[0]['lat']
    long = data[0]['lon']

    return lat, long

class CityNotFoundException(Exception):
    """Exception raised when city cannot be found"""
    pass
