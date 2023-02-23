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
        # from the same source (Pet Class)

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

    def get_name(self):
        return self._name        

    def set_name(self, name):

        if (isinstance(name, str)):
            
            # Assign incoming "name" as "_name" for Pet instance
            self._name = name

        else:
            print("Name must be a String")

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
    
    # Instance Method
    def print_pet_details(self):
        print(f'''
            name: {self.name}
            age: {self.age}
            breed: {self.breed}
            temperament: {self.temperament}
        ''')

# Instance / Object Properties => Attributes that are controlled by methods

class Owner:
    
    # Class Variable
        # We Would Expect This to Be Accessible / Settable For Each
        # New Instance
    approved_jobs = ["Programmer", "Cashier", "Pharmacist"]
    
    def __init__(self, age):
        self.age = age

    # Create an Owner class with two instance methods:

        # get_name => Retrieve Owner's name
    
    def get_name(self):
        print("Retrieving Owner's name...")
        return self._name

    def set_name(self, name):
        print("Setting Owner's name...")

        # Conditional Logic

            # Ensure that Owner's name is a String

            # If not, issue warning of "Name must be a string"

        if (isinstance(name, str)):
            
            # Assign incoming "name" as "_name" for Owner instance
            self._name = name

        else:
            print("Name must be a String")

    
    # Use property() to compile get_name / set_name and invoke them
    # whenever we access an Owner instance's name (owner.name)
    name = property(get_name, set_name)

# Labs
class Book:

    # If intention is to create each new Book instance with
    # a default "page_count" of 0...

        # book = Book("Some Title")
    
    def __init__(self, title, page_count=0):
        self.title = title
        self._page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    def get_page_count(self):
        return self._page_count

    # ...then we will need to ensure that each subsequent value 
    # of "page_count" will be set as an Integer.

    def set_page_count(self, value):
        
        if type(value) == int:
            self._page_count = value

        print("page_count must be an integer")

    page_count = property(get_page_count, set_page_count)

class Dog:

    # __init__ => Always Runs Upon Class Instantiation

        # In this case, we are assuming that each new Dog instance
        # will be instantiated without any attributes.

    def get_name(self):
        return self._name

    def set_name(self, name):
        
        if (type(name) == str) and (1 <= len(name) <= 25):
            self._name = name

        else:
            print("Name must be string between 1 and 25 characters.")

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        
        approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei",
            "Beagle", "French Bulldog", "Pug", "Pointer"]

        if breed in approved_breeds:
            self._breed = breed
        
        else:
            print("Breed must be in list of approved breeds.")

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)

# ipdb.set_trace()