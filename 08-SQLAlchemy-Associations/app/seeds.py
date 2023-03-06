
from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Pet, Owner

if __name__ == '__main__':
    engine = create_engine('sqlite:///pet_app.db')
    Session = sessionmaker(bind=engine)
    session = Session()

# 2.a ✅ Add delete methods for Pet and Owner to clear the database before each seeding

    # Initialize faker

    # Create List of species with "Cat" and "Dog"

    # Create a List of cat breeds
   
    # Create a List of dog breeds
 
    # Create a List of temperaments 
    
    # Create an empty List of owners
 
    # Create a for loop that iterates 50 times
   
        # Create an owner using data from faker
       
        # Use .add and .commit to save the owner one at a time, so we maintain the owner ID in our instance.
       
        # Append each new owner to the owners array
       
    # Create an empty pets array
    
    # Create a for loop that iterates over the owners array
  
        # Create a for loop that iterates 1 - 3 times
      
            # Use faker and the species, cat breeds, dog breeds and temperament Lists to create a pet
            
            # Use .add and .commit to save the pet to the database
          
            # Append the pet to the pets array
            
# 3. ✅ Run the seed file and head over to debug.py to test out your One to Many association

#----------------------------------------------------- 

# 5. ✅ Add Delete methods for Job and Handler

    # Create a empty List set to handlers
    
    # Create a for loop that iterates 50 times
    
        # Create a handler with faker data 
       
        # Use .add and .commit to save the handler to the database
        
        # Append handler to handlers
    
    # Create a List of requests: "Walk", "Drop-in" and "Boarding"
    
    # Create an empty array and set it to jobs
    
    # Create a for loop that iterates over the handlers array
   
        # Create a for loop that iterates 1 - 10 times
        
            # Create a Job using faker, the requests List and pets List
            
            # Append each new job to the jobs List
               
        # Bulk save the jobs
    
    session.commit()
    session.close()

# 6. ✅ Run the seeds file and head over to debug.py to test out your Many to Many 