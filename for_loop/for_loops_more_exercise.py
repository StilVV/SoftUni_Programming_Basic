"""01. Back To The Past"""
# heritage = float(input())
# year = int(input())
#
# age = 18
#
# for i in range(1800, year + 1):
#     if i % 2 == 0:
#         heritage -= 12000
#     else:
#         heritage -= 12000 + (age * 50)
#     age += 1
#
# if heritage >= 0:
#     print(f"Yes! He will live a carefree life and will have {heritage:.2f} dollars left.")
# else:
#     print(f"He will need {abs(heritage):.2f} dollars to survive.")
#######################################################################################################################
"""02. Hospital"""
# period = int(input())
#
# doctors = 7
# checked_patients = 0
# not_checked_patients = 0
#
# for day in range(1, period + 1):
#     number_of_patients = int(input())
#
#     if day % 3 == 0:
#         if checked_patients < not_checked_patients:
#             doctors += 1
#
#     if number_of_patients <= doctors:
#         checked_patients += number_of_patients
#     else:
#         not_checked_patients += number_of_patients - doctors
#         checked_patients += doctors
#
# print(f"Treated patients: {checked_patients}.")
# print(f"Untreated patients: {not_checked_patients}.")
#######################################################################################################################
"""03. Logistics"""
# number_of_shipments = int(input())
#
# weight_price = 0
# total_weight = 0
# microbus = 0
# truck = 0
# train = 0
#
# for shipment in range(number_of_shipments):
#     weight = int(input())
#     total_weight += weight
#
#     if weight <= 3:
#         microbus += weight
#         weight_price += 200 * weight
#     elif 4 <= weight <= 11:
#         weight_price += 175 * weight
#         truck += weight
#     else:
#         weight_price += 120 * weight
#         train += weight
#
# print(f"{weight_price / total_weight:.2f}")
# print(f"{microbus / total_weight * 100:.2f}%")
# print(f"{truck / total_weight * 100:.2f}%")
# print(f"{train / total_weight * 100:.2f}%")
#######################################################################################################################
"""04. Grades"""
# students = int(input())
#
# fail = 0
# middle = 0
# above_avr = 0
# top = 0
# total_marks = 0
# avr_mark = 0
#
# for student in range(students):
#     mark = float(input())
#     avr_mark += mark
#     total_marks += 1
#
#     if 2 <= mark <= 2.99:
#         fail += 1
#     elif 3 <= mark <= 3.99:
#         middle += 1
#     elif 4 <= mark <= 4.99:
#         above_avr += 1
#     elif mark >= 5:
#         top += 1
#
# print(f"Top students: {top / total_marks * 100:.2f}%")
# print(f"Between 4.00 and 4.99: {above_avr / total_marks * 100:.2f}%")
# print(f"Between 3.00 and 3.99: {middle / total_marks * 100:.2f}%")
# print(f"Fail: {fail / total_marks * 100:.2f}%")
# print(f"Average: {avr_mark / total_marks:.2f}")
#######################################################################################################################
"""05. Game Of Intervals"""
# moves = int(input())
#
# points = 0
# between_0_9 = 0
# between_10_19 = 0
# between_20_29 = 0
# between_30_39 = 0
# between_40_50 = 0
# invalid = 0
#
# for move in range(moves):
#     number = int(input())
#
#     if 0 <= number <= 9:
#         points += number * 0.20
#         between_0_9 += 1
#     elif 10 <= number <= 19:
#         points += number * 0.30
#         between_10_19 += 1
#     elif 20 <= number <= 29:
#         points += number * 0.40
#         between_20_29 += 1
#     elif 30 <= number <= 39:
#         points += 50
#         between_30_39 += 1
#     elif 40 <= number <= 50:
#         points += 100
#         between_40_50 += 1
#     if number < 0 or number > 50:
#         points /= 2
#         invalid += 1
#
# print(f"{points:.2f}")
# print(f"From 0 to 9: {between_0_9 / moves * 100:.2f}%")
# print(f"From 10 to 19: {between_10_19 / moves * 100:.2f}%")
# print(f"From 20 to 29: {between_20_29 / moves * 100:.2f}%")
# print(f"From 30 to 39: {between_30_39 / moves * 100:.2f}%")
# print(f"From 40 to 50: {between_40_50 / moves * 100:.2f}%")
# print(f"Invalid numbers: {invalid / moves * 100:.2f}%")
#######################################################################################################################
"""06. Bills"""
# months = int(input())
#
# total_water = 0
# total_internet = 0
# total_electricity = 0
# total_others = 0
#
# for month in range(months):
#     electricity = float(input())
#
#     total_electricity += electricity
#     water = 20
#     total_water += water
#     internet = 15
#     total_internet += internet
#     others = ((water + electricity + internet) * 0.20) + (water + electricity + internet)
#     total_others += others
#
# total = total_others + total_electricity + total_internet + total_water
#
# print(f"Electricity: {total_electricity:.2f} lv")
# print(f"Water: {total_water:.2f} lv")
# print(f"Internet: {total_internet:.2f} lv")
# print(f"Other: {total_others:.2f} lv")
# print(f"Average: {total / months:.2f} lv")
#######################################################################################################################
"""07. Football League"""
# capacity = int(input())
# number_of_fans = int(input())
#
# sector_a = 0
# sector_b = 0
# sector_v = 0
# sector_g = 0
#
# for fan in range(number_of_fans):
#     sector = input()
#
#     if sector == "A":
#         sector_a += 1
#     elif sector == "B":
#         sector_b += 1
#     elif sector == "V":
#         sector_v += 1
#     elif sector == "G":
#         sector_g += 1
#
# print(f"{sector_a / number_of_fans * 100:.2f}%")
# print(f"{sector_b / number_of_fans * 100:.2f}%")
# print(f"{sector_v / number_of_fans * 100:.2f}%")
# print(f"{sector_g / number_of_fans * 100:.2f}%")
# print(f"{number_of_fans / capacity * 100:.2f}%")
#######################################################################################################################
"""08. Equal Pairs"""
# from sys import maxsize
# pairs = int(input())
#
# max_diff = -maxsize
# last_sum = -maxsize
#
# for pair in range(pairs):
#     number_1 = int(input())
#     number_2 = int(input())
#
#     current_pairs_sum = number_2 + number_1
#
#     if pair == 0:
#         last_sum = current_pairs_sum
#         continue
#
#     if last_sum != current_pairs_sum:
#         if abs(current_pairs_sum - last_sum) > max_diff:
#             max_diff = abs(current_pairs_sum - last_sum)
#
#         last_sum = current_pairs_sum
#
# if max_diff == -maxsize:
#     print(f"Yes, value={last_sum}")
# else:
#     print(f"No, maxdiff={max_diff}")
#######################################################################################################################
"""09. Clock"""
# for h in range(24):
#     for m in range(60):
#         print(f"{h} : {m}")
#######################################################################################################################
"""10. Clock - part 2"""
# for h in range(24):
#     for m in range(60):
#         for s in range(60):
#             print(f"{h} : {m} : {s}")
#######################################################################################################################
"""11. Odd / Even Position"""
# from sys import maxsize
#
# number = int(input())
#
# odd_sum = 0
# odd_min = maxsize
# odd_max = -maxsize
# even_sum = 0
# even_min = maxsize
# even_max = -maxsize
#
# for i in range(1, number + 1):
#     number_input = float(input())
#
#     if i % 2 == 0:
#         even_sum += number_input
#         if number_input > even_max:
#             even_max = number_input
#         if number_input < even_min:
#             even_min = number_input
#
#     else:
#         odd_sum += number_input
#         if number_input > odd_max:
#             odd_max = number_input
#         if number_input < odd_min:
#             odd_min = number_input
#
# print(f"OddSum={odd_sum:.2f},")
# if odd_min == maxsize or odd_max == -maxsize:
#     print(f"OddMin=No,")
#     print("OddMax=No,")
# else:
#     print(f"OddMin={odd_min:.2f},")
#     print(f"OddMax={odd_max:.2f},")
#
# print(f"EvenSum={even_sum:.2f},")
# if even_min == maxsize or even_max == -maxsize:
#     print("EvenMin=No,")
#     print("EvenMax=No")
# else:
#     print(f"EvenMin={even_min:.2f},")
#     print(f"EvenMax={even_max:.2f}")
