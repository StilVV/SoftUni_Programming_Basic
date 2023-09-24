"""01. Numbers Ending in 7"""
# for i in range(1, 1001):
#     if i % 10 == 7:
#         print(i)
#######################################################################################################################
"""02. Half Sum Element"""
# from sys import maxsize
# num_count = int(input())
#
# summary = 0
# max_number = - maxsize
#
# for i in range(0, num_count):
#     num = int(input())
#     summary += num
#     if num > max_number:
#         max_number = num
#
# if max_number == summary - max_number:
#     print(f"Yes\nSum = {max_number}")
# else:
#     print(f"No\nDiff = {abs(max_number - (summary - max_number))}")
#######################################################################################################################
"""03. Histogram"""
# total_numbers = int(input())
#
# under_200 = 0
# between_200_399 = 0
# between_400_599 = 0
# between_600_799 = 0
# over_800 = 0
#
# for n in range(total_numbers):
#     number = int(input())
#
#     if number < 200:
#         under_200 += 1
#     elif 200 <= number <= 399:
#         between_200_399 += 1
#     elif 400 <= number <= 599:
#         between_400_599 += 1
#     elif 600 <= number <= 799:
#         between_600_799 += 1
#     else:
#         over_800 += 1
#
# print(f"{under_200 / total_numbers * 100:.2f}%")
# print(f"{between_200_399 / total_numbers * 100:.2f}%")
# print(f"{between_400_599 / total_numbers * 100:.2f}%")
# print(f"{between_600_799 / total_numbers * 100:.2f}%")
# print(f"{over_800 / total_numbers * 100:.2f}%")
#######################################################################################################################
"""04. Clever Lily"""
# age = int(input())
# washer = float(input())
# toy = int(input())
#
# toys = 0
# money = 0
#
# for i in range(1, age + 1):
#     if i % 2 == 0:
#         money += 10 * (i / 2)
#         money -= 1
#     else:
#         toys += 1
#
# total = money + (toy * toys)
#
# if total >= washer:
#     print(f"Yes! {total -washer:.2f}")
# else:
#     print(f"No! {washer - total:.2f}")
#######################################################################################################################
"""05. Salary"""
# number_of_tabs = int(input())
# salary = float(input())
#
# for i in range(number_of_tabs):
#     tab_name = input()
#
#     if tab_name == "Facebook":
#         salary -= 150
#     elif tab_name == "Instagram":
#         salary -= 100
#     elif tab_name == "Reddit":
#         salary -= 50
#
#     if salary <= 0:
#         print("You have lost your salary.")
#         break
#
# if salary > 0:
#     print(f"{salary:.0f}")
#######################################################################################################################
"""06. Oscars"""
# actors_name = input()
# academy_points = float(input())
# jury = int(input())
#
# for i in range(jury):
#     jury_name = input()
#     jury_points = float(input())
#
#     academy_points += (len(jury_name) * jury_points) / 2
#
#     if academy_points >= 1250.5:
#         print(f"Congratulations, {actors_name} got a nominee for leading role with {academy_points:.1f}!")
#         break
# else:
#     print(f"Sorry, {actors_name} you need {1250.5 - academy_points:.1f} more!")
#######################################################################################################################
"""07. Trekking Mania"""
# total_climbers = int(input())
#
# all_climbers = 0
# musala = 0
# mont_blanc = 0
# kilimanjaro = 0
# k2 = 0
# everest = 0
#
# for climber in range(total_climbers):
#     climber_group = int(input())
#     all_climbers += climber_group
#
#     if climber_group <= 5:
#         musala += climber_group
#     elif 6 <= climber_group <= 12:
#         mont_blanc += climber_group
#     elif 13 <= climber_group <= 25:
#         kilimanjaro += climber_group
#     elif 26 <= climber_group <= 40:
#         k2 += climber_group
#     elif climber_group >= 41:
#         everest += climber_group
#
# print(f"{(musala / all_climbers * 100):.2f}%")
# print(f"{(mont_blanc / all_climbers * 100):.2f}%")
# print(f"{(kilimanjaro / all_climbers * 100):.2f}%")
# print(f"{(k2 / all_climbers * 100):.2f}%")
# print(f"{(everest / all_climbers * 100):.2f}%")
#######################################################################################################################
"""08. Tennis Ranklist"""
# from math import floor
#
# tournaments = int(input())
# start_points = int(input())
#
# win_points = 0
# win = 0
#
# for i in range(tournaments):
#     w_f_sf = input()
#
#     if w_f_sf == "W":
#         win += 1
#         win_points += 2000
#     elif w_f_sf == "F":
#         win_points += 1200
#     elif w_f_sf == "SF":
#         win_points += 720
#
# print(f"Final points: {start_points + win_points}")
# print(f"Average points: {floor(win_points / tournaments)}")
# print(f"{win / tournaments * 100:.2f}%")
