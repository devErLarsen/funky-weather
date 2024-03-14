from geolocation import CityNotFoundException, get_lat_long
from weather import print_weather

valid_options = ['temp', 'regn', 'vind']

def parse_input(input):
    return [arg.strip() for arg in input.split(',')]

def validate_options(options):
    valid_arguments = [option for option in options if option in valid_options]
    invalid_arguments = set(options) - set(valid_arguments)

    if invalid_arguments or not options:
        return False, f"Invalid argument(s) provided: {', '.join(invalid_arguments)}. enter only valid options!"
    else:
        return True, ''

while True:
    arg = input('Tast inn bynavn, regn*, temp*, vind* eller 0 for å avslutte (* = optional):\n')

    if arg == '0':
        break

    args = parse_input(arg)
    city = args.pop(0)
    valid, error_message = validate_options(args)

    if valid:
        try:
            lat, long = get_lat_long(city)
            print_weather(lat, long, args)
        except CityNotFoundException as e:
            print(e)
    else:
        print(error_message)


