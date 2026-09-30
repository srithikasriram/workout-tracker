from datetime import datetime

import requests
import os
WORKOUT_APP_ID = os.environ["WORKOUT_APP_ID"]
WORKOUT_API_KEY = os.environ["WORKOUT_API_KEY"]
WORKOUT_ENDPOINT = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]

headers = {
    "x-app-id" : WORKOUT_APP_ID,
    "x-app-key" : WORKOUT_API_KEY,
}
nutrition_config = {
    "query" : str(input("Tell me which exercises you did. ")),
    "weight_kg" : 48,
    "height_cm" : 155,
    "age" : 18,
    "gender" : "female",
}

response = requests.post(url=WORKOUT_ENDPOINT, headers=headers, json=nutrition_config)
response.raise_for_status()
result = response.json()
print(result)

sheety_endpoint = "https://api.sheety.co/82b43dead2459e5763168b6e69f796a3/workoutTrackcing/workouts"

sheety_header = {
    "Authorization" : os.environ["SHEETY_AUTHORIZATION"]
}

sheety_body = {
    "workout":{
        "date" : datetime.now().strftime("%m/%d/%Y"),
        "time" : datetime.now().strftime("%H:%M:%S"),
        "exercise" : result["exercises"][0]["name"],
        "duration" : result["exercises"][0]["duration_min"],
        "calories" : result["exercises"][0]["nf_calories"],
    }
}
sheety_response = requests.post(url=sheety_endpoint, headers=sheety_header, json=sheety_body)
print(sheety_response.status_code)
print(sheety_response.json())
