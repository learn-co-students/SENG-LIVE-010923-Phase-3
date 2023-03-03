
# 3. ✅ CRUD Practice

# To run the file, run `python3 debug.py` in the app directory

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (Base, Pet)

# Store code that should only run when your file is executed as a script
# https://realpython.com/if-name-main-python/#in-short-it-allows-you-to-execute-code-when-the-file-runs-as-a-script-but-not-when-its-imported-as-a-module
if __name__ == '__main__':
    
    #3.1 ✅ Uncomment below to create the engine.
    engine = create_engine('sqlite:///pet_app.db')
    Base.metadata.create_all(engine)
    
    #3.2 ✅ Uncomment below to create sessions and bind to the engine.
    Session = sessionmaker(bind=engine)
    session = Session()

    # session => Object to Run CRUD Queries Through

    #3.3 ✅ Create
    
        # Create a pet and save it to the database with 'session.add' and 'session.commit'
    # rose = Pet(name="rose", species="cat", breed="domestic longhair", temperament="relaxed", owner_id=1)
    # spot = Pet(name="spot", species="dog", breed="boxer", temperament="feisty", owner_id=2)
    
    # session.add(rose)
    # session.bulk_save_objects([rose, spot])
    # session.commit()

        # Create multiple pets and bulk save them with  'session.bulk_save_objects' and 'session.commit'

            # Note: Bulk save will not contain the id

        # Verify results by checking the db 

    #3.4 ✅ Read
        
        # Retrieve all pets with session.query

    # pets = session.query(Pet)

    # # Print the pets 

    # print([pet for pet in pets])

    # # Get all of the pet names and print them with session.query

    # names = [name for name in session.query(Pet.name)]
    # print(names)

    # # Get all the pet names and print them in order with session.query and order_by

    # names_in_order

    # # Get the first pet with session.query and first

    # names_in_order = [name for name in session.query(Pet.name).order_by(Pet.name)]

    # Filter pet by temperament with session.query and filter 

    # filtered_by_temperament = session.query(Pet).filter(Pet.temperament.like('%feisty%'))
    # for record in filtered_by_temperament:
    #     print(record)

    #3.5 ✅ Update 
        
        # Update the first pet's name and print the updated pet info
    # first = session.query(Pet).first()
    # first.name = "Rex"
    # session.commit()

        # Update all the pets' temperaments to 'cool' and print the pets 
    # pets = session.query(Pet)
    # pets.update({Pet.temperament: 'cool'})
    # session.commit()

    #3.6 ✅ Delete
        
        # Delete one item by querying the first pet, deleting it and committing
    # first = session.query(Pet).first()
    # session.delete(first)
    # session.commit()

        # Delete all the pets with session.query and .delete
    # pets = session.query(Pet)
    # pets.delete()
    # session.commit()

    # optional Break point for debugging and testing
    import ipdb; ipdb.set_trace()