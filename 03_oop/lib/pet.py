# !/usr/bin/env python3
    # Defines the location of the Python interpreter
    # See More => https://stackoverflow.com/a/7670338/8655247

import ipdb

# Classes

    # Blueprints => We Create Instances From Blueprint
    # Cookie Cutter => Instances (Cookies)

# 1. ✅ Create a Pet class
# class Pet:
    # pass

# ipdb.set_trace()

    # Note: Add 'pass' to the Pet class 

# 2. ✅ Instantiate a few Pet instances

    # Compare the Pet instances. Are each of them the same object?

        # No, they are different Objects in Memory but are all created
        # from the same source (Pet)

# 3. ✅ Demonstrate __init__ 

# self => Instance of Pet Class

# Attributes:
    # name
    # age
    # breed
    # temperament
class Pet:
    def __init__(self, name, age, breed, temperament, owner="No Owner"):
        
        # Attached Incoming Arguments to "self" (Instance)
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament
        self.owner = owner

# fido = Pet("Fido", 5, "Boxer", "Tranquil")
# spot = Pet("Spot", 7, "Terrier", "Feisty", "Louis")

# ipdb.set_trace()

    # DONE - Add arguments to instances  
    
    # DONE - Use dot notation to access / set each Pet instance's attributes 

    # DONE - Update attributes with new values

# Instance Methods

    # def say_hello(self):
    #     print("Hello!")

# ipdb.set_trace()

# 4. ✅ Create a "print_pet_details" function that will print each Pet instance's 
# attributes

    # DONE - Review the "self" keyword 
    
    # Invoke "print_pet_details" on an instance 
    
    # Example Terminal Ouput:
        # name: Rose
        # age: 11
        # breed: Domestic Longhair
        # temperament: Sweet
    
    def print_pet_details(self):
        print(f'''
            name: {self.name}
            age: {self.age}
            breed: {self.breed}
            temperament: {self.temperament}
        ''')

ipdb.set_trace()

# Object Properties => Attributes that are controlled by methods

    # Create an Owner class with two instance methods:

        # get_name => Retrieve Owner's name
        
        # set_name => Set Owner's name

            # Ensure that Owner's name is a String

            # If not, issue warning of "Name must be a string"

    # Use property() to compile get_name / set_name and invoke them
    # whenever we access an Owner instance's name