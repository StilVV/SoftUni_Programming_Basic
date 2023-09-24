"""01. Clock"""
# for hour in range(0, 24):
#     for minutes in range(0, 60):
#         print(f"{hour}:{minutes}")
##################################################################################################
"""02. Multiplication Table"""
# for num1 in range(1, 11):
#     for num2 in range(1, 11):
#         result = num1 * num2
#         print(f"{num1} * {num2} = {result}")
##################################################################################################
"""03. Combinations"""
# number = int(input())
#
# result_count = 0
#
# for num1 in range(0, number + 1):
#     for num2 in range(0, number + 1):
#         for num3 in range(0, number + 1):
#             result = num1 + num2 + num3
#             if result == number:
#                 result_count += 1
#
# print(f"{result_count}")
##################################################################################################
"""04. Sum of Two Numbers"""
# first_number = int(input())
# second_number = int(input())
# the_number = int(input())
#
# count = 0
# found = 0
#
# for num1 in range(first_number, second_number + 1):
#     for num2 in range(first_number, second_number + 1):
#         count += 1
#         if num1 + num2 == the_number:
#             print(f"Combination N:{count} ({num1} + {num2} = {the_number})")
#             found = 1
#             break
#     if found == 1:
#         break
#
# if found < 1:
#     print(f"{count} combinations - neither equals {the_number}")
##################################################################################################
"""05. Travelling"""
# while True:
#     country = input()
#
#     if country == "End":
#         break
#
#     budget = float(input())
#
#     while budget > 0:
#         saves = float(input())
#
#         budget -= saves
#
#     print(f"Going to {country}!")
##################################################################################################
"""06. Building"""
floors = int(input())
rooms = int(input())

room_type = ""

for floor in range(floors, 0 , -1):
    for room in range(0, rooms):
        if floor == floors:
            print(f"L{floor}{room} ", end="")
        elif floor % 2 == 0:
            print(f"O{floor}{room} ", end="")
        else:
            print(f"A{floor}{room} ", end="")

    print("")
