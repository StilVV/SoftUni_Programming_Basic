"""01. Numbers from 1 to 100"""
# for i in range(1, 101):
#     print(i)
#######################################################################################################################
"""02. Numbers 1...N with Step 3"""
# number = int(input())
#
# for i in range(1,number + 1, 3):
#     print(i)
#######################################################################################################################
"""03. Even Powers of 2"""
# from math import pow
#
# number = int(input())
#
# for i in range(0, number + 1, 2):
#     print(int(pow(2, i)))
#######################################################################################################################
"""04. Numbers N...1"""
# number = int(input())
#
# for i in range(number, 0, -1):
#     print(i)
#######################################################################################################################
"""05. Character Sequence"""
# word = input()
#
# for char in word:
#     print(char)
#######################################################################################################################
"""06. Vowels Sum"""
# word = input()
#
# total_sum = 0
#
# for char in word:
#     if char == "a":
#         total_sum += 1
#     elif char == "e":
#         total_sum += 2
#     elif char == "i":
#         total_sum += 3
#     elif char == "o":
#         total_sum += 4
#     elif char == "u":
#         total_sum += 5
#
# print(total_sum)
#######################################################################################################################
"""07. Sum Numbers"""
# numbers_to_sum = int(input())
#
# total_sum = 0
#
# for number in range(numbers_to_sum):
#     add_number = int(input())
#     total_sum += add_number
#
# print(total_sum)
#######################################################################################################################
"""08. Number sequence"""
# from sys import maxsize
#
# total_numbers = int(input())
#
# min_number = maxsize
# max_number = -maxsize
#
# for number in range(total_numbers):
#     new_number = int(input())
#
#     if new_number > max_number:
#         max_number = new_number
#     if new_number < min_number:
#         min_number = new_number
#
# print(f"Max number: {max_number}")
# print(f"Min number: {min_number}")
#######################################################################################################################
"""09. Left and Right Sum"""
# number = int(input())
#
# left_sum = 0
# right_sum = 0
#
# for i in range(0, number):
#     num = int(input())
#     left_sum += num
#
# for i in range(0, number):
#     num = int(input())
#     right_sum += num
#
# if left_sum == right_sum:
#     print(f"Yes, sum = {left_sum}")
# else:
#     print(f"No, diff = {abs(left_sum - right_sum)}")
#######################################################################################################################
"""10. Odd Even Sum"""
# total_numbers = int(input())
#
# even_sum = 0
# odd_sum = 0
#
# for i in range(1, total_numbers + 1):
#     number = int(input())
#
#     if i % 2 == 0:
#         even_sum += number
#     else:
#         odd_sum += number
#
# if even_sum == odd_sum:
#     print("Yes")
#     print(f"Sum = {even_sum}")
# else:
#     print("No")
#     print(f"Diff = {abs(even_sum - odd_sum)}")
