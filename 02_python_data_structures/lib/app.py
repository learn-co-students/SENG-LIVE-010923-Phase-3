# Sequence Types
    
# Note: use print() to execute the examples. Comment out examples as needed to keep your Terminal
# output clean.

# Mutable
# Creating Lists
#1. ✅ Create a list of 10 pet names
pet_names = ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']

# Reading Information From Lists
#2. ✅ Return the first pet name

# print(pet_names[0])
# print(pet_names[-2])


#3. ✅ Return all pet names beginning from the 3rd index

# Inclusive
# print(pet_names[3:])

#4. ✅ Return all pet names before the 3rd index

# Exclusive
# print(pet_names[:3])


#5. ✅ Return all pet names beginning from the 3rd index and "up to" (exclusive) the 7th

# Inclusive
# print(pet_names[3:8])
    # Luke => 3
    # Tom => 7

# Exclusive
# print(pet_names[3:7])
    # Luke => 3
    # Spot => 6

#6. ✅ Find the index of a given element => .index()
# print(pet_names.index('Rose'))
# print(pet_names.index('Paul'))

# print(pet_names.index('Bud'))
    # ValueError

#7. ✅ Reverse the original list => .reverse()

# Mutative (Destructive)
    # Demonstrates the Mutability of Lists

# print(pet_names.reverse())
# print(pet_names)

#8. ✅ Return the frequency of a given element => .count()

# print(pet_names.count(''))
# print(pet_names.count('Bud'))

# Updating Lists
#9. ✅ Change the first name to all uppercase letters => .upper()

# pet_names[0] = pet_names[0].upper()

# print(pet_names)
# print(some_variable)

#10. ✅ Append a new name to the list => .append()

# Mutative (Destructive)

# pet_names.append('Bud')
# print(pet_names)

#11. ✅ Add a new name at a specific index => .insert()

# Argument 1 => Index
# Argument 2 => Value
# pet_names.insert(0, "Bud")
# pet_names.insert(1, "Sally")

# pet_names.insert(-1, "Sally")
# pet_names.append("Sally")

# print(pet_names)

#12. ✅ Add two lists together => +

# new_pet_list = pet_names + ["Bud", "Sally"]
# print(new_pet_list)

# number_list = [1,2,3] + [4,5,6]
# print(number_list)

#13. ✅ Remove the final element from the list => .pop()

# print(pet_names)

# Mutative (Destructive)
# pet_names.pop()
# print(pet_names)

#14. ✅ Remove element by specific index => .pop()

# print(pet_names)
# pet_names.pop(-1)
# print(pet_names)


#15. ✅ Remove a specific element => .remove()

# print(pet_names)
# pet_names.remove('Rose')
# pet_names.remove('Rose')
# print(pet_names)

#16. ✅ Remove all pet names from the list => .clear()

# print(pet_names)
# pet_names.clear()
# print(pet_names)

#Tuple
# Why Are Tuples Immutable?
    # What advantages does this provide for us? In what situations
    # would this serve us?

    # Helps us to preserve our data, keep it from being
    # changed or altered in any way.

# 📚 Review:
    # Mutable, Immutable <=> Changeable, Unchangeable

#17. ✅ Create a Tuple of 10 pet ages => () 
pet_ages = (1,2,3,4,5,6,7,8,9,10)

#18. ✅ Print the first pet age => []
# print(pet_ages[-1])


# Testing Mutability 
#19. ✅ Attempt to remove an element with ".pop" (should error)

# pet_ages.pop()
# AttributeError: 'tuple' object has no attribute 'pop'

#20. ✅ Attempt to change the first element (should error) => []
# pet_ages[0] = 2
# TypeError: 'tuple' object does not support item assignment


# Tuple Methods
#21. ✅ Return the frequency of a given element => .count()
# print(pet_ages.count(1))

#22. ✅ Return the index of a given element  => .index()
# print(pet_ages.index(1))

# BREAK PERIOD POINT

#23. ✅ Create a Range 
# Note:  Ranges are primarily used in loops

# print(range(60))

# Sets
#24. ✅ Create a set of 3 pet foods
pet_fav_food = {'house plants', 'fish', 'bacon'}

# Dictionaries 
# Creating 
#25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"

# Looks Like...JSON

pet_info_rose = {'name':'Rose', 'age':11, 'breed':'domestic long'}
pet_info_spot = {'name':'Spot', 'age':5, 'breed':'persian'}


#26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed" => dict(...)
pet_info_spot_1 = {'name': 'Spot', 'age': 25, 'breed':'boxer', 'temperament': 'relaxed'}
pet_info_spot_2 = dict(name='Spot', age=25, breed='boxer', temperament="relaxed")

    # Main advantage of using "dict" => Less Keystrokes (Less Quotes to Write Into Code)

# print(pet_info_spot_1)
# print(pet_info_spot_2)

