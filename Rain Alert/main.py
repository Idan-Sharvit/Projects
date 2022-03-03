# The following script will check if it's going to be a rainy day.
# If it is, it will send an sms to your phone with a recommendation to grab an umbrella.
# If you want to be able to receive this notification every morning, you can upload this code to pythonanywhere.com.
# In addition, you'll have to make a Twilio account, and sign up for openweathermap.org to get an api key.


import requests
from twilio.rest import Client


account_sid = 'Place your account sid from the Twilio dashboard'
auth_token = 'Place your auth token from the Twilio dashboard'
RAIN_INDICATION = 700 # By the api documentation, if the value in the data is less then 700 it indicates on a rainy day.
OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = 'Place your "openweathermap api key'
weather_params = {
    'lat': 'Enter your latitude',
    'lon': 'Enter your longitude',
    'exclude': 'current,minutely,daily',
    'appid': api_key,
}
response = requests.get(url=OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
hourly_forecast = weather_data['hourly'][:12]
for hour in hourly_forecast:
    condition_code = hour['weather'][0]['id']
    if int(condition_code) < RAIN_INDICATION:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body="It's going to rain today, remember to bring an ☔️!",
                from_='Place the phone number from the Twilio dashboard',
                to="Place the phone number you'd like to receive an sms with"
            )
        print(message.sid)
        break
