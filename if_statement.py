cars = ["bmw", "benz", "audi", "brabus", "vw"]

for car in cars:
    if car == "benz":
        print(car.upper())
    else:
        print(car.title())

"""
Checking for Inequality
"""
requested_topping = "mushroom"

if requested_topping != "anchovies":
    print("Hold the anchovies")

answer = 22

if answer != 37:
    print("That is not the correct answer. Please try again!")

age_0 = 18
age_1 = 25

(age_0 >= 21) and (age_1 >= 21)
(age_0 >= 21) or (age_1 >= 21)

ingredients = ['carrots', 'maccaroni', 'chicken', 'salads']
'carrots' in ingredients
'pepperoni' in ingredients

if 'carrots' in ingredients:
    print("Adding carrots")
elif 'chicken' in ingredients:
    print("Adding chicken")
elif 'mushroom' in ingredients:
    print("Adding mushrooms")

print("\nFinished making your meal!")

banned_users = ['andrew', 'natasha', 'anntonia', 'lisa']
user = 'nicole'

if user not in banned_users:
    print(f"{user.title()}, you can post a comment if you wish.")

age = 15
voting_age = 18
if age >= voting_age:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print(f"Please register to vote in {voting_age - age} years time when you are eligible!")

person_age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}")

available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni",
                     'pineaple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don't have of {requested_topping} right now.")

print("\nFinished making your pizza")