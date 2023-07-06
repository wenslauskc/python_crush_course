#A variable are boxes you can store values in. Or variables are labels that you can assign to values.
message = "hello world"
print(message)

message = "Hello Python Crash Course world"
print(message)

#Naming and Using Variables
#You can't start with numbers, use spaces, using Python reserved keywords
# Avoid name errors when using variables

#traceback is where the interpreter ran into trouble trying to execute the code

#DATA TYPES
#1 STRINGS
#String is a series of characters. Usually inside either double or single quotes

#Changing Case is a string with Methods
#A method is an action that Python can perfom on a piece of data. Every method has a set of parantheses
name = "ada lovelace"
print(name.title()) # Ada Lovelace

name = "Ada Lovelace"
print(name.upper()) # ADA LOVELACE
print(name.lower()) # ada lovelace. This method is useful for storing data

first_name = "wenslaus"
last_name = "kachasu"
full_name = f" {first_name} {last_name}" # f(format) strings - replaces the name of any variable in braces with its value
print(f"Hello, {full_name.title()}")

#Adding Whitespace(nonprinting character) to Strings with Tabs or Newlines
print("\tPython")
print("Languages:\nPython\nC\nJavascript")

favorite_language = " python "
print(favorite_language.rstrip()) # " python"
print(favorite_language.lstrip()) # "python "
print(favorite_language.strip()) # "python"

#Syntax error - Python doesnt recognize a section of your program as valid Python code

# 2 NUMBERS
#Integers 
add = 2 + 3 # 5
subtrack = 3 - 2 # 1
multiply = 2 * 3 # 6
division = 3 / 2 # 1.5
exponents = 3 ** 3 # 27
#Floats-any number with a decimal point
add = 0.1 + 0.1 # 0.2
add = 0.2 + 0.1 + 0.300000000000004 #arbitrary number of decimal places
divide = 4 / 2 # 2.0
multiply = 2 * 3.0 # 6.0

universe_age = 14_000_000_000
print(universe_age) #14000000000

#Multiple assignment
x, y, z = 0, 2, 6

#CONSTANTS - a variable whose values stays the same throughout the life of a program.
#Python dont have built-in constant types but programmers use all capital letters
MAX_CONNECIONS = 5000


