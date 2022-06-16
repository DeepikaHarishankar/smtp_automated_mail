import smtplib
import datetime as dt
import random

user_name = "deepika4test@gmail.com"
password = "oIL1Z#3+adZxIM2"
recipients = ['deepika.see@gmail.com','deepika_swankar@yahoo.com','harishyam@gmail.com','ramnkl8219@gmail.com']


# TODO 1. Read the txt file and convert each line  into a list
# TODO 2. Pick a random entry from the list
# TODO 3. If now.date is Wednesday , send a mail to myself using smtplib with the random entry .
# ------Send a mail-----------------------------------------------------
def send_mail(quote):
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=user_name, password=password)

        connection.sendmail(from_addr=user_name,

                            to_addrs = recipients ,
                            msg=f'Subject:Monday Motivation\n\n {quote} \n -Deepika Harishankar')


# --------Read the txt file and convert each line  into a list-------------

with open('quotes.txt') as file_text:
    list_of_quotes = file_text.readlines()

quote_of_the_week = random.choice(list_of_quotes)
print(quote_of_the_week)

# ----If now.date is Wednesday , send a mail to myself using smtplib with the random entry .-----

current_day = dt.datetime.now()
if current_day.weekday() == 0:
    send_mail(quote_of_the_week)
