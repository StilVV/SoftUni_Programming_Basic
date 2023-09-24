"""01. Sum Seconds"""
# first_time = int(input())
# second_time = int(input())
# third_time = int(input())
#
# total_time = first_time + second_time + third_time
# minutes = total_time // 60
# seconds = total_time % 60
#
# if seconds < 10:
#     print(f"{minutes}:0{seconds}")
# else:
#     print(f"{minutes}:{seconds}")
######################################################################################################################
"""02. Bonus Score"""
# points = int(input())
#
# bonus = 0
#
# if points < 100:
#     bonus = 5
# elif points > 1000:
#     bonus = points * 0.10
# else:
#     bonus = points * 0.20
#
# if points % 2 == 0:
#     bonus += 1
# elif points % 10 == 5:
#     bonus += 2
#
# print(bonus)
# print(bonus + points)
######################################################################################################################
"""03. Time + 15 Minutes"""
# hours = int(input())
# minutes = int(input()) + 15
#
# if minutes >= 60:
#     hours += 1
#     minutes -= 60
# if hours > 23:
#     hours = hours - 24
#
# if minutes < 10:
#     print(f"{hours}:0{minutes}")
# else:
#     print(f"{hours}:{minutes}")
######################################################################################################################
"""04. Toy Shop"""
# budget = float(input())
# puzzles = int(input())
# dolls = int(input())
# bears = int(input())
# minions = int(input())
# trucks = int(input())
#
# total_sale = (puzzles * 2.60) + (dolls * 3) + (bears * 4.10) + (minions * 8.20) + (trucks * 2)
# all_toys = puzzles + dolls + bears + minions + trucks
#
# if all_toys >= 50:
#     total_sale *= 0.75
#
# rent = total_sale * 0.10
# money_left = total_sale - rent
#
# if money_left >= budget:
#     print(f"Yes! {abs(budget - money_left):.2f} lv left.")
# else:
#     print(f"Not enough money! {abs(budget - money_left):.2f} lv needed.")
######################################################################################################################
"""05. Godzilla vs. Kong"""
# budget = float(input())
# extras = int(input())
# clothes = float(input())
#
# decor = budget * 0.10
#
# if extras > 150:
#     clothes *= 0.90
#
# total = (clothes * extras) + decor
#
# if budget >= total:
#     print(f"Action!" )
#     print(f"Wingard starts filming with {budget - total:.2f} leva left.")
# else:
#     print("Not enough money!")
#     print(f"Wingard needs {total - budget:.2f} leva more.")
######################################################################################################################
"""06. World Swimming Record"""
# from math import floor
# record = float(input())
# distance = float(input())
# time_for_meter = float(input())
#
# delay = floor(distance / 15) * 12.50
# total_time = delay + (distance * time_for_meter)
#
# if total_time < record:
#     print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
# else:
#     print(f"No, he failed! He was {total_time - record:.2f} seconds slower.")
######################################################################################################################
"""07. Shopping"""
# budget = float(input())
# video_cards = int(input())
# processors = int(input())
# ram = int(input())
#
# video_cards_price = 250 * video_cards
# processors_price = (video_cards_price * 0.35) * processors
# ram_price = (video_cards_price * 0.10) * ram
#
# total = video_cards_price + processors_price + ram_price
#
# if video_cards > processors:
#     total *= 0.85
#
# if budget >= total:
#     print(f"You have {budget - total:.2f} leva left!")
# else:
#     print(f"Not enough money! You need {total - budget:.2f} leva more!")
######################################################################################################################
"""08. Lunch Break"""
# from math import ceil
# name = input()
# episode = int(input())
# lunch_break = int(input())
#
# lunch = lunch_break / 8
# relax = lunch_break / 4
# total_break = lunch_break - (lunch + relax)
#
# if episode <= total_break:
#     print(f"You have enough time to watch {name} and left with {ceil(total_break - episode)} minutes free time.")
# else:
#     print(f"You don't have enough time to watch {name}, you need {ceil(episode - total_break)} more minutes.")
