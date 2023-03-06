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
    session.query(Pet).delete()
    session.query(Owner).delete()

    # Initialize faker
    fake = Faker()

    # Create List of species with "Cat" and "Dog"
    species = ["Cat", "Dog"]

    # Create a List of cat breeds
    cat_breeds = ["Domestic Long Hair", "Domestic Short Hair", "Siamese", "Ragdoll", "Sphynx", "Burmese"]

    # Create a List of dog breeds
    dog_breeds = ["Mix", "Husky", "Malamute", "Dachshound", "Samoyed", "Shiba Inu", "Corgi" ]

    # Create a List of temperaments 
    temperaments = ["Calm", "Nervous", "Mischievous", "Aggressive", "Hyper" ]

    # Create an empty List of owners
    owners = []
 
    # Create a for loop that iterates 50 times
    for _ in range(50):
            
            # Create an owner using data from faker
        owner = Owner(
            name=f"{fake.first_name()} {fake.last_name()}",
            email=fake.email(),
            phone=random.randint(1000000000, 9999999999),
            address=fake.address()
        )
        
        # Use .add and .commit to save the owner one at a time, so we maintain the owner ID in our instance.
        session.add(owner)
        session.commit()
        
        # Append each new owner to the owners array
        owners.append(owner)
       
    # Create an empty pets array
    pets = []

    # Create a for loop that iterates over the owners array
    for owner in owners:

        # Create a for loop that iterates 1 - 3 times
        for _ in range (random.randint(1,3)):

            # Use faker and the species, cat breeds, dog breeds and temperament Lists to create a pet
            rand_species = random.choice(species)

            pet = Pet(
                name=fake.name(),
                species=rand_species,
                breed=random.choice(cat_breeds) if rand_species == "Cat" else random.choice(dog_breeds),
                temperament=random.choice(temperaments),
                owner_id=owner.id
            )

            # Use .add and .commit to save the pet to the database
            session.add(pet)
            session.commit()
          
            # Append the pet to the pets array
            pets.append(pet)
            
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