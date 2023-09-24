"""01. Match Tickets"""
# budget = float(input())
# category = input()
# number_of_fans = int(input())
#
# transport = 0
# price = 0
#
# if 1 <= number_of_fans <= 4:
#     transport = budget * 0.75
# elif 5 <= number_of_fans <= 9:
#     transport = budget * 0.60
# elif 10 <= number_of_fans <= 24:
#     transport = budget * 0.50
# elif 25 <= number_of_fans <= 49:
#     transport = budget * 0.40
# elif number_of_fans >= 50:
#     transport = budget * 0.25
#
# if category == "VIP":
#     price = 499.99
# elif category == "Normal":
#     price = 249.99
#
# total = transport + (price * number_of_fans)
#
# if total <= budget:
#     print(f"Yes! You have {budget - total:.2f} leva left.")
# else:
#     print(f"Not enough money! You need {total - budget:.2f} leva.")
##################################################################################################
"""02. Bike Race"""
# juniors = int(input())
# seniors = int(input())
# trail_type = input()
#
# juniors_price = 0
# seniors_price = 0
#
# if trail_type == "trail":
#     juniors_price = 5.50 * juniors
#     seniors_price = 7 * seniors
# elif trail_type == "cross-country":
#     juniors_price = 8 * juniors
#     seniors_price = 9.50 * seniors
#     if juniors + seniors >= 50:
#         juniors_price *= 0.75
#         seniors_price *= 0.75
# elif trail_type == "downhill":
#     juniors_price = 12.25 * juniors
#     seniors_price = 13.75 * seniors
# elif trail_type == "road":
#     juniors_price = 20 * juniors
#     seniors_price = 21.50 * seniors
#
# total = juniors_price + seniors_price
# total *= 0.95
#
# print(f"{total:.2f}")
##################################################################################################
"""03. Flowers"""
# chrysanthemums = int(input())
# roses = int(input())
# tulips = int(input())
# season = input()
# holiday = input()
#
# total = 0
#
# if season == "Spring" or season == "Summer":
#     total = (chrysanthemums * 2) + (roses * 4.10) + (tulips * 2.50)
# elif season == "Autumn" or season == "Winter":
#     total = (chrysanthemums * 3.75) + (roses * 4.50) + (tulips * 4.15)
#
# if holiday == "Y":
#     total *= 1.15
#
# if season == "Spring" and total > 7:
#     total *= 0.95
# elif season == "Winter" and roses >= 10:
#     total *= 0.90
#
# if (chrysanthemums + roses + tulips) > 20:
#     total *= 0.80
#
# total += 2
#
# print(f"{total:.2f}")
####################################################################################################
"""04. Car To Go"""
# budget = float(input())
# season = input()
#
# car_type = ""
# rent_class = ""
# car_price = 0
#
# if budget <= 100:
#     rent_class = "Economy class"
#     if season == "Summer":
#         car_type = "Cabrio"
#         car_price = budget * 0.35
#     elif season == "Winter":
#         car_type = "Jeep"
#         car_price = budget * 0.65
#
# elif 100 < budget <= 500:
#     rent_class = "Compact class"
#     if season == "Summer":
#         car_type = "Cabrio"
#         car_price = budget * 0.45
#     elif season == "Winter":
#         car_type = "Jeep"
#         car_price = budget * 0.80
#
# elif budget > 500:
#     rent_class = "Luxury class"
#     car_type = "Jeep"
#     car_price = budget * 0.90
#
# print(f"{rent_class}")
# print(f"{car_type} - {car_price:.2f}")
###################################################################################################
"""05. Vacation"""
# budget = float(input())
# season = input()
#
# place = ""
# country = ""
# price = 0
#
# if budget <= 1000:
#     place = "Camp"
#     if season == "Winter":
#         country = "Morocco"
#         price = budget * 0.45
#     elif season == "Summer":
#         country = "Alaska"
#         price = budget * 0.65
#
# elif 1000 < budget <= 3000:
#     place = "Hut"
#     if season == "Winter":
#         country = "Morocco"
#         price = budget * 0.60
#     elif season == "Summer":
#         country = "Alaska"
#         price = budget * 0.80
#
# elif budget > 3000:
#     place = "Hotel"
#     price = budget * 0.90
#     if season == "Winter":
#         country = "Morocco"
#     elif season == "Summer":
#         country = "Alaska"
#
# print(f"{country} - {place} - {price:.2f}")
################################################################################################
""""06. Truck Driver"""
# season = input()
# distance = float(input())
#
# price = 0
#
# if 10000 < distance <= 20000:
#     price = distance * 1.45
#
# elif season == "Spring" or season == "Autumn":
#     if distance <= 5000:
#         price = distance * 0.75
#     elif 5000 < distance <= 10000:
#         price = distance * 0.95
#
# elif season == "Summer":
#     if distance <= 5000:
#         price = distance * 0.90
#     elif 5000 < distance <= 10000:
#         price = distance * 1.10
#
# elif season == "Winter":
#     if distance <= 5000:
#         price = distance * 1.05
#     elif 5000 < distance <= 10000:
#         price = distance * 1.25
#
# total = (price * 4) * 0.90
#
# print(f"{total:.2f}")
################################################################################################
"""07. School Camp"""
# season = input()
# group_type = input()
# number_of_students = int(input())
# nights = int(input())
#
# price = 0
# sport = ""
#
# if season == "Winter":
#     if group_type == "boys" or group_type == "girls":
#         price = nights * 9.60
#         if group_type == "boys":
#             sport = "Judo"
#         elif group_type == "girls":
#             sport = "Gymnastics"
#     elif group_type == "mixed":
#         price = nights * 10
#         sport = "Ski"
#
# elif season == "Spring":
#     if group_type == "boys" or group_type == "girls":
#         price = nights * 7.20
#         if group_type == "boys":
#             sport = "Tennis"
#         elif group_type == "girls":
#             sport = "Athletics"
#     elif group_type == "mixed":
#         price = nights * 9.50
#         sport = "Cycling"
#
# elif season == "Summer":
#     if group_type == "boys" or group_type == "girls":
#         price = nights * 15
#         if group_type == "boys":
#             sport = "Football"
#         elif group_type == "girls":
#             sport = "Volleyball"
#     elif group_type == "mixed":
#         price = nights * 20
#         sport = "Swimming"
#
# total = price * number_of_students
#
# if number_of_students >= 50:
#     total *= 0.50
# elif 10 <= number_of_students < 20:
#     total *= 0.95
# elif 20 <= number_of_students < 50:
#     total *= 0.85
#
# print(f"{sport} {total:.2f} lv.")
#################################################################################################
"""08. Point on Rectangle Border"""
# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())
# x = float(input())
# y = float(input())
#
# if (x == x1 or x == x2) and (y1 <= y<= y2):
#     print("Border")
# elif (y == y1 or y == y2) and (x1 <=x <= x2):
#     print("Border")
# else:
#     print("Inside / Outside")
#################################################################################################
"""09. Numbers from 1 to 10"""
# for number in range(1, 11):
#     print(number)
#################################################################################################
"""10. Multiply by 2"""
while True:
    number = float(input())

    if number < 0:
        print(f"Negative number!")
        break
    else:
        number *= 2
        print(f"Result: {number:.2f}")
