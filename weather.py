import requests
from datetime import datetime, timedelta, timezone


def print_weather(lat, lon):
    URL = "https://api.met.no/weatherapi/locationforecast/2.0/compact"
    PARAMS = { 'lat': lat, 'lon': lon }
    headers = {
        'User-Agent': 'funky-weather/1.0 erik.larsen@funkweb.org'
    }
    request = requests.get(url=URL, params=PARAMS, headers=headers)

    data = request.json()

    timeseries = data["properties"]["timeseries"]

    periods = ['00-06', '06-12', '12-18', '18-00']

    base_date = datetime.now(timezone.utc).date() + timedelta(days=1)

    for day in range(7):
        start_time = datetime.combine(base_date + timedelta(days=day), datetime.min.time(), tzinfo=timezone.utc)
        end_time = start_time + timedelta(days=1)

        all_day_temps = []
        daily_temps = {period: [] for period in periods}
        

        for entry in timeseries:
            entry_time = datetime.fromisoformat(entry["time"].replace("Z", "+00:00"))
            if start_time <= entry_time < end_time:
                hour = entry_time.hour
                period = get_period(hour)
                temp = entry["data"]["instant"]["details"]["air_temperature"]
                all_day_temps.append(temp)
                #print(f"Kl {entry_time.strftime('%H:%M')} {temp} grader")
                daily_temps[period].append(temp)


        print(f"---{start_time.strftime('%A %-d. %B %Y')} (snittemperatur {(sum(all_day_temps) / len(all_day_temps)):.1f} grader)---")
        for period, temps in daily_temps.items():
            if temps:
                period_min_temp = min(temps)
                period_max_temp = max(temps)
                period_avg_temp = sum(temps) / len(temps)
                print(f"{period}: fra {period_min_temp} til {period_max_temp} grader (snittemperatur {period_avg_temp:.1f} grader)")



def get_period(hour):
    if 0 <= hour < 6:
        return '00-06'
    elif 6 <= hour < 12:
        return '06-12'
    elif 12 <= hour < 18:
        return '12-18'
    else:
        return '18-00'




