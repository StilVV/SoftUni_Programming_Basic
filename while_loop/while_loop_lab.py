"""01. Read Text"""
# while True:
#     word = input()
#
#     if word == "Stop":
#         break
#     print(word)
######################################################################################################################
"""02. Password"""
# username = input()
# password = input()
#
# while True:
#     password_check = input()
#
#     if password_check == password:
#         print(f"Welcome {username}!")
#         break
######################################################################################################################
"""03. Sum Numbers"""
# number = int(input())
#
# number_sum = 0
#
# while True:
#     next_number = int(input())
#
#     number_sum += next_number
#
#     if number_sum >= number:
#         print(number_sum)
#         break
######################################################################################################################
"""04. Sequence 2k+1"""
# input = int(input())
#
# count = 1
#
# while count <= input:
#     print(count)
#
#     count = 2 * count + 1
######################################################################################################################
"""05. Account Balance"""
# balance = 0
#
# while True:
#     user_input = input()
#     if user_input == "NoMoreMoney":
#         break
#     money = float(user_input)
#     if money < 0:
#         print("Invalid operation!")
#         break
#     print(f"Increase: {money:.2f}")
#     balance += money
#
# print(f"Total: {balance:.2f}")
######################################################################################################################
"""06. Max Number"""
# from sys import maxsize
#
# max_number = -maxsize
#
# while True:
#     input_word_number = input()
#
#     if input_word_number == "Stop":
#         break
#     else:
#         number = int(input_word_number)
#
#         if number > max_number:
#             max_number = number
#
# print(max_number)
######################################################################################################################
"""07. Min Number"""
# from sys import maxsize
#
# min_number = maxsize
#
# while True:
#     input_word_number = input()
#
#     if input_word_number == "Stop":
#         break
#     else:
#         number = int(input_word_number)
#
#         if number < min_number:
#             min_number = number
#
# print(min_number)
######################################################################################################################
"""08. Graduation"""
# student_name = input()
#
# grade = 1
# fail = 0
# marks = 0
#
# while grade <= 12:
#     mark = float(input())
#
#     if mark < 4:
#         fail += 1
#         if fail >= 2:
#             break
#         continue
#
#     marks += mark
#     grade += 1
#
# if fail >= 2:
#     print(f"{student_name} has been excluded at {grade} grade")
# else:
#     print(f"{student_name} graduated. Average grade: {marks / 12:.2f}")
