# !/usr/bin/env python3
    # Defines the location of the Python interpreter
    # See More => https://stackoverflow.com/a/7670338/8655247

import ipdb

# Classes

# 1. ✅ Create a Pet class

    # Note: Add 'pass' to the Pet class 

# 2. ✅ Instantiate a few Pet instances

    # Compare the Pet instances. Are each of them the same object?

# 3. ✅ Demonstrate __init__ 

    # Add arguments to instances  
    
    # Use dot notation to access each Pet instance's attributes 

    # Update attributes with new values

# Instance Methods

# 4. ✅ Create a "print_pet_details" function that will print each Pet instance's 
# attributes

    # Review the "self" keyword 
    
    # Invoke "print_pet_details" on an instance 
    
    # Example Terminal Ouput:
        # name: Rose
        # age: 11
        # breed: Domestic Longhair
        # temperament: Sweet

# Object Properties => Attributes that are controlled by methods

    # Create an Owner class with two instance methods:

        # get_name => Retrieve Owner's name
        
        # set_name => Set Owner's name

            # Ensure that Owner's name is a String

            # If not, issue warning of "Name must be a string"

    # Use property() to compile get_name / set_name and invoke them
    # whenever we access an Owner instance's name