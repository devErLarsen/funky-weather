from geolocation import get_lat_long
from weather import print_weather

lat, long = get_lat_long()

print_weather(lat, long)
