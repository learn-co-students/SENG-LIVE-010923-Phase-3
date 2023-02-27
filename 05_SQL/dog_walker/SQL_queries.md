-- -- Remove A Table 

-- DROP TABLE owners;

-- -- Create Two New Tables

--     -- owners => class Owner():
--     -- pets => class Pet():

--     -- Foreign Key => One to Many Relationship

--         -- Stored Inside pets Table

-- CREATE TABLE owners(
--     id INTEGER PRIMARY KEY,
--     name TEXT,
--     address TEXT,
--     email TEXT,
--     phone INTEGER
-- );

-- CREATE TABLE pets(
--     id INTEGER PRIMARY KEY,
--     owner_id INTEGER,
--     name TEXT,
--     birthdate DATETIME,
--     breed TEXT,
--     favorite_treats TEXT,
--     last_fed_at DATETIME,
--     last_walked_at DATETIME,
--         FOREIGN KEY (owner_id) REFERENCES owners(id)
-- );

-- -- Modify pets Table

--     -- Add New Column

-- ALTER TABLE pets
-- ADD COLUMN image_url TEXT;

--     -- Rename Column

-- ALTER TABLE pets
-- RENAME COLUMN birthdate TO age;

--     -- Changing Data Type

-- -- Create New Pet & Owner Instances

--     -- Seeding Our Data => Creating Sample Instances

-- -- Create Two Owners

-- INSERT INTO owners(name, address, email, phone)
-- VALUES ('Louis', '123 Street', 'myemail@gmail.com', '555-555-5555') 

-- INSERT INTO owners(name, address, email, phone)
-- VALUES ('Sally', '456 Street', 'myotheremail@gmail.com', '444-444-4444') 

-- -- Create Four Pets

--     -- owner_id => Foreign Key (Primary Key in owners Table)

-- INSERT INTO pets(name, age, breed, favorite_treats, image_url, owner_id) 
-- VALUES ('Luke', '2', 'domestic longhair', 'bacon', 'https://res.cloudinary.com/dnocv6uwb/image/upload/v1631229064/zx6CPsp_d_utkmww.webp', 2);

-- INSERT INTO pets(name, age, breed, favorite_treats, image_url, owner_id) 
-- VALUES ('rose', '11', 'domestic longhair', 'house plants', 'https://res.cloudinary.com/dnocv6uwb/image/upload/v1631229038/EEE90-E50-25-F0-4-DF0-98-B2-0-E0-B6-F9-BAA89_menwgg.jpg', 1);

-- INSERT INTO pets(name, age, breed, favorite_treats, image_url, owner_id) 
-- VALUES ('leia', '2', 'domestic Shorthair', 'bacon', 'https://res.cloudinary.com/dnocv6uwb/image/upload/v1631229011/8136c615d670e214f80de4e7fcdf8607--cattle-dogs-mans_vgyqqa.jpg', 2);

-- INSERT INTO pets(name, age, breed, favorite_treats, image_url, owner_id) 
-- VALUES ('Chop', '5', 'shiba inu', 'cheese', 'https://res.cloudinary.com/dnocv6uwb/image/upload/v1629822267/cdbd77592e3ef91e8cc1cf67d936f94f_fkozjt.jpg', 1);

-- CRUD Actions

    -- Read Data

-- Select All Pets

    -- SELECT * FROM pets;

-- Select Pets By "name"

    -- SELECT * FROM pets
    -- WHERE name = 'rose';

-- Select Pets By favorite_treats

    -- SELECT * FROM pets
    -- WHERE favorite_treats = 'bacon';

-- Select Pets By age

    -- SELECT * FROM pets
    -- WHERE age > 5;

-- Update Data

-- Update Pet's age By Name

    -- UPDATE pets
    -- SET age = 15
    -- WHERE name = 'rose';

-- Update Multiple Pet's favorite_treats

-- UPDATE pets
-- SET favorite_treats = "cheese"

-- Delete Pets

DELETE FROM pets 
WHERE age < 5

-- Adding Additional Conditions

-- WHERE name = 'luke';