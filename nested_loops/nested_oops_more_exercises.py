"""01. Unique PIN Codes"""
# max_number_1 = int(input())
# max_number2 = int(input())
# max_number3 = int(input())
#
# for num1 in range(2, max_number_1 + 1, 2):
#     for num2 in range(2, max_number2 + 1):
#         for num3 in range(2, max_number3 + 1, 2):
#             if num2 == 2 or num2 == 3 or num2 == 5 or num2 == 7:
#                 print(f"{num1} {num2} {num3}")
######################################################################################################################
"""02. Letters Combinations"""
# first_letter = input()
# second_letter = input()
# spacial_letter = input()
#
# count = 0
#
# for letter1 in range(ord(first_letter), ord(second_letter) + 1):
#     for letter2 in range(ord(first_letter), ord(second_letter) + 1):
#         for letter3 in range(ord(first_letter), ord(second_letter) + 1):
#             if chr(letter1) != spacial_letter and chr(letter2) != spacial_letter and chr(letter3) != spacial_letter:
#                 print(f"{chr(letter1)}{chr(letter2)}{chr(letter3)}", end=" ")
#                 count += 1
#
# print(count)
######################################################################################################################
"""03. Lucky Numbers"""
# number = int(input())
#
# for n in range(1000, 10000):
#     first_sum, second_sum = 0, 0
#
#     for index, digits in enumerate(str(n)):
#         if digits == "0":
#             break
#
#         if index < 2:
#             first_sum += int(digits)
#         else:
#             second_sum += int(digits)
#     else:
#         if first_sum == second_sum and number % first_sum == 0:
#             print(n, end=" ")
#######################################################################################################################
"""04. Car Number"""
# first_number = int(input())
# second_number = int(input())
#
# for num1 in range(first_number, second_number + 1):
#     for num2 in range(first_number, second_number + 1):
#         for num3 in range(first_number, second_number + 1):
#             for num4 in range(first_number, second_number + 1):
#
#                 if (num1 > num4) and (num2 + num3) % 2 == 0:
#
#                     if (num1 % 2 == 0) and num4 % 2 != 0:
#                         print(f"{num1}{num2}{num3}{num4}", end=" ")
#
#                     if num1 % 2 != 0 and num4 % 2 == 0:
#                         print(f"{num1}{num2}{num3}{num4}", end=" ")
######################################################################################################################
"""05. Challenge the Wedding"""
# mens = int(input())
# womens = int(input())
# tables = int(input())
#
# for men in range(1, mens + 1):
#     for women in range(1, womens + 1):
#         print(f"({men} <-> {women})", end=" ")
#         tables -= 1
#         if tables <= 0:
#             break
#     if tables <= 0:
#         break
######################################################################################################################
"""06. Wedding Seats"""
# end_sector = input()
# row_first_sector = int(input())
# seats_odd_row = int(input())
#
# counter = 0
# start_sector = 65
# start_seat = 97
#
# for sector in range(start_sector, ord(end_sector) + 1):
#     for row in range(1, row_first_sector + 1):
#         if row % 2 != 0:
#             for seats in range(start_seat, (start_seat + seats_odd_row)):
#                 print(f'{chr(sector)}{row}{chr(seats)}')
#                 counter += 1
#         elif row % 2 == 0:
#             for seats in range(start_seat, (start_seat + seats_odd_row + 2)):
#                 print(f'{chr(sector)}{row}{chr(seats)}')
#                 counter += 1
#     if row_first_sector + 1 > row_first_sector:
#         row_first_sector += 1
#
# print(counter)
######################################################################################################################
"""07. Safe Passwords Generator"""
# third_symbol = int(input())
# fourth_symbol = int(input())
# max_combinations = int(input())
#
# total_combinations = 0
# first_last_symbol = 35
# second_and_before_last_symbol = 64
#
# for i in range(1, third_symbol + 1):
#     for x in range(1, fourth_symbol + 1):
#         total_combinations += 1
#
#         if total_combinations > max_combinations:
#             break
#         if first_last_symbol > 55:
#             first_last_symbol = 35
#         if second_and_before_last_symbol > 96:
#             second_and_before_last_symbol = 64
#
#         print(f"{chr(first_last_symbol)}{chr(second_and_before_last_symbol)}{i}{x}"
#               f"{chr(second_and_before_last_symbol)}"
#               f"{chr(first_last_symbol)}", end="|")
#
#         first_last_symbol += 1
#         second_and_before_last_symbol += 1
######################################################################################################################
"""08. Secret Door's Lock"""
# upper_limit_1 = int(input())
# upper_limit_2 = int(input())
# upper_limit_3 = int(input())
# is_prime = True
# for first in range(1, upper_limit_1 + 1):
#     for second in range(1, upper_limit_2 + 1):
#         current_number = second
#         is_prime = True
#
#         for number in range(2, current_number):
#             if current_number % number == 0:
#                 is_prime = False
#                 break
#
#         if is_prime:
#             for third in range(1, upper_limit_3 + 1):
#                 if second == 2 or second == 3 or second == 5 or second == 7:
#                     if first % 2 == 0 and third % 2 == 0:
#                         print(first, second, third)
######################################################################################################################
"""09. Sum of Two Numbers"""
# first_number = int(input())
# second_number = int(input())
# magic_number = int(input())
#
# count = 0
# is_fount = False
#
# for number_1 in range(first_number, second_number + 1):
#     for number_2 in range(first_number, second_number + 1):
#         count += 1
#
#         if number_1 + number_2 == magic_number:
#             print(f"Combination N:{count} ({number_1} + {number_2} = {magic_number})")
#             is_fount = True
#             break
#     if is_fount:
#         break
#
# else:
#     print(f"{count} combinations - neither equals {magic_number}")
######################################################################################################################
"""10. Profit"""
# lv_1 = int(input())
# lv_2 = int(input())
# lv_5 = int(input())
# summary = int(input())
#
# current_sum = 0
#
# for one_lev in range(0, lv_1 + 1):
#     for two_leva in range(0, lv_2 + 1):
#         for five_leva in range(0, lv_5 + 1):
#             current_sum = one_lev + two_leva * 2 + five_leva * 5
#
#             if current_sum == summary:
#                 print(f"{one_lev} * 1 lv. + {two_leva} * 2 lv. + {five_leva} * 5 lv. = {summary} lv.")
######################################################################################################################
"""11. HappyCat Parking"""
# days = int(input())
# hours = int(input())
#
# price = 0
# total = 0
#
# for day in range(1, days + 1):
#     for hour in range(1,hours + 1):
#         if day % 2 == 0 and hour % 2 != 0:
#             price += 2.50
#         elif day % 2 != 0 and hour % 2 == 0:
#             price += 1.25
#         else:
#             price += 1
#
#     total += price
#     print(f"Day: {day} - {price:.2f} leva")
#     price = 0
#
# print(f"Total: {total:.2f} leva")
######################################################################################################################
"""12. The song of the wheels"""
# magic_number = int(input())
#
# count = 0
# password = ""
# not_found = False
#
# for first in range(1, 10):
#     for second in range(1, 10):
#         for third in range(1, 10):
#             for forth in range(1, 10):
#
#                 if first < second and third > forth:
#                     if first * second + third * forth == magic_number:
#                         not_found = True
#                         print(f"{first}{second}{third}{forth}", end=" ")
#                         count += 1
#
#                         if count == 4:
#                             password = f"{first}{second}{third}{forth}"
#
# if count >= 4:
#     print(f"\nPassword: {password}")
# elif not_found:
#     print(f"\nNo!")
# else:
#     print(f"No!")
######################################################################################################################
"""13. Prime Pairs"""
# first_beginning = int(input())
# second_beginning = int(input())
# first_limit = int(input())
# second_limit = int(input())
#
# for first in range(first_beginning, (first_beginning + first_limit) + 1):
#     current_number = first
#     is_prime = True
#
#     for number in range(2, current_number):
#         if current_number % number == 0:
#             is_prime = False
#             break
#
#     if is_prime:
#         for second in range(second_beginning, (second_beginning + second_limit) + 1):
#             current_number = second
#             is_prime = True
#
#             for number in range(2, current_number):
#                 if current_number % number == 0:
#                     is_prime = False
#                     break
#
#             if is_prime:
#                 print(f"{first}{second}")
######################################################################################################################
"""14. Password Generator"""
# number = int(input())
# letter = int(input())
#
# for first_number in range(1, number):
#     for second_number in range(1, number):
#         for first_letter in range(ord("a"), ord("a") + letter):
#             for second_letter in range(ord("a"), ord("a") + letter):
#                 for third_number in range(1, number + 1):
#                     if third_number > first_number and third_number > second_number:
#                         print(f"{first_number}{second_number}{chr(first_letter)}{chr(second_letter)}{third_number}",
#                               end=" ")
