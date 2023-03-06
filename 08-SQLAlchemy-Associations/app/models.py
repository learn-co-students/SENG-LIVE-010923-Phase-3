#1.✅ Update our Models to include a One to Many association

# Pet >- Owner

# Import Foreign Key
from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer, Float,  DateTime, ForeignKey)

# Import relationship and backref from sqlalchemy.orm 
from sqlalchemy.orm import relationship, backref
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
    owner_id = Column(Integer(), ForeignKey('owners.id'))
    
    def __repr__(self):
        return f"Id: {self.id}, " \
            + f"Name:{self.name}, " \
            + f"Species: {self.species}, "\
            + f"Breed: {self.breed}, "\
            + f"Temperament: {self.temperament}"

#1.b ✅ Add an Owners table 
class Owner(Base):
    __tablename__ = 'owners'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    #Create the following columns
    # id -> type integer
    # name -> type string
    # email -> type string
    # phone -> type int
    # address -> type string

    id = Column(Integer())
    name = Column(String())
    email = Column(String())
    phone = Column(Integer())
    address = Column(String())
    
    #1.c ✅ Associate the Pet model with the Owner model
        # relationship('Pet', backref=backref('pet'))
    pets = relationship('Pet', backref=backref('pet'))
    
    # Add a __repr__ method that returns a string containing the id, name, email, phone and address of our class
    def __repr__(self):
        return f"Id: {self.id}, " \
            + f"Name:{self.name}, " \
            + f"Email: {self.email}, "\
            + f"Phone: {self.phone}, "\
            + f"Address: {self.address}"

#2. ✅ Update your migrations by running `alembic revision --autogenerate -m "add pets and owners tables"` 
# followed by `alembic upgrade head` 

# After running your migrations, go build out some seeds and test your one-to-many with debug.py
# -------------------------------

#4. ✅ Update our Models to have a Many to Many Association

# Pet-< Jobs >- Handlers

class Handler(Base):
    __tablename__ = 'handlers'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    # Create the following columns
    # id -> type integer
    # name -> type string
    # email -> type string
    # phone -> type int
    # hourly_rate -> type float
    id = Column(Integer())
    name = Column(String())
    email = Column(String())
    phone = Column(Integer())
    hourly_rate = Column(Float())

   # Add a __repr__ method that returns a string containing the id, name, email, phone and hourly_rate of our class
    def __repr__(self):
        return f"Id: {self.id}, " \
            + f"Name:{self.name}, " \
            + f"Email: {self.email}, "\
            + f"Phone: {self.phone}, "\
            + f"Hourly Rate: {self.hourly_rate}"


# Create a "jobs" table to serve as our join
class Job(Base):
    __tablename__ = 'jobs'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    # Create the following columns
    # id -> type integer
    # request -> type string
    # data -> type datetime
    # fee -> type float
    # pet_id -> type int with a ForeignKey('pet.id')
    # handler_id -> type int with a ForeignKey('handlers.id') 
    id = Column(Integer())
    request = Column(String())
    date = Column(DateTime())
    notes = Column(String())
    fee = Column(Float())
    pet_id = Column(Integer(), ForeignKey('pets.id'))
    handler_id = Column(Integer(), ForeignKey('handlers.id'))

    # Associate the models with relationship(<ModelNameHere>, backref=backref(<TableNameHere>))
    pet = relationship('Pet', backref=backref('pets'))
    handler = relationship('Handler', backref=backref('handlers'))

    # Add a __repr__ method that returns a string containing the id, request, date, notes, fee, pet_id and handler_id of our class
    def __repr__(self):
        return f"Id: {self.id}, " \
            + f"Request:{self.request}, " \
            + f"Data: {self.date}, "\
            + f"Notes: {self.notes}, "\
            + f"Fee: {self.fee}, "\

# 5. ✅ Update your migrations by running `alembic revision --autogenerate -m "add handlers and jobs tables"` 
# followed by `alembic upgrade head` 

# After running your migrations, go build out some seeds and test your many to many with debug.py