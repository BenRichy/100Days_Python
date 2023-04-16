import smtplib
import json
import getpass
import datetime as dt
import random
from birthday_wisher import birthday_wisher

#Set variables
dir_fp = "Day_32_smtplib_datetime/"
send_email = True
BenRichie_User = True
Account = "GMail_App"
email_type = "birthday"
email_to_send = "ben_richmond@ntlworld.com"
#0-Monday, 1-Tueday etc.
weekday_quote = 6

#depending on what the user decides to send, the following code triggers
if email_type == "greeting":
    send_message = "Subject:Hello\n\nHello, this is a test from python."
#if "quote" is chosen as email_type
elif email_type == "quote":
    #get current day number
    current_day = dt.datetime.now().weekday()
    if current_day == weekday_quote:
        #get a random quote from the list
        quotes = open(dir_fp+"quotes.txt").read().splitlines()
        send_message = "Subject:Motivational Quote\n\n"+random.choice(quotes)
    else:
        next
elif email_type == "birthday":
    bday_message = birthday_wisher()
    email_to_send = bday_message[0]
    send_message = f"Subject:Birthday Message\n\n{bday_message[1]}"
    next


if  send_email:
    if BenRichie_User:
        #created file on pc to store passwords
        with open("../../br_coding_users.json") as password_file:
            password_data = json.load(password_file)
            my_email = password_data[Account]["email"]
            my_password = password_data[Account]["password"]
    else:
        #otherwise, prompt the user for details
        my_email = getpass.getuser()
        my_password = getpass.getpass()

    with smtplib.SMTP("smtp.gmail.com") as connection:
    #this is a way of securing a connection to the email server, and encrypts the email
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email_to_send,
            msg=send_message)
else:
    print("No email sent")
