# Pet Attributes: 
# name: TEXT 
# species: TEXT
# breed: TEXT 
# temperament: TEXT

# https://docs.python.org/3/library/sqlite3.html#tutorial
import sqlite3

# https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection
CONN = sqlite3.connect('lib/resources.db')

# https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor
CURSOR = CONN.cursor()

# import ipdb

# Pet => pets
class Pet:

    # ✅ 1. Add "__init__" with "name", "species", "breed", "temperament", and "id" (Default: None) Attributes

    def __init__(self, name, species, breed, temperament, id=None):

        # self.id = None
        # Attempt Later

        self.id = id
        self.name = name
        self.species = species
        self.breed = breed
        self.temperament = temperament

    # ✅ 2. Add "create_table" Class Method to Create "pets" Table If Doesn't Already Exist


        # Wrong => spot.create_table()
        # Right => Pet.create_table()

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS pets
                (id INTEGER PRIMARY KEY,
                name TEXT,
                species TEXT,
                breed TEXT,
                temperament TEXT)
        """

        # Execute SQL
        CURSOR.execute(sql)

    # ✅ 3. Add "drop_table" Class Method to Drop "pets" Table If Exists

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS pets
        """

        # Execute SQL
        CURSOR.execute(sql)

    # ✅ 4. Add "save" Instance Method to Persist New "pet" Instances to DB

    def save(self):
        sql = """
            INSERT INTO pets (name, species, breed, temperament)
            VALUES (?, ?, ?, ?)
        """

        # Execute SQL
        CURSOR.execute(sql, (self.name, self.species, self.breed, self.temperament))

    # ✅ 5. Add "create" Class Method to Initialize and Save New "pet" Instances to DB

        # Repeated Action That We're Abstracting Out Into "create"
    
    @classmethod
    def create(cls, name, species, breed, temperament):
        
        # __init__ Method Fires Off
        # Create Instance of Pet Class
        pet = cls(name, species, breed, temperament)
        
        # Persist Instance to DB
        pet.save()

        return pet

    # ✅ 6. Add "new_from_db" Class Method to Retrieve Newest "pet" Instance w/ Attributes From DB

    @classmethod
    def create_instance(cls, row):
        
        # Reinstantiating the Class
        pet = cls(
            name=row[1],
            species=row[2],
            breed=row[3],
            temperament=row[4],
            id=row[0]
        )

        return pet

    # ✅ 7. Add "get_all" Class Method to Retrieve All "pet" Instances From DB
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM pets
        """

        return [cls.create_instance(row) for row in CURSOR.execute(sql).fetchall()]
        
        # return CURSOR.execute(sql).fetchall() # => Gives us a List of Pet Tuple Objects

    # ✅ 8. Add "find_by_name" Class Method to Retrieve "pet" Instance by "name" Attribute From DB

        # If No "pet" Found, return "None"

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM pets
            WHERE name = ?
            LIMIT 1
        """

        row = CURSOR.execute(sql, (name, )).fetchone()
    
        # Return None is no "row" is found
        if not row:
            return None

        # Instantiate Pet class with Tuple values / Return Instance
        return Pet.create_instance(row)

    # ✅ 9. Add "find_by_id" Class Method to Retrieve "pet" Instance by "id" Attribute From DB

        # If No "pet" Found, return "None"

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM pets
            WHERE id = ?
            LIMIT 1
        """

        # If record is found, "row" will be assigned Tuple value
        row = CURSOR.execute(sql, (id, )).fetchone()

        # Return None is no "row" is found
        if row:
            return Pet.create_instance(row)

        # Instantiate Pet class with Tuple values / Return Instance
        return None

    # ✅ 10. Add "find_or_create_by" Class Method to:

        #  Find and Retrieve "pet" Instance w/ All Attributes

        # If No "pet" Found, Create New "pet" Instance w/ All Attributes

    # Pet.find_or_create_by("spot", "dog", "boxer", "chill")

        # If we find a record, return that record expressed as a Python object

        # If we don't, instantiate / persist the new Pet

    @classmethod
    def find_or_create_by(cls, name=None, species=None, breed=None, temperament=None):
        
        # SQL Query to Find Pet If It Exists
        sql = """
            SELECT * FROM pets
            WHERE (name, species, breed, temperament) = (?, ?, ?, ?)
            LIMIT 1
        """

        row = CURSOR.execute(sql, (name, species, breed, temperament)).fetchone()

        # If We Don't Find Matching Record...
        if not row: 
            
            # SQL Query for Inserting New Record into pets Table
            sql = """
                INSERT INTO pets (name, species, breed, temperament)
                VALUES (?, ?, ?, ?)
            """

            # Execution of SQL
            CURSOR.execute(sql, (name, species, breed, temperament))

            return Pet.find_by_name(name)

        return Pet.create_instance(row)

    # ✅ 11. Add "update" Method to Find "pet" Instance by "id" and Update All Attributes

    # spot.name = "new name"
    # spot.breed = "new breed"
    # spot.update()

    def update(self):
        sql = """
            UPDATE pets
            SET name = ?,
                breed = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.name, self.breed, self.id))