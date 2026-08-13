# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.
import requests
import smtplib
import os

API_KEY = os.environ.get("WEATHER_API_KEY")
LATITUDE = 14.605810
LONGITUDE = 121.021629
MY_EMAIL = os.environ.get("EMAIL")
MY_PASSWORD = os.environ.get("E_PASSWORD")

parameters = {"lat": LATITUDE,
            "lon": LONGITUDE,
            "appid": API_KEY,
              "cnt": 4}

weather_data = requests.get(url= "https://api.openweathermap.org/data/2.5/forecast", params=parameters)
weather_data.raise_for_status()

w_data_12hrs = weather_data.json()

def will_it_rain():
    for data in w_data_12hrs['list']:
        weather_id_code = data.get('weather')[0].get('id')
        if weather_id_code < 700:
            return True
    return False

def send_rain_alert():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,
                            msg=f"Subject:Bring an Umbrella!\n\nIt's raining today. Better bring an umbrella.\n\nFrom,\nGelo")

if will_it_rain():
    send_rain_alert()




