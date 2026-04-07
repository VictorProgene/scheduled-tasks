from random import randint
import pandas as pd
import datetime as dt
import smtplib
import os


MY_EMAIL = os.getenv("FROM_MY_EMAIL")
MY_PASSWORD = os.getenv("PASSWORD")
# from main import birthday

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

df = pd.read_csv("birthdays.csv")
birthday_dict = df.to_dict(orient="records")
birthday_list = list(birthday_dict)
# print(birthday_list)
counter = 0
for _ in birthday_list:
    letter = randint(1, 3)


    # Person info
    name = birthday_list[counter]["name"]
    email = birthday_list[counter]["email"]
    day = birthday_list[counter]["day"]
    month = birthday_list[counter]["month"]
    year = birthday_list[counter]["year"]
    day_int = int(day)
    month_int = int(month)
    year_int = int(year)

    # Datetime info
    now = dt.datetime.now()
    current_year = now.year
    current_month = now.month
    current_day = now.day


    if (day_int == current_day) and (month_int == current_month):
        file = open(f"./letter_templates/letter_{letter}.txt", "r")
        letter = file.read()

        new_letter = letter.replace("[NAME],", f"{name.strip()},")
        # print(new_letter)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(FROM_MY_EMAIL, PASSWORD)
            connection.sendmail(from_addr=FROM_MY_EMAIL, to_addrs=email,
                                msg=f"Subject: Happy birthday Sunshine\n\n{new_letter}")


    counter += 1
