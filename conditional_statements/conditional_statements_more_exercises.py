"""01. Pipes In Pool"""
# v = int(input())
# p1 = int(input())
# p2 = int(input())
# h = float(input())
#
# pipe1 = p1 * h
# pipe2 = p2 * h
# volume = pipe1 + pipe2
#
# pipe1_percent = pipe1 * 100 / volume
# pipe2_percent = pipe2 * 100 / volume
# percent = volume * 100 / v
#
# if volume <= v:
#     print(f"The pool is {percent}% full. Pipe 1: {pipe1_percent}%. Pipe 2: {pipe2_percent}%.")
# else:
#     difference = volume - v
#     print(f"For {h} hours the pool overflows with {difference} liters.")
##################################################################################################
"""02. Sleepy Tom Cat"""
# weekends = int(input())
#
# year_play_needed = 30000
# weekends_play = weekends * 127
# working_days_play = (365 - weekends) * 63
# total_play = weekends_play + working_days_play
#
# diff = year_play_needed - total_play
# hours_diff = abs(diff) // 60
# minutes_diff = abs(diff) % 60
#
# if total_play < year_play_needed:
#     print(f"Tom sleeps well")
#     print(f"{hours_diff} hours and {minutes_diff} minutes less for play")
# else:
#     print(f"Tom will run away")
#     print(f"{hours_diff} hours and {minutes_diff} minutes more for play")
##################################################################################################
"""03. Harvest"""
# from math import ceil, floor
#
# side = int(input())
# grape_for_meter = float(input())
# wine_goal = int(input())
# workers = int(input())
#
#
# total_grapes = side * grape_for_meter
# wine = (total_grapes * 0.40) / 2.5
# wine_for_workers = (wine - wine_goal) / workers
#
# if wine < wine_goal:
#     print(f"It will be a tough winter! More {floor(wine_goal - wine)} liters wine needed.")
# else:
#     print(f"Good harvest this year! Total wine: {ceil(wine)} liters.")
#     print(f"{ceil(wine -wine_goal)} liters left -> {ceil(wine_for_workers)} liters per person.")
##################################################################################################
"""04. Transport Price"""
# from sys import maxsize
# kilometers = int(input())
# day_night = input()
#
# cheapest = maxsize
# price = 0
#
# if kilometers < 20 and day_night == "day":
#     price = 0.79 * kilometers + 0.70
#     if price < cheapest:
#         cheapest = price
#
# elif kilometers < 20 and day_night == "night":
#     price = 0.90 * kilometers + 0.70
#     if price < cheapest:
#         cheapest = price
#
# elif 20 <= kilometers < 100:
#     price = kilometers * 0.09
#     if price < cheapest:
#         cheapest = price
#
# elif kilometers >= 100:
#     price = kilometers * 0.06
#     if price < cheapest:
#         cheapest = price
#
# print(f"{cheapest:.2f}")
##################################################################################################
"""05. Pets"""
# from math import floor, ceil
#
# days = int(input())
# food = int(input())
# dog_eat = float(input())
# cat_eat = float(input())
# turtle_eat = float(input()) / 1000
#
# dog_total = dog_eat * days
# cat_total = cat_eat * days
# turtle_total = turtle_eat * days
# total_eaten = dog_total + cat_total + turtle_total
#
# if total_eaten <= food:
#     print(f"{floor(food - total_eaten)} kilos of food left.")
# else:
#     print(f"{ceil(total_eaten - food)} more kilos of food are needed.")
##################################################################################################
"""06. Flower Shop"""
# from math import floor, ceil
#
# magnolias = int(input()) * 3.25
# hyacinths = int(input()) * 4
# roses = int(input()) * 3.50
# cacti = int(input()) * 8
# present = float((input()))
#
# total = (magnolias + hyacinths + roses + cacti) * 0.95
#
# if total >= present:
#     print(f"She is left with {floor(total - present)} leva.")
# else:
#     print(f"She will have to borrow {ceil(present - total)} leva.")
##################################################################################################
"""07. Fuel Tank"""
# fuel_type = input().lower()
# liters = float(input())
#
# if fuel_type == "diesel" or fuel_type == "gas" or fuel_type == "gasoline":
#     if liters >= 25:
#         print(f"You have enough {fuel_type}.")
#     elif liters < 25:
#         print(f"Fill your tank with {fuel_type}!")
# else:
#     print("Invalid fuel!")
##################################################################################################
"""08. Fuel Tank - Part 2"""
# fuel_type = input()
# liters = float(input())
# discount_card = input()
#
# diesel_price = 2.33
# gasoline_price = 2.22
# gas_price = 0.93
#
# price = 0
#
# if fuel_type == "Gas":
#     if discount_card == "Yes":
#         price = (gas_price - 0.08) * liters
#     else:
#         price = gas_price * liters
#
# elif fuel_type == "Gasoline":
#     if discount_card == "Yes":
#         price = (gasoline_price - 0.18) * liters
#     else:
#         price = gasoline_price * liters
#
# elif fuel_type == "Diesel":
#     if discount_card == "Yes":
#         price = (diesel_price - 0.12) * liters
#     else:
#         price = diesel_price * liters
#
# if 20 <= liters <= 25:
#     price *= 0.92
# elif liters > 25:
#     price *= 0.90
#
# print(f"{price:.2f} lv.")
