"""01. Dishwasher"""
# detergent = int(input()) * 750
# dishes = 0
# pots = 0
#
# count = 0
#
# while detergent >= 0:
#     washed = input()
#
#     if washed == "End":
#         break
#     else:
#         washed = int(washed)
#         count += 1
#
#     if count % 3 == 0:
#         detergent -= washed * 15
#         pots += washed
#     else:
#         detergent -= washed * 5
#         dishes += washed
#
# if detergent >= 0:
#     print(f"Detergent was enough!")
#     print(f"{dishes} dishes and {pots} pots were washed.")
#     print(f"Leftover detergent {detergent} ml.")
# else:
#     print(f"Not enough detergent, {abs(detergent)} ml. more necessary!")
######################################################################################################################
"""02. Report System"""
# goal = int(input())
#
# card = 0
# cash = 0
# count = 0
# count_cash = 0
# count_card = 0
# total = 0
#
# while total < goal:
#     money = input()
#
#     if money == "End":
#         print("Failed to collect required money for charity.")
#         break
#     else:
#         money = int(money)
#         count += 1
#
#     if count % 2 != 0:
#         if money > 100:
#             print(f"Error in transaction!")
#         else:
#             print("Product sold!")
#             cash += money
#             total += money
#             count_cash += 1
#     else:
#         if money < 10:
#             print("Error in transaction!")
#         else:
#             card += money
#             total += money
#             count_card += 1
#             print("Product sold!")
#
# if total >= goal:
#     print(f"Average CS: {cash / count_cash:.2f}")
#     print(f"Average CC: {card / count_card:.2f}")
######################################################################################################################
"""03. Stream Of Letters"""
# command = []
# secret = ''
# entry = ''
# while entry != 'End':
#     entry = input()
#     if not entry.isalpha():
#         continue
#     if (entry == 'c' or entry == 'o' or entry == 'n') and entry not in command:
#         command.append(entry)
#         entry = ''
#     if 'c' in command and 'o' in command and 'n' in command:
#         print(secret, end=' ')
#         secret = ''
#         command = []
#     else:
#         secret += entry
######################################################################################################################
"""04. Numbers Divided by 3 Without Reminder"""
# number = 0
# while number < 100:
#     number += 1
#     if number % 3 == 0:
#         print(number)
######################################################################################################################
"""05. Average Number"""
# number = int(input())
# total = 0
# count = 0
#
# while number > count:
#     add_number = int(input())
#
#     total += add_number
#     count += 1
#
# print(f"{(total / number):.2f}")
