import requests
from colorama import Fore

URL = "https://nominatim.openstreetmap.org/search"

# attempts to find the coordinates for a given city name, if not raise an exception.
# the service might return more than one result, (more than one country can have a city with the same name). Anyways we pick the first one, because laxy :^)
def get_lat_long(city):
    PARAMS = { 'city': city, 'format': 'jsonv2' }
    request = requests.get(url = URL, params = PARAMS)

    data = request.json()

    if not data:
        raise CityNotFoundException(f"{Fore.RED}Fant ikke by med navn '{city}'")

    lat = data[0]['lat']
    long = data[0]['lon']

    return lat, long

class CityNotFoundException(Exception):
    """Exception raised when city cannot be found"""
    pass
