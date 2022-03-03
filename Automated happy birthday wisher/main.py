from email.message import EmailMessage
import pandas as pd
import random
import smtplib
import datetime as dt

REPLACE = '[NAME]'
MY_EMAIL = 'PLACE YOUR EMAIL HERE'
PASSWORD = 'PLACE YOUR PASSWORD'
current_date = dt.datetime.now()

file = pd.read_csv('birthdays.csv')
birthdays = file.to_dict(orient='records')
for person in birthdays:
    if person['day'] == current_date.day and person['month'] == current_date.month:
        person_email = person['email']
        person_name = person['name']
        with open(f'./letter_templates/letter_{random.randint(1, 3)}.txt', mode='r') as letter:
            copy_of_letter = ''.join(letter.read())
            copy_of_letter = copy_of_letter.replace(REPLACE, person_name)
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)

                msg = EmailMessage()
                msg.set_content(copy_of_letter)
                msg["Subject"] = 'HAPPY BIRTHDAY'
                msg["From"] = MY_EMAIL
                msg["To"] = person_email
                connection.send_message(msg)
