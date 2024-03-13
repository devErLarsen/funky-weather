import requests
from datetime import datetime, timedelta, timezone

base_date = datetime.now(timezone.utc).date() + timedelta(days=1)
start_time = datetime.combine(base_date, datetime.min.time(), tzinfo=timezone.utc)
end_time = start_time + timedelta(days=1)

def print_weather(lat, lon):
    URL = "https://api.met.no/weatherapi/locationforecast/2.0/compact"
    PARAMS = { 'lat': lat, 'lon': lon }
    headers = {
        'User-Agent': 'funky-weather/1.0 erik.larsen@funkweb.org'
    }
    request = requests.get(url=URL, params=PARAMS, headers=headers)

    data = request.json()

    timeseries = data["properties"]["timeseries"]

    for entry in timeseries:
        entry_time = datetime.fromisoformat(entry["time"].replace("Z", "+00:00"))
        if start_time <= entry_time < end_time:
            temp = entry["data"]["instant"]["details"]["air_temperature"]
            print(f"Kl {entry_time.strftime('%H:%M')} {temp} grader")



