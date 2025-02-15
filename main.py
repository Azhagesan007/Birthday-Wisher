import pandas
import datetime as dt
import smtplib
import random

data = pandas.read_csv(filepath_or_buffer="birthdays.csv")
# print(data[data["year"] == 2003]["day"].values[0])

current = dt.datetime.now()
month = current.month
day = current.day
# print(month)
# print(day)
birthday_month = [j["month"] for i, j in data.iterrows()]
birthday_day = [j["day"] for i, j in data.iterrows()]
birthday_name = [j["name"] for i, j in data.iterrows()]
birthday_email = [j["email"] for i, j in data.iterrows()]
letter_list = [f"letter_{m}.txt" for m in range(1,4)]
# print(letter_list)


if month in birthday_month and day in birthday_day:
    i = data[data["month"] == month]
    j = data[data["day"] == day]
    today_bithday_email = j["email"].values
    today_bithday_name = j["name"].values
    mail = smtplib.SMTP("smtp.gmail.com")
    mail.starttls()
    mail.login(user="Your Mail", password="Your Password")
    for mails in range(0, len(today_bithday_email)):
        letter = random.choice(letter_list)
        with open(file=f"./letter_templates/{letter}") as file:
            letter_data = file.read()
            letter_withname = letter_data.replace("[NAME]", today_bithday_name[mails])
            mail.sendmail(from_addr="Your mail",
                          to_addrs=today_bithday_email[mails],
                          msg=f"Subject: Happy Birthday \n\n {letter_withname}")

    mail.close()
