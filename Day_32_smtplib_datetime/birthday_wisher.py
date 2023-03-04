import datetime as dt
import pandas as pd
import random
#from siuba import *


#define file path
dir_fp = "Day_32_smtplib_datetime/"

def birthday_wisher():
    #get today's month and day
    today_month = dt.datetime.now().month
    today_day = dt.datetime.now().day
    
    #filter birthday dataset for bdays with the current month/day
    birthdays = pd.DataFrame(pd.read_csv(dir_fp+"birthdays.csv"))
    
    today_birthdays = birthdays[(birthdays.month==today_month)&(birthdays.day==today_day)]

    #loop through list of birthdays
   
    for index in today_birthdays.iterrows():
        random_letter = random.randint(1,3)
        letter_fp = f"{dir_fp}birthday_letter_templates/letter_{random_letter}.txt"
        with open(letter_fp) as letter_file:
            contents = letter_file.read()
            #TODO change this so it actually loops through the current birthdays
            name_bday = select(today_birthdays, _.name).iloc[0].item()
            email_bday = select(today_birthdays, _.email).iloc[0].item()
            new_contents = contents.replace("[NAME]",name_bday)
            #print(index)
            return(email_bday, new_contents)
            
    

