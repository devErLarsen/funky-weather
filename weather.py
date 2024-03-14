import requests
from datetime import datetime, timedelta, timezone

def print_weather(lat, lon, args):
    URL = "https://api.met.no/weatherapi/locationforecast/2.0/compact"
    PARAMS = { 'lat': lat, 'lon': lon }
    headers = {
        'User-Agent': 'funky-weather/1.0 erik.larsen@funkweb.org'
    }
    request = requests.get(url=URL, params=PARAMS, headers=headers)

    data = request.json()

    temp_option = 'temp' in args
    wind_option = 'vind' in args
    rain_option = 'regn' in args

    timeseries = data["properties"]["timeseries"]

    units = data['properties']['meta']['units']
    wind_speed_unit = units['wind_speed']
    air_temperature_unit = units['air_temperature']
    precipitation_amount_unit = units['precipitation_amount']

    periods = ['00-06', '06-12', '12-18', '18-00']

    base_date = datetime.now(timezone.utc).date() + timedelta(days=1)

    for day in range(7):
        start_time = datetime.combine(base_date + timedelta(days=day), datetime.min.time(), tzinfo=timezone.utc)
        end_time = start_time + timedelta(days=1)

        all_day_temps = []
        daily_temps = {period: {'temps': [], 'winds': [], 'rains': []} for period in periods}
        

        for entry in timeseries:
            entry_time = datetime.fromisoformat(entry["time"].replace("Z", "+00:00"))
            if start_time <= entry_time < end_time:
                hour = entry_time.hour
                period = get_period(hour)
                temp = entry["data"]["instant"]["details"]["air_temperature"]
                all_day_temps.append(temp)
                daily_temps[period]['temps'].append(temp)
                daily_temps[period]['winds'].append(entry['data']['instant']['details']['wind_speed'])


                if 'next_1_hours' in entry['data']:
                    daily_temps[period]['rains'].append(entry['data']['next_1_hours']['details']['precipitation_amount'])
                elif 'next_6_hours' in entry['data']:
                    daily_temps[period]['rains'].append(entry['data']['next_6_hours']['details']['precipitation_amount'])
                else:
                    continue


        if temp_option:
            print(f"---{start_time.strftime('%A %-d. %B %Y')} (snittemperatur {(sum(all_day_temps) / len(all_day_temps)):.1f} grader {air_temperature_unit})---")
        else:
            print(f"---{start_time.strftime('%A %-d. %B %Y')}---")

        for period in daily_temps:
            print(f"{period}:")
            temps = daily_temps[period]['temps']
            winds = daily_temps[period]['winds']
            rains = daily_temps[period]['rains']
            if temp_option:
                if temps:
                    period_min_temp = min(temps)
                    period_max_temp = max(temps)
                    period_avg_temp = sum(temps) / len(temps)
                    print(f"fra {period_min_temp} til {period_max_temp} grader {air_temperature_unit} (snittemperatur {period_avg_temp:.1f} grader {air_temperature_unit})")
            if wind_option:
                if winds:
                    period_avg_wind = sum(winds) / len(winds)
                    print(f"vind: {period_avg_wind:.1f} {wind_speed_unit} (avg)")

            if rain_option:
                if rains:
                    sum_period_rain = sum(rains)
                    print(f"regn: {sum_period_rain:.1f} {precipitation_amount_unit} (sum)")



def get_period(hour):
    if 0 <= hour < 6:
        return '00-06'
    elif 6 <= hour < 12:
        return '06-12'
    elif 12 <= hour < 18:
        return '12-18'
    else:
        return '18-00'
