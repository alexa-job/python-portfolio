import requests
import sqlite3
from datetime import datetime
import os

conn = sqlite3.connect("weater.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS weather (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  city TEXT NOT NULL,
                  temperature_max REAL,
                  temperature_mim REAL,
                  precipitation REAL,
                  date TEXT NOT NULL)""")
    
inp_meteo = input ("Запрос (история, добавить): ")
if inp_meteo.lower() == "история":
   cursor.execute("SELECT * FROM weather ORDER BY city")
   rows = cursor.fetchall()
   if rows:
      for row in rows:
          print(f"{row[5]} - {row[1]}, макс: {row[2]}°C, мин: {row[3]}°C, осадки {row[4]} мм")
   else:
      print("История пуста!")
   conn.close() 
   exit()  
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
time_current = datetime.now().strftime('%d.%m.%Y %H:%M')
for i in range(days):
       # Чтение данных
     found = False
     cursor.execute("SELECT * FROM weather WHERE city = ? AND date = ?", (city, daily['time'][i]))
     if cursor.fetchone():
            cursor.execute("UPDATE weather SET temperature_max = ?, temperature_mim = ?, precipitation = ? WHERE city = ? AND date = ?",
            (daily["temperature_2m_max"][i], daily["temperature_2m_min"][i], daily["precipitation_sum"][i], city, daily['time'][i]))
            found = True
     
     if not found:   
            cursor.execute("INSERT INTO weather (city, temperature_max, temperature_mim, precipitation, date) VALUES (?, ?, ?, ?, ?)",
                           (city, daily["temperature_2m_max"][i], daily["temperature_2m_min"][i], daily["precipitation_sum"][i],daily['time'][i]))                
    
conn.commit()
conn.close() 