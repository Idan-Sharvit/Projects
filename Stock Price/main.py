from math import ceil

import requests
from datetime import datetime as dt
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
APIKEY_APLHA = 'GBZBSR2NU7B95YKM'
APIKEY_NEWS = 'ca5ed3c307e24c428b201ffcad92f425'


alpha_vantage_url = 'https://www.alphavantage.co/query'
alpha_vantage_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': APIKEY_APLHA,
}
r = requests.get(url=alpha_vantage_url, params=alpha_vantage_parameters)
r.raise_for_status()
data = r.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]

# Get yesterday data.
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data['4. close'])

# Get the day before yesterday data.
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data['4. close'])


# Gets the stock price of a company
print(yesterday_closing_price)
print(day_before_yesterday_closing_price)

# Gets the difference in percentage between the previous day and the current day.
difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)
percentage = ceil(difference * 100 / yesterday_closing_price)
print(percentage)
if yesterday_closing_price > day_before_yesterday_closing_price:
    symbol = '🟢'
else:
    symbol = '🔻'

# Get the news.
news_url = 'https://newsapi.org/v2/top-headlines'
news_parameters = {
    'q': 'tesla',
    'from': dt.now(),
    'sortBy': 'popularity',
    'apiKey': APIKEY_NEWS,
}

response = requests.get(url=news_url, params=news_parameters)

articles = (response.json()['articles'])

print(articles)

account_sid = 'AC47f610c07a76ff412e528349b71de626'
auth_token = '0907d5d600d8d7de7f5f25ddf25e0a4a'
client = Client(account_sid, auth_token)
if percentage >= 5:
    message = client.messages \
                    .create(
                         body=f"{STOCK} {symbol} {percentage}%\n"
                              f"Headline: {articles[0]['title']}\n"
                              f"Brief:{articles[0]['description']}",
                         from_='Put your Twilio phone number here',
                         to='Addressee '
                     )

    print(message.sid)




