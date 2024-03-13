from geolocation import CityNotFoundException, get_lat_long
from weather import print_weather

while True:
    arg = input('Tast inn bynavn, eller 0 for å avslutte:\n')

    if arg == '0':
        break

    try:
        lat, long = get_lat_long(city=arg)
        print_weather(lat, long)
    except CityNotFoundException as e:
        print(e)

