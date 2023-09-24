"""01. Old Books"""
# the_book = input()
#
# count = 0
#
# while True:
#     next_book = input()
#
#     if next_book == the_book:
#         print(f"You checked {count} books and found it.")
#         break
#
#     elif next_book == "No More Books":
#         print(f"The book you search is not here!")
#         print(f"You checked {count} books.")
#         break
#
#     count += 1
######################################################################################################################
"""02. Exam Preparation"""
# failed_threshold = int(input())
#
# failed_times = 0
# solved_problems = 0
# grade_sum = 0
# last_problem = ""
# has_failed = True
#
# while failed_times < failed_threshold:
#     problem_name = input()
#
#     if problem_name == "Enough":
#         break
#
#     grade = float(input())
#
#     if grade <= 4:
#         failed_times += 1
#
#     grade_sum += grade
#     last_problem = problem_name
#     solved_problems += 1
#
# if failed_times < failed_threshold:
#     print(f"Average score: {grade_sum / solved_problems:.2f}")
#     print(f"Number of problems: {solved_problems}")
#     print(f"Last problem: {last_problem}")
# else:
#     print(f"You need a break, {failed_times} poor grades.")
######################################################################################################################
"""03. Vacation"""
# vacation_price = float(input())
# balance = float(input())
#
# spend_count = 0
# days = 0
#
# while True:
#     action = input()
#     money = float(input())
#
#     days += 1
#
#     if action == "spend":
#         balance -= money
#         if balance < 0:
#             balance = 0
#         spend_count += 1
#         if spend_count >= 5:
#             break
#
#     elif action == "save":
#         balance += money
#         spend_count = 0
#
#     if balance >= vacation_price:
#         break
#
# if balance >= vacation_price:
#     print(f"You saved the money for {days} days.")
# else:
#     print(f"You can't save the money.")
#     print(f"{days}")
######################################################################################################################
"""04. Walking"""
# goal = 10000
#
# steps_walked = 0
#
# while goal > steps_walked:
#     steps = input()
#
#     if steps == "Going home":
#         last_step = int(input())
#         steps_walked += last_step
#         break
#     else:
#         steps = int(steps)
#
#     steps_walked += steps
#
# if steps_walked >= goal:
#     print(f"Goal reached! Good job!")
#     print(f"{steps_walked - goal} steps over the goal!")
# else:
#     print(f"{goal - steps_walked} more steps to reach goal.")
######################################################################################################################
"""05. Coins"""
# change = round(float(input()) * 100)
#
# coins = 0
#
# while change > 0:
#     if change >= 200:
#         change -= 200
#     elif change >= 100:
#         change -= 100
#     elif change >= 50:
#         change -= 50
#     elif change >= 20:
#         change -= 20
#     elif change >= 10:
#         change -= 10
#     elif change >= 5:
#         change -= 5
#     elif change >= 2:
#         change -= 2
#     elif change >= 1:
#         change -= 1
#
#     coins += 1
#
# print(coins)
######################################################################################################################
"""06. Cake"""
# high = int(input())
# width = int(input())
#
# cake = high * width
#
# while cake > 0:
#     piece = input()
#
#     if piece == "STOP":
#         break
#     else:
#         piece = int(piece)
#
#     cake -= piece
#
# if cake > 0:
#     print(f"{cake} pieces are left.")
# else:
#     print(f"No more cake left! You need {abs(cake)} pieces more.")
######################################################################################################################
"""07. Moving"""
# area = (int(input()) * int(input()) * int(input()))
#
# while area > 0:
#     box = input()
#
#     if box == "Done":
#         break
#     else:
#         box = int(box)
#
#     area -= box
#
# if area > 0:
#     print(f"{abs(area)} Cubic meters left.")
# else:
#     print(f"No more free space! You need {abs(area)} Cubic meters more.")
