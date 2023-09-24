"""01. Trapeziod Area"""
# from decimal import Decimal
# b1 = float(input())
# b2 = float(input())
# h = float(input())
#
# s = (b1 + b2) * h / 2
# s1 = Decimal(s)
#
# print(round(s1, 2))
######################################################################################################################
"""02. Triangle Area"""
# from decimal import Decimal
# a = float(input())
# h = float(input())
#
# area = (a * h) / 2
# area = Decimal(area)
#
# print(round(area, 2))
######################################################################################################################
"""03. Celsius to Fahrenheit"""
# from decimal import Decimal
# celsius = float(input())
#
# convert = celsius * 1.8 + 32
# convert = Decimal(convert)
#
# print(round(convert, 2))
######################################################################################################################
"""04. Vegetable Market"""
# from decimal import Decimal
# vegetables_price = float(input())
# fruit_price = float(input())
# vegetables_kg = int(input())
# fruit_kg = (int(input()))
#
# vegetables_total = vegetables_price * vegetables_kg
# fruit_total = fruit_price * fruit_kg
# total = vegetables_total + fruit_total
# euro = total / 1.94
# euro = Decimal(euro)
#
# print(round(euro, 2))
######################################################################################################################
"""05. Training Lab"""
# width = float((input())) * 100
# height = float(input()) * 100
#
# desk_h = (height - 100) // 70
# desk_w = width // 120
# desks = (desk_w * desk_h) - 3
#
# print(desks)
######################################################################################################################
"""06. Fishland"""
# mackerel_price = float(input())
# caca_price = float(input())
# bonito_kg = float(input())
# safrid_kg = float(input())
# mussels_kg = int(input()) * 7.50
#
# bonito_price = (mackerel_price * 1.60) * bonito_kg
# safrid_price = (caca_price * 1.80) * safrid_kg
# total = bonito_price + safrid_price + mussels_kg
#
# print(f"{total:.2f}")
######################################################################################################################
"""07. House Painting"""
# h_house = float(input())
# a_house = float(input())
# h_roof = float(input())
#
# back_wall = h_house * h_house
# door = 1.20 * 2
# front_wal = back_wall - door
# window = 1.50 * 1.50
# side_walls = ((a_house * h_house) - window) * 2
# roof_walls = 2 * (a_house * h_house)
# roof_sides = 2 * (h_house * h_roof / 2)
#
# walls_paint = (back_wall + front_wal + side_walls) / 3.40
# roof_paint = (roof_walls + roof_sides) / 4.30
#
# print(f'{walls_paint:.2f}')
# print(f'{roof_paint:.2f}')
######################################################################################################################
"""08. Circle Area and Perimeter"""
# from math import pi
# radius = float(input())
#
# perimeter = pi * radius * radius
# area = 2 * (radius * pi)
#
# print(f'{perimeter:.2f}')
# print(f'{area:.2f}')
######################################################################################################################
"""09. Weather Forecast"""
# weather = input()
#
# if weather == "sunny":
#     print("It's warm outside!")
# else:
#     print("It's cold outside!")
######################################################################################################################
"""10. Weather Forecast - Part 2"""
# degrees = float(input())
#
# if 5 <= degrees < 12:
#     print("Cold")
# elif 12 <= degrees < 15:
#     print("Cool")
# elif 15 <= degrees <= 20:
#     print("Mild")
# elif 20 < degrees < 26:
#     print("Warm")
# elif 26 <= degrees <= 35:
#     print("Hot")
# else:
#     print("unknown")
