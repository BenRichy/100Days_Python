import smtplib
import json
import getpass

BenRichie_User = True
Account = "GMail_App"

if BenRichie_User:
    #created file on pc to store passwords
    with open("../../br_coding_users.json") as password_file:
        password_data = json.load(password_file)
        my_email = password_data[Account]["email"]
        my_password = password_data[Account]["password"]
else:
    my_email = getpass.getuser()
    my_password = getpass.getpass()

with smtplib.SMTP("smtp.gmail.com") as connection:
#this is a way of securing a connection to the email server, and encrypts the email
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="ben_richmond@ntlworld.com",
        msg="Subject:Hello\n\nHello, this is a test.")
