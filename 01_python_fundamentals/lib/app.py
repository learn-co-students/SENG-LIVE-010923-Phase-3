#!/usr/bin/env python3

# 📚 Review:
    # Python environment set up
	# Python debugging tools 
	# Python datatypes 

# 🚨 To enable ipdb debugging, first import "ipdb"
import ipdb

# Python => Snake Case 
# JavaScript => camelCase

# Python => Cannot Declare Variables Without Assignment
    # NameError: name 'pet_mood' is not defined
# JavaScript => Can Declare Variables Without Assignment

pet_mood = "Hungry!"
pet_name = "Rose"

# 1. ✅ Create a condition to check a pet's mood
    # If "pet_mood" is "Hungry!", "Rose needs to be fed."
    # If "pet_mood" is "Rowdy!", "Rose needs a walk."
    # In all other cases, "Rose is all good."

# JavaScript => "==="" (Compare Data Types)
# Python => Max of  "==" 

# We can use "set_trace" to override previously set values /
# test different outcomes.
# ipdb.set_trace()

# if pet_mood == "Hungry!":
#     print("Rose needs to be fed.")
# elif pet_mood == "Rowdy!":
#     print("Rose needs a walk.") 
# # elif:
#     # ...
# # elif:
#     # ...
# # elif:
#     # ...
# else:
#     print("Rose is all good.")

    # Note => Feel free to set your own values for "pet_mood" to view various outputs.

# 2. ✅ Create a ternary operator using "pet_mood" as a condition:
    # If pet_mood is "Hungry!" => "Rose needs to be fed."
    # In all other cases => "Rose is all good."

# JavaScript
    # Condition ? If True : If False

# Python
    # If True if Condition else Default Value

# print("Rose needs to be fed.") if pet_mood == "Hungry!" else print("Rose is all good.")

# 3. ✅ Create a function (say_hello) that returns the string "Hello, world!"
    # Test invocation of "say_hello" in ipdb using "say_hello()"
    # say_hello() => "Hello, world!"

# JavaScript => function 
# Python => def

# String Interpolation

    # JavaScript
        # `My name is ${name}`
    # Python
        # f"My name is {name}"

    # f => Format(?)

def say_hello(name = "Student"):
    print(f"Hello, {name}!")
    # print("Hello, world!")

# JavaScript
    # Can Invoke Functions Containing Params Without Args

# Python
    # Cannot Invoke Functions Containing Params Without Args
    # Unless We've Supplied a Default Argument

# Without Argument, Default Value "Student" Kicks In
# say_hello()

# With Argument, We See Expected Output
# say_hello("Louis")

# ipdb.set_trace()

# 4. ✅ Create a function (pet_greeting) that will return a string with interpolated pet's name
    # Test invocation of "pet_greeting" in ipdb using "pet_greeting()"
    # pet_greeting("Rose") => "Rose says hello!"
    # pet_greeting("Spot") => "Spot says hello!"

# Global Scope
# name = "Bud"

# Function (Local) Scope
# def pet_greeting():
#     global name
#     name = "Spot"
#     print(f"{name} says hello!")

# Invoke Functions With / Without Passed Args
# pet_greeting()
# pet_greeting("Rose")
# pet_greeting("Spot")

# pet_greeting()
# pet_greeting()


# 5. ✅ Move conditional logic from Deliverable 1 into a function (pet_status) so that we may 
# use it with different pets / moods
    # Test invocation of "pet_status" in ipdb using "pet_status(pet_name, pet_mood)"
    # pet_status("Rose", "Hungry!") => "Rose needs to be fed."
    # pet_greeting("Spot", "Rowdy!") => "Spot needs a walk."
    # pet_greeting("Bud", "Relaxed") => "Bud is all good."

# def pet_status(pet_name, pet_mood):
#     if pet_mood == "Hungry!":
#         print(f"{pet_name} needs to be fed.")
#     elif pet_mood == "Rowdy!":
#         print(f"{pet_name} needs a walk.") 
#     else:
#         print(f"{pet_name} is all good.")

    # Take a moment to note that "pet_name" and "pet_mood" parameters are within Local Scope and take priority over "pet_name" and "pet_mood"
    # in Global Scope.

# pet_status("Rose", "Hungry!")
# pet_status("Spot", "Rowdy!")
# pet_status("Bud", "Feisty!")

# 6. ✅ Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors. 
    # If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
    # pet_birthday(10) => "Happy Birthday! Your pet is now 11."
    # pet_birthday("oops") => "Type Error Occurred"

def pet_birthday(age = "0.1"):
    
    # ipdb.set_trace()
    
    # Attempt to Execute Code
    try:
        age = age + 1
        print(f"Happy Birthday! Your pet is now {age}")
    
    # If An Error of a Particular Type Occurs,
    # Execute Some Other Bit Of Code
    except TypeError:
        print("Type Error Occurred!")
    # except NameError:
    #     print("Name Error Occurred!")


    # Note => To view more common Python exceptions, visit https://docs.python.org/3/library/exceptions.html

# pet_birthday(10)
# pet_birthday("10")
# pet_birthday()

# 🚨 To create an ipdb breakpoint, comment / uncomment line below:
# ipdb.set_trace()


