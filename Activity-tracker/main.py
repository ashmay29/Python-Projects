import requests
from datetime import datetime
APP_ID = " "
API_KEY = " "
API_ENDPOINT = " "

SHEETS_ENDPOINT = " "
SHEETS_API_KEY = " "

exercise_headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key':API_KEY,
}

exercise_params = {
    "query" : input('What exercise/activity did you do today?'),
    "age" : int(input('What is your age?')),
    "gender": input("What is your gender?"),
    "weight_kg" : int(input('What is your weight in kg?')),
    "height_cm" : int(input('What is your height in cm?')),
}

response = requests.post(API_ENDPOINT,json=exercise_params,headers=exercise_headers)
response.raise_for_status()
exercises = response.json()
# print(exercises)

sheet_header = {
    "Authorization":"Bearer ahs1210",
    }

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in exercises["exercises"]:
    sheet_params = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response = requests.post(SHEETS_ENDPOINT,headers=sheet_header,json=sheet_params)
    data = response.json()
    # print(data)