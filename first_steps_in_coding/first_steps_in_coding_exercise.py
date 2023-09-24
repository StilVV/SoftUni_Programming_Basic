"""01. USD to BGN"""
# usd = float(input())
# bgn = usd * 1.79549
# print(bgn)
######################################################################################################################
"""02. Radians to Degrees"""
# from math import pi
#
# radians = float(input())
#
# angel = radians * 180 / pi
# print(angel)
######################################################################################################################
"""03. Deposit Calculator"""
# deposit = float(input())
# deposit_period = int(input())
# tax = float(input()) / 100
#
# total = deposit + deposit_period * ((deposit * tax) / 12)
#
# print(f"{total:.2f}")
######################################################################################################################
"""04. Vacation books list"""
# pages = int(input())
# pages_for_hour = int(input())
# days = int(input())
#
# total = (pages / pages_for_hour) / days
#
# print(round(total))
######################################################################################################################
"""05. Supplies for School"""
# pens = int(input()) * 5.80
# markers = int(input()) * 7.20
# detergent = int(input()) * 1.20
# discount = int(input()) / 100
#
# total = (pens + markers + detergent)
# total = total - (total * discount)
#
# print(total)
######################################################################################################################
"""06. Repainting"""
# nylon = int(input()) + 2
# paint = int(input())
# thinner = int(input()) * 5
# hours_work = int(input())
#
# materials = (nylon * 1.50) + ((paint + (paint * 0.10)) * 14.50) + thinner + 0.40
# worker = hours_work * (materials * 0.30)
# total = worker + materials
#
# print(f"{total:.2f}")
######################################################################################################################
"""07. Food Delivery"""
# chicken_menu = int(input()) * 10.35
# fish_menu = int(input()) * 12.40
# vegetarian_menu = int(input()) * 8.15
#
# account = chicken_menu + fish_menu + vegetarian_menu
# dessert = account * 0.20
# total_account = account + dessert
# delivery = 2.50
#
# print(f"{total_account + delivery:.2f}")
######################################################################################################################
"""08. Basketball Equipment"""
# yearly_price = int(input())
#
# shoes = yearly_price * 0.60
# outfit = shoes * 0.80
# ball = outfit / 4
# accessories = ball / 5
#
# total = yearly_price + shoes + outfit + ball + accessories
#
# print(total)
######################################################################################################################
"""09. Fish Tank"""
# length = int(input())
# width = int(input())
# height = int(input())
# sand_percent = float(input()) / 100
#
# area = (length * width * height) * 0.001
# filled = area * (1 - sand_percent)
#
# print(filled)
