# Stretch Goal: Include Association with Owner

# Pet Attributes: 
# name: TEXT 
# species: TEXT
# breed: TEXT 
# temperament: TEXT

# Stretch Goal
# owner_id: INTEGER

import sqlite3

CONN = sqlite3.connect('lib/resources.db')
CURSOR = CONN.cursor()

class Pet:
    
    pass

    # ✅ 1. Add "__init__" with "name", "species", "breed", "temperament", and "id" (Default: None) Attributes

    # ✅ 2. Add "create_table" Class Method to Create "pets" Table If Doesn't Already Exist

    # ✅ 3. Add "drop_table" Class Method to Drop "pets" Table If Exists

    # ✅ 4. Add "save" Instance Method to Persist New "pet" Instances to DB

    # ✅ 5. Add "create" Class Method to Initialize and Save New "pet" Instances to DB

    # ✅ 6. Add "new_from_db" Class Method to Retrieve Newest "pet" Instance w/ Attributes From DB

    # ✅ 7. Add "get_all" Class Method to Retrieve All "pet" Instances From DB

    # ✅ 8. Add "find_by_name" Class Method to Retrieve "pet" Instance by "name" Attribute From DB

        # If No "pet" Found, return "None"

    # ✅ 9. Add "find_by_id" Class Method to Retrieve "pet" Instance by "id" Attribute From DB

        # If No "pet" Found, return "None"

    # ✅ 10. Add "find_or_create_by" Class Method to:

        #  Find and Retrieve "pet" Instance w/ All Attributes

        # If No "pet" Found, Create New "pet" Instance w/ All Attributes

    # ✅ 11. Add "update" Class Method to Find "pet" Instance by "id" and Update All Attributes

