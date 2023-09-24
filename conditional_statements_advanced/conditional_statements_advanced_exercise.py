"""01. Cinema"""
# screen_type = input()
# rows = int(input())
# columns = int(input())
#
# price = 0
#
# if screen_type == "Premiere":
#     price = 12
# elif screen_type == "Normal":
#     price = 7.50
# elif screen_type == "Discount":
#     price = 5
#
# total = (rows * columns) * price
#
# print(f"{total:.2f} leva")
#################################################################################################
"""02. Summer Outfit"""
# degrees = int(input())
# time = input()
#
# outfit = ""
# shoes = ""
#
# if time == "Morning":
#     if 10 <= degrees <= 18:
#         outfit = "Sweatshirt"
#         shoes = "Sneakers"
#     elif 18 < degrees <= 24:
#         outfit = "Shirt"
#         shoes = "Moccasins"
#     elif degrees >= 25:
#         outfit = "T-Shirt"
#         shoes = "Sandals"
#
# elif time == "Afternoon":
#     if 10 <= degrees <= 18:
#         outfit = "Shirt"
#         shoes = "Moccasins"
#     elif 18 < degrees <= 24:
#         outfit = "T-Shirt"
#         shoes = "Sandals"
#     elif degrees >= 25:
#         outfit = "Swim Suit"
#         shoes = "Barefoot"
#
# elif time == "Evening":
#     if 10 <= degrees <= 18:
#         outfit = "Shirt"
#         shoes = "Moccasins"
#     elif 18 < degrees <= 24:
#         outfit = "Shirt"
#         shoes = "Moccasins"
#     elif degrees >= 25:
#         outfit = "Shirt"
#         shoes = "Moccasins"
#
# print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
#################################################################################################
"""03. New House"""
# flower = input()
# number_of_flowers = int(input())
# budget = int(input())
#
# rose = 5
# dahlia = 3.80
# tulip = 2.80
# narcissus = 3
# gladiolus = 2.50
# price = 0
#
# if flower == "Roses":
#     price = rose * number_of_flowers
#     if number_of_flowers > 80:
#         price *= 0.90
#
# elif flower == "Dahlias":
#     price = dahlia * number_of_flowers
#     if number_of_flowers > 90:
#         price *= 0.85
#
# elif flower == "Tulips":
#     price = tulip * number_of_flowers
#     if number_of_flowers > 80:
#         price *= 0.85
#
# elif flower == "Narcissus":
#     price = narcissus * number_of_flowers
#     if number_of_flowers < 120:
#         price *= 1.15
#
# elif flower == "Gladiolus":
#     price = gladiolus * number_of_flowers
#     if number_of_flowers < 80:
#         price *= 1.20
#
# budget -= price
#
# if budget >= 0:
#     print(f"Hey, you have a great garden with {number_of_flowers} {flower} and {budget:.2f} leva left.")
# else:
#     print(f"Not enough money, you need {abs(budget):.2f} leva more.")
################################################################################################
"""04. Fishing Boat"""
# budget = int(input())
# season = input()
# fishers = int(input())
#
# price = 0
#
# if season == "Spring":
#     price = 3000
# elif season == "Summer" or season == "Autumn":
#     price = 4200
# elif season == "Winter":
#     price = 2600
#
# if fishers <= 6:
#     price *= 0.90
#
# elif 7 <= fishers <= 11:
#     price *= 0.85
# else:
#     price *= 0.75
#
# if fishers % 2 == 0 and season != "Autumn":
#     price *= 0.95
#
# budget -= price
#
# if budget >= 0:
#     print(f"Yes! You have {budget:.2f} leva left.")
# else:
#     print(f"Not enough money! You need {abs(budget):.2f} leva.")
#################################################################################################
"""05. Journey"""
# budget = float(input())
# season = input()
#
# destination = ""
# stay = ""
# price = 0
#
# if budget > 1000:
#     destination = "Europe"
#     stay = "Hotel"
#     price = budget * 0.90
#
# elif season == "winter":
#     stay = "Hotel"
#     if budget <= 100:
#         destination = "Bulgaria"
#         price = budget * 0.70
#     elif 100 < budget <= 1000:
#         destination = "Balkans"
#         price = budget * 0.80
#
# elif season == "summer":
#     stay = "Camp"
#     if budget <= 100:
#         destination = "Bulgaria"
#         price = budget * 0.30
#     elif 100 < budget <= 1000:
#         destination = "Balkans"
#         price = budget * 0.40
#
# print(f"Somewhere in {destination}")
# print(f"{stay} - {price:.2f}")
#################################################################################################
"""06. Operations Between Numbers"""
# first_number = int(input())
# second_number = int(input())
# operator = input()
#
# result = None
#
# if operator == "+":
#     result = f"{first_number} + {second_number} = {first_number + second_number}" + (" - even" if (first_number + second_number) % 2 == 0 else " - odd")
# elif operator == "-":
#     result = f"{first_number} - {second_number} = {first_number - second_number}" + (" - even" if (first_number - second_number) % 2 == 0 else " - odd")
# elif operator == "*":
#     result = f"{first_number} * {second_number} = {first_number * second_number}" + (" - even" if (first_number * second_number) % 2 == 0 else " - odd")
# elif second_number == 0:
#     result = f"Cannot divide {first_number} by zero"
# elif operator == "/":
#     result = f"{first_number} / {second_number} = {first_number / second_number:.2f}"
# elif operator == "%":
#     result = f"{first_number} % {second_number} = {first_number % second_number}"
#
# print(result)
##################################################################################################
"""07. Hotel Room"""
# month = input()
# days = int(input())
#
# studio = 0
# apartment = 0
#
# if month == "May" or month == "October":
#     studio = 50
#     apartment = 65
#     if 7 < days <= 14:
#         studio *= 0.95
#     elif days > 14:
#         studio *= 0.70
#
# elif month == "June" or month == "September":
#     studio = 75.20
#     apartment = 68.70
#     if days > 14:
#         studio *= 0.80
#
# elif month == "July" or month == "August":
#     studio = 76
#     apartment = 77
#
# if days > 14:
#     apartment *= 0.90
#
# print(f"Apartment: {days * apartment:.2f} lv.")
# print(f"Studio: {days * studio:.2f} lv.")
#################################################################################################
"""08. On Time for the Exam"""
# exam_hours = int(input())
# exam_minutes = int(input())
# student_hour = int(input())
# student_minutes = int(input())
#
# exam_time_in_minutes = exam_hours * 60 + exam_minutes
# student_time_in_minutes = student_hour * 60 + student_minutes
# time_diff = exam_time_in_minutes - student_time_in_minutes
#
# if time_diff > 30:
#     print("Early")
# elif time_diff < 0:
#     print("Late")
# else:
#     print("On time")
#
# hours = 0
# minutes = abs(time_diff)
#
# if minutes >= 60:
#     hours = minutes // 60
#     minutes = minutes % 60
#
# result = ""
#
# if hours > 0:
#     result += str(hours) + ":" + ("0" + str(minutes) if minutes < 10 else str(minutes)) + " hours"
# else:
#     result += str(minutes) + " minutes"
#
# if time_diff > 0:
#     result += " before the start"
# else:
#     result += " after the start"
#
# print(result)
#################################################################################################
"""09. Ski Trip"""
# nights = int(input()) - 1
# room = input()
# mark = input()
#
# price = 0
#
# if room == "room for one person":
#     price = nights * 18
#
# elif room == "apartment":
#     price = nights * 25
#     if nights < 10:
#         price *= 0.70
#     elif 10 <= nights <= 15:
#         price *= 0.65
#     else:
#         price *= 0.50
#
# elif room == "president apartment":
#     price = nights * 35
#     if nights < 10:
#         price *= 0.90
#     elif 10 <= nights <= 15:
#         price *= 0.85
#     else:
#         price *= 0.80
#
# if mark == "positive":
#     price *= 1.25
# else:
#     price *= 0.90
#
# print(f"{price:.2f}")
