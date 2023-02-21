
from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Pet, Owner, Job, Handler

if __name__ == '__main__':
    engine = create_engine('sqlite:///pet_app.db')
    Session = sessionmaker(bind=engine)
    session = Session()
#2.a ✅ Add delete methods for Pet and Owner to clear the database before each seeding
#----------
#5.✅ Add Delete methods for Job and Handler
  
    #Initialize faker

    #Create an array for species with "CAT" and "Dog"

    #Create an array of cat breeds
   
    #Create an array of dog breeds
 
    #Create an array of temperaments 
    
    #Create an empty array for owners
 
    #Create a for loop that iterates 50 times
   
        #Create an owner using data from faker
       

        #Use .add and .commit to save the owner one at a time, so we maintain the owner ID in our instance.
       
        #Append the owner to the owners array
       
    
    #Create an empty pets array
    
    #Create a for loop that iterates over the owners array
  
        #Create a for loop that iterates 1 - 3 times
      
            #Use faker and the species, cat breeds, dog breeds and temperament array to create a pet
            
            #Use .add and .commit to save the pet to the database
          
            #Append the pet to the pets array
            
#3✅ run the seed file and head over to debug.py to test out your one to many
#----------------------------------------------------- 

#5.✅ Create a empty array set to handlers
    
    #Create a for loop that iterates 50 times
    
        #Create a handler with faker data 
       
        #Use .add and .commit to save the handler to the database
        
        #Append handler to handlers
        
    
    #Create an array of requests, "Walk", "Drop-in" and "Boarding"
    
    #Create an empty array and set it to jobs
    
    #Create a for loop that iterates over the handlers array
   
        #Create a for loop that iterates 1 - 10 times
        
            #Create a Job using faker, the request array and pets array
            
            #append the job to the jobs array
               
        #Bulk save the jobs (we wont need their id)
    
    session.commit()
    session.close()

#6.✅ Run the seeds file and head over to debug.py to test out your Many to Many 