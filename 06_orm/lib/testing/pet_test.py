from pet import Pet, CONN, CURSOR

# Pet : name: string species: string breed: string temperament:string, owner_id:int

class TestPet:
    '''Class Pet in pet.py'''

    def test_has_all_attributes(self):
        '''initializes with name, species, breed, temperament, and owner_id.'''
        pet = Pet(name="spot", species="dog", breed="chihuahua", temperament="feisty", owner_id=1)
        assert(pet.name == "spot" and pet.species == "dog" and pet.breed == "chihuahua" and pet.temperament == "feisty" and pet.owner_id == 1)

    def test_creates_table(self):
        '''contains method "create_table()" that creates table "pets" if it does not exist.'''
        CURSOR.execute("DROP TABLE IF EXISTS pets")
        Pet.create_table()
        assert(CURSOR.execute("SELECT * FROM pets"))

    def test_drops_table(self):
        '''contains method "drop_table()" that drops table "pets" if it exists.'''
        sql = """
            CREATE TABLE IF NOT EXISTS pets
                (id INTEGER PRIMARY KEY,
                name TEXT,
                species TEXT,
                breed TEXT,
                temperament TEXT,
                owner_id INTEGER)
        """
        CURSOR.execute(sql)
        Pet.drop_table()

        sql_table_names = """
            SELECT name FROM sqlite_master
            WHERE type='table'
            ORDER BY name
        """
        assert(len(CURSOR.execute(sql_table_names).fetchall()) == 0)

    def test_saves_pet(self):
        '''contains method "save()" that saves a Pet instance to the database.'''
        Pet.drop_table()
        Pet.create_table()
        spot = Pet("spot", "dog", "chihuahua", "feisty", 1)
        spot.save()

        sql = """
            SELECT * FROM pets
            WHERE name='spot'
            LIMIT 1
        """
        assert(CURSOR.execute(sql).fetchone() == (1, "spot", "dog", "chihuahua", "feisty", 1))

    def test_creates_pet(self):
        '''contains method "create()" that creates a new row in the database and returns a Pet instance.'''
        Pet.drop_table()
        Pet.create_table()
        spot = Pet.create("spot", "dog", "chihuahua", "feisty", 1)
        assert((spot.id, spot.name, spot.species, spot.breed, spot.temperament, spot.owner_id) == (1, "spot", "dog", "chihuahua", "feisty", 1))

    def test_creates_new_instance_from_db(self):
        '''contains method "new_from_db()" that takes a database row and creates a Pet instance.'''
        Pet.drop_table()
        Pet.create_table()
        sql = """
            INSERT INTO pets (name, species, breed, temperament, owner_id)
            VALUES ('spot', 'dog', 'chihuahua', 'feisty', 1)
        """
        CURSOR.execute(sql)
        sql = """
            SELECT * FROM pets
            WHERE name='spot'
            LIMIT 1
        """
        row = CURSOR.execute(sql).fetchone()
        spot = Pet.new_from_db(row)
        assert((spot.id, spot.name, spot.species, spot.breed, spot.temperament, spot.owner_id) == (1, "spot", "dog", "chihuahua", "feisty", 1))

    def test_gets_all(self):
        '''contains method "get_all()" that returns a list of Pet instances for every record in the database.'''
        Pet.drop_table()
        Pet.create_table()
        Pet.create("spot", "dog", "chihuahua", "feisty", 1)
        Pet.create("gracie", "cat", "laperm", "graceful", 2)

        pets = Pet.get_all()
        assert(
            (pets[0].id, pets[0].name, pets[0].species, pets[0].breed, pets[0].temperament, pets[0].owner_id) == \
                (1, "spot", "dog", "chihuahua", "feisty", 1) \
            and (pets[1].id, pets[1].name, pets[1].species, pets[1].breed, pets[1].temperament, pets[1].owner_id) == \
                (2, "gracie", "cat", "laperm", "graceful", 2)
        )

    def test_finds_by_name(self):
        '''contains method "find_by_name()" that returns a Pet instance corresponding to its database record retrieved by name.'''
        Pet.drop_table()
        Pet.create_table()
        Pet.create("spot", "dog", "chihuahua", "feisty", 1)

        spot = Pet.find_by_name("spot")
        assert(
            (spot.id, spot.name, spot.species, spot.breed, spot.temperament, spot.owner_id) == \
                (1, "spot", "dog", "chihuahua", "feisty", 1)
        )

    def test_finds_by_id(self):
        '''contains method "find_by_id()" that returns a Pet instance corresponding to its database record retrieved by id.'''
        Pet.drop_table()
        Pet.create_table()
        Pet.create("spot", "dog", "chihuahua", "feisty", 1)

        spot = Pet.find_by_id(1)
        assert(
            (spot.id, spot.name, spot.species, spot.breed, spot.temperament, spot.owner_id) == \
                (1, "spot", "dog", "chihuahua", "feisty", 1)
        )

    def test_finds_by_name_and_breed(self):
        '''contains method "find_or_create_by()" that takes all attributes as arguments and returns a Pet instance matching that record.'''
        Pet.drop_table()
        Pet.create_table()
        Pet.create("spot", "dog", "chihuahua", "feisty", 1)

        spot = Pet.find_or_create_by("spot", "dog", "chihuahua", "feisty", 1)
        assert(
            (spot.id, spot.name, spot.breed) == \
                (1, "spot", "chihuahua")
        )

    def test_finds_by_name_and_breed(self):
        '''contains method "find_or_create_by()" that takes all attributes as arguments and creates a Pet instance matching that record if it does not exist.'''
        Pet.drop_table()
        Pet.create_table()

        spot = Pet.find_or_create_by("spot", "dog", "chihuahua", "feisty", 1)
        assert(
            (spot.id, spot.name, spot.breed) == \
                (1, "spot", "chihuahua")
        )

    def test_saves_with_id(self):
        '''contains a method "save()" that saves a Pet instance to the database and returns a Pet instance with id.'''
        Pet.drop_table()
        Pet.create_table()
        spot = Pet("spot", "dog", "chihuahua", "feisty", 1)
        spot.save()
        assert(
            (spot.id, spot.name, spot.breed) == \
                (1, "spot", "chihuahua")
        )
    
    def test_updates_record(self):
        '''contains a method "update()" that updates an instance's corresponding database record to match its new attribute values.'''
        Pet.drop_table()
        Pet.create_table()
        spot = Pet.create("spot", "dog", "chihuahua", "feisty", 1)
        spot.name = "carlos"
        spot.update()

        assert(Pet.find_by_id(1).name == "carlos" \
            and Pet.find_by_name("joey") == None)