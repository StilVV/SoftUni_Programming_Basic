""""01. Number Pyramid"""
# number = int(input())
# counter = 0
#
# for row in range(1, number + 1):
#     for col in range(1, row + 1):
#         counter += 1
#
#         print(f"{counter}", end=" ") if row != col else print(f"{counter}")
#
#         if counter == number:
#             raise SystemExit
##################################################################################################
"""02. Equal Sums Even Odd Position"""
# first_number = int(input())
# second_number = int(input())
#
# for number in range(first_number, second_number + 1):
#     current_number = str(number)
#     odd_sum = 0
#     even_sum = 0
#
#     for index, digit in enumerate(current_number):
#         if index % 2 == 0:
#             odd_sum += int(digit)
#         else:
#             even_sum += int(digit)
#
#     if even_sum == odd_sum:
#         print(number, end=" ")
##################################################################################################
"""03. Sum Prime Non Prime"""
# prime_sum = 0
# non_prime_sum = 0
#
# while True:
#     command = input()
#
#     if command == "stop":
#         break
#
#     current_number = int(command)
#     is_prime = True
#
#     if current_number < 0:
#         print("Number is negative.")
#         continue
#
#     for number in range(2, current_number):
#         if current_number % number == 0:
#             is_prime = False
#             break
#
#     if is_prime:
#         prime_sum += current_number
#     else:
#         non_prime_sum += current_number
#
# print(f"Sum of all prime numbers is: {prime_sum}")
# print(f"Sum of all non prime numbers is: {non_prime_sum}")
##################################################################################################
"""04. Train The Trainers"""
# jury = int(input())
# command = input()
#
# total_mark = 0
# marks_count = 0
#
# while command != "Finish":
#     current_mark = 0
#
#     for marks in range(jury):
#         mark = float(input())
#         current_mark += mark
#         marks_count += 1
#
#     total_mark += current_mark
#     print(f"{command} - {current_mark / jury:.2f}.")
#
#     command = input()
#
# avr_mark = total_mark / marks_count
#
# print(f"Student's final assessment is {avr_mark:.2f}.")
##################################################################################################
"""05. Special Numbers"""
# number = int(input())
#
# for special_number in range(1111, 10000):
#     for digit in str(special_number):
#         if digit == "0":
#             break
#         if number % int(digit) != 0:
#             break
#
#     else:
#         print(special_number, end=" ")
##################################################################################################
"""06. Cinema Tickets"""
total_tickets = 0
student = 0
standard = 0
kid = 0

while True:
    movie = input()
    taken_seats = 0

    if movie == "Finish":
        break

    available_seats = int(input())

    while taken_seats < available_seats:
        seat = input()

        if seat == "End":
            break
        elif seat == "student":
            student += 1
        elif seat == "standard":
            standard += 1
        elif seat == "kid":
            kid += 1

        taken_seats += 1

    percentage_taken = taken_seats / available_seats * 100

    print(f"{movie} - {percentage_taken:.2f}% full.")

total_tickets = standard + student + kid

print(f"Total tickets: {total_tickets}")
print(f"{student / total_tickets * 100:.2f}% student tickets.")
print(f"{standard / total_tickets * 100:.2f}% standard tickets.")
print(f"{kid / total_tickets * 100:.2f}% kids tickets.")
