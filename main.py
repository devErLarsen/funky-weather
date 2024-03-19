from geolocation import CityNotFoundException, get_lat_long
from weather import print_weather

# text color
from colorama import init, Fore
init(autoreset=True)

valid_options = ['regn', 'vind']
default_days = 7

def parse_input(input):
    # split the input string into separate arguments
    arg_arr = [arg.strip() for arg in input.split(',')]
    days = -1
    # try to find a digit for number of days, and remove it from the rest of the list.
    for i, arg in enumerate(arg_arr):
        if arg.isdigit():
            days = int(arg_arr.pop(i))

    # no argument provided, use default number of days
    if days == -1:
        days = default_days

    return arg_arr, days

# compare options provided to valid_options, returns true/false and error strings.
def validate_options(options):
    valid_arguments = [option for option in options if option in valid_options]
    invalid_arguments = set(options) - set(valid_arguments)

    if invalid_arguments:
        invalid_arguments_str = ', '.join(f"'{arg}'" for arg in invalid_arguments)
        valid_options_str = ', '.join(f"'{opt}'" for opt in valid_options)
        return False, f"Ugyldige argumenter angitt: {invalid_arguments_str}. gyldige argumenter er {valid_options_str}"
    else:
        return True, ''

# check if provided days is between 1 and 10.
def validate_days(days):
    return days >= 1 and days <= 10

# print the accumulated error messages.
def print_input_errors(errors):
    for error_message in errors:
        print(f"{Fore.RED}{error_message}")

# 'program loop' exits on user entering '0' into the console.
while True:
    arg = input('Tast inn bynavn, regn*, vind*, antall dager* (default 7) eller 0 for å avslutte (* = optional):\n')

    if arg == '0':
        break

    error_messages = []

    args, days = parse_input(arg)
    city = args.pop(0)
    days_valid = validate_days(days)

    if not days_valid:
        error_messages.append('Om du har spesifisert antall dager må nummeret være mellom 1 og 10.')

    options_valid, options_error_message = validate_options(args)
    if options_error_message:
        error_messages.append(options_error_message)
    


    if len(error_messages) == 0:
        try:
            lat, long = get_lat_long(city)
            print_weather(lat, long, days, option_args=args)
        except CityNotFoundException as e:
            print(e)
    else:
        print_input_errors(error_messages)


