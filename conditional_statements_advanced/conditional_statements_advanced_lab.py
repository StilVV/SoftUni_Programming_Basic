"""01. Day of Week"""
# number = int(input())
#
# if number == 1:
#     print("Monday")
# elif number == 2:
#     print("Tuesday")
# elif number == 3:
#     print("Wednesday")
# elif number == 4:
#     print("Thursday")
# elif number == 5:
#     print("Friday")
# elif number == 6:
#     print("Saturday")
# elif number == 7:
#     print("Sunday")
# else:
#     print("Error")
################################################################################################
"""02. Weekend or Working Day"""
# day = input()
#
# if day == "Monday" or \
#         day == "Tuesday" or \
#         day == "Wednesday" or \
#         day == "Thursday" or \
#         day == "Friday":
#     print("Working day")
# elif day == "Saturday" or day == "Sunday":
#     print("Weekend")
# else:
#     print("Error")
#################################################################################################
"""03. Animal Type"""
# animal = input()
#
# if animal == "crocodile" or animal == "tortoise" or animal == "snake":
#     print("reptile")
# elif animal == "dog":
#     print("mammal")
# else:
#     print("unknown")
#################################################################################################
"""04. Personal Titles"""
# age = float(input())
# gender = input()
#
# if age < 16:
#     if gender == "m":
#         print("Master")
#     elif gender == "f":
#         print("Miss")
# else:
#     if gender == "m":
#         print("Mr.")
#     elif gender == "f":
#         print("Ms.")
#################################################################################################
"""05. Small Shop"""
# product = input()
# city = input()
# quantity = float(input())
#
# price = 0
#
# if city == "Sofia":
#     if product == "coffee":
#         price = 0.50
#     elif product == "water":
#         price = 0.80
#     elif product == "beer":
#         price = 1.20
#     elif product == "sweets":
#         price = 1.45
#     elif product == "peanuts":
#         price = 1.60
#
# elif city == "Plovdiv":
#     if product == "coffee":
#         price = 0.40
#     elif product == "water":
#         price = 0.70
#     elif product == "beer":
#         price = 1.15
#     elif product == "sweets":
#         price = 1.30
#     elif product == "peanuts":
#         price = 1.50
#
# elif city == "Varna":
#     if product == "coffee":
#         price = 0.45
#     elif product == "water":
#         price = 0.70
#     elif product == "beer":
#         price = 1.10
#     elif product == "sweets":
#         price = 1.35
#     elif product == "peanuts":
#         price = 1.55
#
# total = quantity * price
#
# print(total)
#################################################################################################
""""07.Working Hours"""
# hour = int(input())
# day = (input())
#
# if 10 <= hour <= 18 and day != "Sunday":
#     print("open")
# else:
#     print("closed")
#################################################################################################
"""08.Cinema Ticket"""
# day = input()
#
# price = 0
#
# if day == "Monday" or day == "Tuesday" or day == "Friday":
#     price = 12
# elif day == "Wednesday" or day == "Thursday":
#     price = 14
# else:
#     price = 16
#
# print(price)
#################################################################################################
"""09. Fruit or Vegetable"""
# product = input()
#
# if product == "banana" or \
#         product == "apple" or \
#         product == "kiwi" or \
#         product == "cherry" or \
#         product == "lemon" or \
#         product == "grapes":
#     print("fruit")
#
# elif product == "tomato" or \
#         product == "cucumber" or \
#         product == "pepper" or \
#         product == "carrot":
#     print("vegetable")
#
# else:
#     print("unknown")
#################################################################################################
"""10. Invalid Number"""
# number = int(input())
#
# if number == 0 or 100 <= number <= 200:
#     pass
# else:
#     print("invalid")
#################################################################################################
""""11. Fruit Shop"""
# fruit = input()
# day = input()
# quantity = float(input())
# price = 0
#
# if day == "Monday" or day == "Tuesday" \
#         or day == "Wednesday" \
#         or day == "Thursday" \
#         or day == "Friday":
#     if fruit == "banana":
#         price = 2.50
#     elif fruit == "apple":
#         price = 1.20
#     elif fruit == "orange":
#         price = 0.85
#     elif fruit == "grapefruit":
#         price = 1.45
#     elif fruit == "kiwi":
#         price = 2.70
#     elif fruit == "pineapple":
#         price = 5.50
#     elif fruit == "grapes":
#         price = 3.85
#
# elif day == "Saturday" or day == "Sunday":
#     if fruit == "banana":
#         price = 2.70
#     elif fruit == "apple":
#         price = 1.25
#     elif fruit == "orange":
#         price = 0.90
#     elif fruit == "grapefruit":
#         price = 1.60
#     elif fruit == "kiwi":
#         price = 3.00
#     elif fruit == "pineapple":
#         price = 5.60
#     elif fruit == "grapes":
#         price = 4.20
#
# if price * quantity == 0.00:
#     print("error")
# else:
#     print(f'{price * quantity:.2f}')
################################################################################################
"""12. Trade Commissions"""
# city = input()
# sales = float(input())
#
# commission = 0
# is_invalid_input = False
#
# if city == "Sofia":
#     if 0 < sales <= 500:
#         commission = 0.05
#     elif 500 < sales <= 1000:
#         commission = 0.07
#     elif 1000 < sales <= 10000:
#         commission = 0.08
#     elif sales > 10000:
#         commission = 0.12
#     else:
#         is_invalid_input = True
#
# elif city == "Varna":
#     if 0 < sales <= 500:
#         commission = 0.045
#     elif 500 < sales <= 1000:
#         commission = 0.075
#     elif 1000 < sales <= 10000:
#         commission = 0.10
#     elif sales > 10000:
#         commission = 0.13
#     else:
#         is_invalid_input = True
#
# elif city == "Plovdiv":
#     if 0 < sales <= 500:
#         commission = 0.055
#     elif 500 < sales <= 1000:
#         commission = 0.08
#     elif 1000 < sales <= 10000:
#         commission = 0.12
#     elif sales > 10000:
#         commission = 0.145
#     else:
#         is_invalid_input = True
# else:
#     is_invalid_input = True
#
# if is_invalid_input:
#     print("error")
# else:
#     print(f"{sales * commission:.2f}")
