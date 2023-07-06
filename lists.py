#List - a collection of items in a particular order. You can mix data types within a list
# List work well for storing collections of items that can change throughout the life of a progran(MUTABLE)
# a square bracket[] indicates a list
cars = ['bmw', 'benz', 'ferrari', 'lamborghini']
print(cars) #['BMW', 'Benz', 'Ferrari', 'Lamborghini']

#Accessing elements in a list
print(cars[0].title()) #Bmw - zero-indexed
print(cars[-1].title()) #Lamborghini -last item in the list

message = f"My first car will be a {cars[1].title()}"
print(message)

# --- MODIFYING ---
cars[1] = "toyota"
print(cars) #['bmw', 'toyota', 'ferrari', 'lamborghini']

# --- ADDING ----
# 1.append() method - adds at the end of a list
cars.append('tesla')
print(cars) #['bmw', 'toyota', 'ferrari', 'lamborghini', 'tesla']

# 2.insert() method - specify the index of the new element and the value of the new item
cars.insert(0,"haval")
print(cars) #['haval', 'bmw', 'toyota', 'ferrari', 'lamborghini', 'tesla']

# --- REMOVING ---
# 1. del statement - use this when you know the psotion of the item you want to delete
del cars[2] # removes 'toyota' from the list
print(cars) #['haval', 'bmw', 'ferrari', 'lamborghini', 'tesla']

# 2.pop() mehtod -lets you remove the last item in a list but lets you work with that item after removing it
popped_car = cars.pop()
print(popped_car) #tesla
# we can use pop() with an index in it 
first_owned = cars.pop(3)
message = f"The firs car I will own is a {first_owned.title()}"
print(message)

# 3. remove() method - if you know the value of the item you want to remove
cars.remove('haval')
print(cars) #['bmw', 'ferrari']

# --- ORGANIZING ---
# 1. sort() method - sorts a list permanently
cars = ['bmw', 'audi', 'toyota', 'tesla']
cars.sort()
print(cars) #['audi', 'bmw', 'tesla', 'toyota']
cars.sort(reverse=True)
print(cars) #['toyota', 'tesla', 'bmw', 'audi']

# 2. sorted() function - sorts a list temporarily
print("\n Here is the sorted list:")
print(sorted(cars)) #['audi', 'bmw', 'tesla', 'toyota']

# 3. reverse() method - reverse the original order of a list. It applys permanently
cars = ['bmw', 'audi', 'toyota', 'tesla']
cars.reverse()
print(cars) #['tesla', 'toyota', 'audi', 'bmw']

# 4. len() function - find the length of a list
length = len(cars)
print(length) # 4

# --- LOOPING ---
teams = ["Chelsea", "Liverpool", "Manchester United", "Arsenal"]
for team in teams:
    message = f"{team.title()}, has qualified for Champions League"
    print(message)
    print(f"We can't wait to see next season, {team.title()}.\n")

print("Thank you to the participating teams!")

# -- Numerical List --

# range() function
for value in range(1, 6):
    print(value) # It prints numbers from 1 to 5 ie off-by-one behavior

numbers = list(range(1,7))
print(numbers) # [1, 2, 3, 4, 5, 6]

# third arguement is a step size when generating numbers
even_numbers = list(range(2, 11, 2))
print(numbers) #[2, 4, 6, 8, 10]

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# -- statistics --
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
minimum = min(digits) # 0
maximum = max(digits) # 9
total = sum(digits)

# -- list comprehension --
# list comprehension combine for loop and the creation of new elements into one line and automatically append each new element

squares = [value**2 for value in range(1, 11)]
print(squares)

cubes = []
for value in range(1, 11):
    cube = value ** 3
    cubes.append(cube)

print(cubes)

cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

# -- Slicing a List --
# specify the index of the index of the first and last elemens I want to work with
players = ['charles', 'martina', 'gift', 'florence', 'michael']
print(players[0:3]) # ['charles', 'martina', 'gift']
print(players[1:4]) # ['martina', 'gift', 'florence']
print(players[:4]) # ['charles', 'martina', 'gift', 'florence']
print(players[2:]) # ['gift', 'florence', 'michael']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# -- Copying a List --
my_food = ['pizza', 'cake', 'fresh chips', 'rice']
friend_foods = my_food[:] # take note that friends_food = my_food doesn't work
friend_foods.append('sadza')
print("\nMy friend's favorite foods are:")
print(friend_foods)