# Reading
#27. ✅ Print the pet attribute of "name" using bracket notation 

# print(pet_info_rose['name'])
# print(pet_info_rose['temperament'])
    # KeyError: 'temperament'

#28. ✅ Print the pet attribute of "age" using ".get"

    # Note: ".get" is preferred over bracket notation in most cases 
    # because it will return "None" instead of an error

# print(pet_info_rose.get('temperament', 'Attribute Not Found!')) # Returns None

# Updating 
#29. ✅ Update Rose's age to 12 => []
# print(pet_info_rose)
# pet_info_rose['temperament'] = 'chill'
# print(pet_info_rose)


#30. ✅ Update Spot's age to 26 => .update({...})
# print(pet_info_spot)
# pet_info_spot.update({'temperament': 'chill'})
# print(pet_info_spot)


# Deleting
#31. ✅ Delete Rose's age using the "del" keyword => []

# print(pet_info_rose)
# del pet_info_rose['age']
# print(pet_info_rose)

#32. ✅ Delete Spot's age using ".pop"

# print(pet_info_rose)
# pet_info_rose.pop('age')
# print(pet_info_rose)

#33. ✅ Delete the last item for Rose using "popitem()"

# print(pet_info_rose)
# pet_info_rose.popitem()
# print(pet_info_rose)

# Loops 
pet_info = [
    {
        'name':'Spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Rose',
        'age':11,
        'breed': 'domestic long-haired',
    },
    {
        'name':'Meow Meow Beans',
        'age':2,
        'breed': 'domestic long-haired',
    }
]

pet_info_2 = [
    {
        'name':'Bud',
        'age':5,
        'breed': 'golden retriever',
    }, 
    {
        'name':'Princess Grace',
        'age':9,
        'breed': 'persian',
    },
    {
        'name':'WiFi',
        'age':4,
        'breed': 'wolf',
    }
]

#34. ✅ Loop through a range of 10 and print every number within the range
# for num in range(10):
#     print(num)

#35. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number
# for num in range(50, 60, 2):
#     print(num)

#36. ✅ Loop through the "pet_info" list and print every dictionary 
# for pet in pet_info:
#     print(pet)

#37. ✅ Create a function that takes a list a parameter 
    # The function should use a "for" loop to loop through the list and print each item 
    # Invoke the function and pass it "pet_names" as an argument
# def loop_through_list(list):
#     for pet in list:
#         print(pet)

# loop_through_list(pet_info)
# loop_through_list(pet_info_2)

#38. ✅ Create a function that takes a list as a parameter
    # The function should define a counter and set it to 0
    # Create a "while" loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # Return the counter 

# def demonstrate_while(list):
#     counter = 0
    
#     while(counter < len(list) - 1):
#         counter += 1
    
#     return counter

# print(demonstrate_while(pet_names))


#39. ✅ Create a function that updates the age of a given pet
        # DONE - The function should take a list of "dictionaries", "name" and "age" as parameters 
        # DONE - Create an index variable and set it to 0
        # DONE - Create a while loop 
            # DONE - The loop will continue so long as the list does not contain a name matching the "name" param 
            # and the index is less then the length of the list
            # DONE - Every list will increase the index by 1
        # If the dictionary containing a matching name is found, update the item's age with the new age 
            # Otherwise, return 'Pet not found'

# def update_pet_age(list, name, age):
    
#     index = 0
    
#     while(list[index]['name'] != name and index < len(list) - 1):
#         index += 1

#         if (list[index]['name'] == name):
#             list[index]['age'] = age

#             return list
        
#         else:
#             return 'Pet Not Found!'

# Pet Does Exist / Age is Updated
# print(update_pet_age(pet_info, 'Spot', 50))

# Pet Does Not Exist / "Pet Not Found"
# print(update_pet_age(pet_info, 'Bud', 50))

# List Comprehensions => []
# map like 
#40. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase
# print(pet_info)
# new_pet_list = [pet.get('name').upper() for pet in pet_info]
# print(new_pet_list)
# print(pet_info)

# find like
#41. ✅ Use list comprehension to find a pet named spot

# spot = [RETURNED PET / LOOP / CONDITIONAL]
# spot = [pet for pet in pet_info if pet.get("name") == 'Spot' ]
# print(spot)

# filter like
#42. ✅ Use list comprehension to find all of the pets under 3 years old

# young_pets = [RETURNED PET / LOOP / CONDITIONAL]
# young_pets = [pet for pet in pet_info if pet.get("age") < 2]
# print(len(young_pets))

# Generator Expression => ()
#43. ✅ Create a generator expression matching the filter above

    # Main Benefit => Less Memory Intensive

young_pets = (pet for pet in pet_info if pet.get("age") < 26)

# Accessing Generator Object Values

# 1. Using next()
print(next(young_pets))
print(next(young_pets))
print(next(young_pets))

# 2. Using a for loop
for pet in young_pets:
    print(pet)