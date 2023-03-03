
# 3. ✅ CRUD Practice

# To run the file, run `python3 debug.py` in the app directory

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (Base, Pet)

if __name__ == '__main__':
    
    #3.1 ✅ Uncomment below to create the engine.
    # engine = create_engine('sqlite:///pet_app.db')
    # Base.metadata.create_all(engine)
    
    #3.2 ✅ Uncomment below to create sessions and bind to the engine.
    # Session = sessionmaker(bind=engine)
    # session = Session()

    #3.3 ✅ Create
    
        # Create a pet and save it to the database with 'session.add' and 'session.commit'

        # Create multiple pets and bulk save them with  'session.bulk_save_objects' and 'session.commit'

            # Note: Bulk save will not contain the id

        # Verify results by checking the db 

    #3.4 ✅ Read
        
        # Retrieve all pets with session.query

        # Print the pets 

        # Get all of the pet names and print them with session.query

        # Get all the pet names and print them in order with session.query and order_by

        # Get the first pet with session.query and first

        # Filter pet by temperament with session.query and filter 

    #3.5 ✅ Update 
        
        # Update the first pet's name and print the updated pet info

        # Update all the pets' temperaments to 'cool' and print the pets 

    #3.6 ✅ Delete
        
        # Delete one item by querying the first pet, deleting it and committing

        # Delete all the pets with session.query and .delete
  
    # optional Break point for debugging and testing
    import ipdb; ipdb.set_trace()