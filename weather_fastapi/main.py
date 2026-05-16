from fastapi import FastAPI
import requests 

app = FastAPI()
# @app.get("/")
# def read_root():
#     return {"message": "Привет, мир!"}

@app.get("/weather/{city}")  
def get_weather(city: str):
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_param = {"name": city, "count": 1, "language": "ru"}
    geo_data = requests.get(url=geo_url, params=geo_param).json()

    if "results" not in geo_data:
        # print (f"Город {city} не найден!")
        return {"error": f"Город {city} не найден"}
    
    results = geo_data ["results"][0]
    lat = results["latitude"]
    lon = results["longitude"]


    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": lat, 
              "longitude":lon,
              "current":["temperature_2m", "wind_speed_10m", "rain"]}

    data = requests.get(url=url, params=params).json()

    if "current" not in data:
        # print("Информация о погоде не найдена!")
        return {"error":"Информация о погоде не найдена!"}

    current = data["current"]
    return {"city": city, "temperature": current['temperature_2m'], "wind": current['wind_speed_10m'], "rain": current['rain']}
    #cd fastapi_weather, затем uvicorn main:app --reload
    #http://127.0.0.1:8000/weather/Иркутск
    #http://127.0.0.1:8000/docs