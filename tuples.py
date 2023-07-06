# TUPLES are immutable list
# tuples are simple data structures - use whenstoring set of values that should not be changed throughout the life of a program
# A tuple looks just like a list except you use () instead of brackets

dimensions = (200, 50)
print(dimensions[0]) # 200
print(dimensions[1]) # 50

# dimensions[0] = 50 doesnt work it results in a traceback

# to define a tuple with one element, you need to provide a trailing comma
my_t = (4,)

# -- looping through all values in a Tuple

for dimension in dimensions:
    print(dimension)

# -- Writing over a Tuple --
# we cant modify a tuple but you can assign a new value to a variable that represents a tuple
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)