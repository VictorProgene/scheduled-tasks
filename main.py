from random import randint
import pandas as pd
import datetime as dt
import smtplib
import os



from_my_email = os.environ.get("from_my_email")
passwword = os.environ.get("passwword")

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
            connection.login(from_my_email, passwword)
            connection.sendmail(from_addr=from_my_email, to_addrs=email,
                                msg=f"Subject: Happy birthday Sunshine\n\n{new_letter}")


    counter += 1
