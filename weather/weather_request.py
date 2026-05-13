import requests
from json import dump, load
from datetime import datetime
import os

if os.path.exists('meteoreguest.json'):
    with open("meteoreguest.json", 'r', encoding='utf-8') as f:
        data_meteo = load(f)
else:
    data_meteo = {}
    
#inp_meteo = input ("Запрос (прогноз, история, обновить, выход)")
city = input("Введите город: ")
days = int(input("Период прогноза, дни: "))
# Поиск координат
geo_url = "https://geocoding-api.open-meteo.com/v1/search"
geo_params = {"name": city, "count": 1, "language": "ru"}
geo_data = requests.get(geo_url, params=geo_params).json()

if "results" not in geo_data:
    print("Город не найден")
    exit()

result = geo_data["results"][0]
lat = result["latitude"]
lon = result["longitude"]
print(f"Найден: {result['name']}, {result.get('country', '')}")

# Запрос погоды
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": lat,
    "longitude": lon,
    "current_weather": "true",
    "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum"],
    "timezone": "auto",
    "forecast_days": days
}

data = requests.get(url, params=params).json()

# Текущая погода
weather = data["current_weather"]
print(f"\nСейчас: {weather['temperature']}°C, ветер {weather['windspeed']} км/ч")


# Прогноз по дням
print("\nПрогноз погоды:")
daily = data["daily"]
if city not in data_meteo:
    data_meteo[city] = []
time_current = datetime.now().strftime('%d.%m.%Y %H:%M')
for i in range(days):
       found = False
       for record in data_meteo[city]:
           if record['date'] == daily['time'][i]:
                 record['time_request'] = time_current
                 record["tmax"] = daily["temperature_2m_max"][i]
                 record["tmin"] = daily["temperature_2m_min"][i]
                 record["precipitation"] = daily["precipitation_sum"][i]
                 found = True
                 break
       if not found:
           data_meteo[city].append({ "time_request": time_current,
                                     "date": daily["time"][i],
                                     "tmax": daily["temperature_2m_max"][i],
                                     "tmin": daily["temperature_2m_min"][i],
                                     "precipitation": daily["precipitation_sum"][i]})
          
# if cur_data:
#    data_meteo[city].append(cur_data)
       
print (data_meteo)

with open("meteoreguest.json", 'w', encoding='utf-8') as f:
     dump(data_meteo, f, ensure_ascii=False, indent=4)
