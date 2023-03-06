#1.✅ Update our Models to include a One to Many association

# Pet >- Owner

# Import Foreign Key
from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer, Float,  DateTime)

# Import relationship and backref from sqlalchemy.orm 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pet(Base):
    __tablename__ = 'pets'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    name = Column(String())
    species = Column(String())
    breed = Column(String())
    temperament = Column(String())
    
    #1.a ✅ Add  ForeignKey('owners.id') to owner)id
    owner_id = Column(Integer())
    
    def __repr__(self):
        return f"Id: {self.id}, " \
            + f"Name:{self.name}, " \
            + f"Species {self.species}, "\
            + f"Breed {self.breed}, "\
            + f"Species {self.temperament}"

#1.b ✅ Add an Owners table 

    #Create the following columns
    # id -> type integer
    # name -> type string
    # email -> type string
    # phone -> type int
    # address -> type string
    
    #1.c ✅ Associate the Pet model with the Owner model
        # relationship('Pet', backref=backref('pet'))
    
    # Add a __repr__ method that returns a string containing the id, name, email, phone and address of our class

#2. ✅ Update your migrations by running `alembic revision --autogenerate -m "add pets and owners tables"` 
# followed by `alembic upgrade head` 

# After running your migrations, go build out some seeds and test your one-to-many with debug.py
# -------------------------------

#4. ✅ Update our Models to have a Many to Many Association

# Pet-< Jobs >- Handlers

# Create a Handlers table 

    # Create the following columns
    # id -> type integer
    # name -> type string
    # email -> type string
    # phone -> type int
    # hourly_rate -> type float

   # Add a __repr__ method that returns a string containing the id, name, email, phone and hourly_rate of our class
 
# Create a "jobs" table to serve as our join

    # Create the following columns
    # id -> type integer
    # request -> type string
    # data -> type datetime
    # fee -> type float
    # pet_id -> type int with a ForeignKey('pet.id')
    # handler_id -> type int with a ForeignKey('handlers.id') 

    # Associate the models with relationship(<ModelNameHere>, backref=backref(<TableNameHere>))
   
    # Add a __repr__ method that returns a string containing the id, request, date, notes, fee, pet_id and handler_id of our class
   
# 5. ✅ Update your migrations by running `alembic revision --autogenerate -m "add handlers and jobs tables` 
# followed by `alembic upgrade head` 

# After running your migrations, go build out some seeds and test your many to many with debug.py