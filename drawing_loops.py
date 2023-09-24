""" 01. Rectangle of 10 x 10 Stars """
# for i in range(0, 10):
#     print("*" * 10)
######################################################################################################################
""" 02. Rectangle of N x N Stars """
# user_input = int(input())
# for i in range(0, user_input):
#     print("*" * user_input)
######################################################################################################################
"""" 03. Square of Stars """
# user_input = int(input())
# for i in range(0, user_input):
#     print("* " * user_input)
######################################################################################################################
"""04. Triangle of Dollars"""
# user_input = int(input())
# for i in range(0, user_input):
#     print("$ " * (i + 1))
######################################################################################################################
""" 05. Square Frame """
# user_input = int(input())
#
# for i in range(0, 1):
#     print("+", "- " * (user_input - 2)+"+")
#     for o in range(0, user_input - 2):
#         print("|", "- " * (user_input - 2)+"|")
#     print("+", "- " * (user_input - 2)+"+")
######################################################################################################################
""" 06. Rhombus of Stars """
# user_input = int(input())
# if user_input == 1:
#     print("*")
# else:
#     for i in range(1, user_input + 1):
#         print(" " * (user_input - i) + "* " * i)
#     for e in reversed(range(1, user_input)):
#         print(" " * (user_input - e) + "* " * e)
######################################################################################################################
""" 07. Christmas Tree """
# user_input = int(input())
#
# for i in range(user_input + 1):
#     print(f"{' ' * (user_input - i)}{'*' * i} | {'*' * i}")
######################################################################################################################
"""" 08. Sunglasses """
# count = int(input())
#
# print(f"{'*' * (count * 2)}{' ' * count}{'*' * (count * 2)}")
#
# for i in range(count - 2):
#     if i == (count - 1) // 2 - 1:
#         print(f"*{'/' * (count * 2 - 2)}*{'|' * count}*{'/' * (count * 2 - 2)}*")
#     else:
#         print(f"*{'/' * (count * 2 - 2)}*{' ' * count}*{'/' * (count * 2 - 2)}*")
#
# print(f"{'*' * (count * 2)}{' ' * count}{'*' * (count * 2)}")
######################################################################################################################
""" 09. House """
# user_input = int(input())
#
# for i in range((user_input + 1) // 2):
#     if i == 0:
#         if user_input % 2 == 0:
#             print(f"{'-' * ((user_input - 2) // 2)}**{'-' * ((user_input - 2) // 2)}")
#         else:
#             print(f"{'-' * ((user_input - 1) // 2)}*{'-' * ((user_input - 1) // 2)}")
#     else:
#         if user_input % 2 == 0:
#             print(f"{'-' * ((user_input - (i + 1) * 2) // 2)}{'*' * ((i + 1) * 2)}"
#                   f"{'-' * ((user_input - (i + 1) * 2) // 2)}")
#         else:
#             print(f"{'-' * ((user_input + 1 - (i + 1) * 2) // 2)}{'*' * ((i + 1) * 2 - 1)}"
#                   f"{'-' * ((user_input + 1 - (i + 1) * 2) // 2)}")
#
# for i in range(user_input - (user_input + 1) // 2):
#     print(f"|{'*' * (user_input - 2)}|")
######################################################################################################################
"""" 10. """
# user_input = int(input())
#
# for i in range(1, (user_input + 3) // 2):
#     if (user_input + 1) // 2 >= i:
#         if i == 1:
#             if user_input % 2 == 0:
#                 print(f"{'-' * ((user_input - 2) // 2)}**{'-' * ((user_input - 2) // 2)}")
#             else:
#                 print(f"{'-' * ((user_input - 1) // 2)}*{'-' * ((user_input - 1) // 2)}")
#         else:
#             if user_input % 2 == 0:
#                 print(f"{'-' * ((user_input - (i - 1) * 2 - 2) // 2)}*{'-' * ((i - 1) * 2)}*"
#                       f"{'-' * ((user_input - (i - 1) * 2 - 2) // 2)}")
#             else:
#                 print(f"{'-' * ((user_input - (i - 1) * 2 - 1) // 2)}*{'-' * ((i - 1) * 2 - 1)}*"
#                       f"{'-' * ((user_input - (i - 1) * 2 - 1) // 2)}")
#
# for i in range((user_input - 1) // 2, 0, -1):
#     if (user_input + 1) // 2 >= i:
#         if i == 1:
#             if user_input % 2 == 0:
#                 print(f"{'-' * ((user_input - 2) // 2)}**{'-' * ((user_input - 2) // 2)}")
#             else:
#                 print(f"{'-' * ((user_input - 1) // 2)}*{'-' * ((user_input - 1) // 2)}")
#         else:
#             if user_input % 2 == 0:
#                 print(f"{'-' * ((user_input - (i - 1) * 2 - 2) // 2)}*{'-' * ((i - 1) * 2)}*"
#                       f"{'-' * ((user_input - (i - 1) * 2 - 2) // 2)}")
#             else:
#                 print(f"{'-' * ((user_input - (i - 1) * 2 - 1) // 2)}*{'-' * ((i - 1) * 2 - 1)}*"
#                       f"{'-' * ((user_input - (i - 1) * 2 - 1) // 2)}")
