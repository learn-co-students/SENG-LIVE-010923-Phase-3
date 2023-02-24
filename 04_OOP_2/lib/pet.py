#!/usr/bin/env python3
# Class Attributes and Methods 

import ipdb

class Pet:

# 4. ✅ Define a class attribute (total_pets) and set it to 0

    # Class Attribute
    total_pets = 0

    # What happens with our instances when we update a class attribute?

    def __init__(self, name, age, breed, temperament):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament

        # Without Class Method
        # Pet.total_pets += 1
        
        # With Class Method
        Pet.increase_pets()
        
        # Treating increase_pets As Instance Method
        # self.increase_pets()

# ipdb.set_trace()

# 5. ✅. Update the class attribute whenever an instance is initialized

# ipdb.set_trace()

# 6. ✅. Create a class method increase_pets that will increment total_pets
    
    # replace Pet.total_pets += 1 in __init__ with increase_pets()

    # Instance Method
    def print_pet_details(self):
        print(f'''
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
            temperament:{self.temperament}
        ''')

    # Class Method
    @classmethod # Step 1 => Keyword
    def increase_pets(cls): # Step 2 => cls Param
        cls.total_pets += 1

        # Perform Other Behaviors
        print("One New Pet Added!")

# ipdb.set_trace()