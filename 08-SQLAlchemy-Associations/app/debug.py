from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (Base, Owner, Pet)

if __name__ == '__main__':

    engine = create_engine('sqlite:///pet_app.db')
    Base.metadata.create_all(engine)
   
    Session = sessionmaker(bind=engine)
    session = Session()

    # 3. ✅ One to Many - Testing
    
    # Getting an Owner's Pets
    
        # Use session.query and .first() to grab the first Owner

        # Use session.query and filter_by to get the Owner's pets from Pet
    
        # Print out the Owner's pets
  
    # Getting a Pet's Owner
    
        # Use session.query and .first() to grab the first pet
        
        # Use session.query and .filter_by() to get the owner associated with this pet

    # 4. ✅ Head back to models.py to build out a Many to Many association
#--------------------------------------------

# 6. ✅ Many to Many 
    
    # Use session.query and .first() to get the first handler
   
    # Use session.query and .filter_by() to grab the handler_jobs
    
    # Print the handler_jobs
 
    # Use 'handler_jobs' to query pets for the associated pet to each job

    # Optional breakpoint for debugging
    # import ipdb; ipdb.set_trace()