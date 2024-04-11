import datetime
from time import time

medicine = int(input("What's the quantity of the medicine please? "))
amount_per_day = int(input("What's your daily dose? "))
current_amount = medicine

percent_left = 100
while True:
    daily_checks = input("Have you taken your medicine? ")
    print("       ")

    if daily_checks.lower() == "yes":
        current_amount -= amount_per_day
        percent_left = (current_amount / medicine) * 100
        if percent_left <= 0:
            print("Medicine is finished!")
            break
        if percent_left <= 10:
            print("Your medicine is almost out, a gentle reminder to buy one.")
            print("       ")
        else:
            print(f"You have {percent_left:2f}% of medicine left!")
            print("       ")

    if daily_checks.lower() == "no":
        print("It's time to take your medicine!")
        print("       ")

    if daily_checks.lower() != "yes" and daily_checks.lower() != "no":
        print("INVALID INPUT!")
        print("       ")

