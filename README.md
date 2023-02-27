# SENG-LIVE-010923 Phase 3 - Python

## Phase Level Objectives

- Understand the principles of Python as a language including principles of object oriented programming
- Understand the characteristics of a relational database
- Perform CRUD actions on a database using SQLAlchemy & Alembic
- Design an API to handle CRUD actions
- Communicate with an API using different HTTP verbs
- Create and present a project with a React frontend and a database-backed API backend


| Lecture | Notes | Videos | Starter | Solution |
| ------- | :---: | ------ | ------- | -------- |
| 1. (02/21/23) Python Fundamentals     |  [Notes](https://github.com/learn-co-students/SENG-LIVE-010923-Phase-3/compare/main...01_notes)     |  [Video](https://vimeo.com/801004522)      |    [Starter](https://github.com/learn-co-students/SENG-LIVE-010923-Phase-3/tree/main/01_python_fundamentals)     |   [Solution](https://github.com/learn-co-students/SENG-LIVE-010923-Phase-3/tree/01_notes/01_python_fundamentals)       |
| 2. (02/22/23) Python Data Structures     |  [Notes](https://github.com/learn-co-students/SENG-LIVE-010923-Phase-3/commits/02_notes/02_python_data_structures)     |   [Video](https://vimeo.com/801381989)     |    [Starter](https://github.com/learn-co-students/SENG-LIVE-010923-Phase-3/tree/main/02_python_data_structures)     |    [Solution](https://github.com/learn-co-students/SENG-LIVE-010923-Phase-3/tree/02_notes/02_python_data_structures)        |
| 3. (02/23/23) Object Oriented Programming in Python (Part 1)     |  [Notes](https://github.com/learn-co-students/SENG-LIVE-010923-Phase-3/commits/03_notes/03_oop)     |  [Video](https://vimeo.com/801748590)      |   [Starter](https://github.com/learn-co-students/SENG-LIVE-010923-Phase-3/tree/main/03_oop)      |    [Solution](https://github.com/learn-co-students/SENG-LIVE-010923-Phase-3/tree/03_notes/03_oop)      |
| 4. (02/24/23) Object Oriented Programming in Python (Part 2)     |   [Notes](https://github.com/learn-co-students/SENG-LIVE-010923-Phase-3/compare/main...04_notes)    |   [Video](https://vimeo.com/802120514)     |   [Starter](https://github.com/learn-co-students/SENG-LIVE-010923-Phase-3/tree/main/04_OOP_2)      |  [Solution](https://github.com/learn-co-students/SENG-LIVE-010923-Phase-3/tree/04_notes/04_OOP_2)        |
| 5. (02/27/23) SQL Fundamentals & Table Relations     |  [Notes](https://github.com/learn-co-students/SENG-LIVE-010923-Phase-3/commits/05_notes/05_SQL)     |   [Video](https://vimeo.com/802851841)     |   [Starter](https://github.com/learn-co-students/SENG-LIVE-010923-Phase-3/tree/main/05_SQL)      |   [Solution](https://github.com/learn-co-students/SENG-LIVE-010923-Phase-3/tree/05_notes/05_SQL)         |
| 6. (02/28/23) Object-Relational Mapping (ORM)     |   [Notes](#)    |   [Video](#)     |    [Starter](#)     |   [Solution](#)       |
| 7. (03/03/23) SQLAlchemy & Alembic     |   [Notes](#)    |    [Video](#)    |   [Starter](#)      |    [Solution](#)      |
| 8. (03/06/23) SQLAlchemy Associations     |   [Notes](#)    |    [Video](#)    |   [Starter](#)      |    [Solution](#)      |

## 1: Python Fundamentals
### Lecture Goals:
- Introduce Python and phase trajectory 
- Demonstrate Python package management with `pip`
- Demonstrate debugging in Python with `shell`, `print`, and `ipdb`
- Review Python data types (`str`, `int`, `float`, `bool`, `None`)
- Demonstrate Python conditionals and control flow
- Demonstrate Python functions
- Review Python variable scope and the `global` keyword
- Review Python error messages and exceptions 
- Demonstrate handling errors with `try:` and `except:` 

### Lecture Topics:
- Python and a Short History
- Package Management with `pip`
- Debugging
    - `print`
    - `ipdb`
    - Python Shell
    - Errors
    - Exceptions
        - `try:` `except:` 
- Python Conditionals and Control Flow
    - `if...else`
    - Comparison Operators
        - `>:` greater than
        - `>=:` greater than or equal to
        - `<:` less than
        - `<=:` less than or equal to
        - `==:` equal to
        - `!=:` not equal to
    - Logical operators
        - `and:` 
        - `or:` 
        - `not:` 
- Conditional Expressions
    - Ternary
- Python Functions
    - Function Definition 
    - Params
    - Default Params
    - Arguments
    - Invoking 
- Error Handling 
    - Reading Errors 
        - Syntax Errors, Logic Errors, and Exceptions
        - `AssertionError`
        - `IndexError` and `KeyError`
        - `NameError`
        - `TypeError`
        - `try:` `except:`

## 2: Python Data Structures
### Lecture Goals:
- Demonstrate Sequence types (`list`, `tuple`, `range`)
- Review the different uses for each Sequence type
- Demonstrate standard methods for accessing, updating and deleting values in Lists
- Review Tuples
- Review Ranges 
- Demonstrate Mapping types with Dictionaries
- Demonstrate standard methods for accessing, updating and deleting values in Dictionaries
- Demonstrate Set types with `set()` and `frozenset()`
- Demonstrate `for` and `while` loops
- Demonstrate list compressions 

### Lecture Topics:
- Sequence Types
    - List
    - Tuple
    - Range
    - Common Sequence Operators 
    - List Methods 
    - Tuples and Immutable vs Mutable 
- Mapping Types
    - Dict 
        - `switch`
- Set Types
    - Set
- Loops
    - `for`
    - `while`
    - List Compression
- Sequence Operators
- Sequence Functions and Methods

## 3: Object Oriented Programming in Python (Part 1)
### Lecture Goals:
- Define Object Oriented Programming
- Explain the benefits of Object Oriented Programming
- Explain the principles of Object-Oriented Design
- Demonstrate classes 
- Demonstrate instances 
- Demonstrate `__init__`
- Demonstrate instance method
- Demonstrate the `self` keyword 

### Lecture Topics:
- Object Oriented Programming 
- Benefits of Object Oriented Programming
- Principles of Object-Oriented Design
- Classes 
- Instances
- Initializing with Attributes Using `__init__`
- Instance Methods
- Self

## 4: Object Oriented Programming in Python (Part 2)
### Lecture Goals:
- Demonstrate Decorators 
    - `@decorator`  
- Demonstrate class attributes
    - Defining class attributes
    - Updating class attributes
- Demonstrate class methods
    - Defining class methods 
    - `@classmethod`
    - `cls` keyword 
- Object Inheritance

### Lecture Topics:
- Decorators
- Class Attributes
- Class Methods
- Object Inheritance

## 5: SQL Fundamentals & Table Relations
### Lecture Goals:
- Explain why we use databases
- Explain what SQL is and why we use it
- Explain the differences between a database, server, and API
- Explain the differences between rows and columns in a table
- Explain the differences between a Foreign Key and a Primary Key
- Explain what a join table is
- Explain what it means to seed a database
- Observe using SQL to communicate with a database
- Explain what an ORM is

### Lecture Topics:
- The Use Value of Databases in Applications
- Domain Modeling
- Join Table
- Mapping Columns and Rows to Classes and Instances
- Primary Keys
- Foreign Keys
- SQL
- ORM

## 6: Object-Relational Mapping (ORM)
### Lecture Goals:
- Demonstrate configuring an application to connect with sqlite3
- Demonstrate a create table method 
- Review preventative measures for SQL injection
- Demonstrate save and create methods  
    - Save => Persist created instance to DB
    - Create => Instantiate / persist created instance to DB, return new instance 
- Demonstrate query methods to find and retrieve resources 

### Lecture Topics:
- The benefits of ORM
- Connecting ORMs to DBs
- How to Use Data From a Database to Make Python Objects
- Mapping a Database Table to a Python Object
- Turning Database Rows into Python Objects


## 7: SQLAlchemy & Alembic
### Lecture Goals:
- Explain what SQLAlchemy is and how it benefits us as an ORM
    - Demonstrate creating a database with SQLAlchemy 
    - Demonstrate creating a schema
    - Demonstrate creating columns with SQLAlchemy
    - Demonstrate creating column constraints with SQLAlchemy 
    - Demonstrate creating indexes with SQLAlchemy 
    - Demonstrate creating default values 
- Explain Alembic and what it does for us
    - Demonstrate configuring an application to use Alembic 
    - Demonstrate creating migrations using Alembic
    - Demonstrate creating manual migrations using Alembic
    - Demonstrate CRUD in SQLAlcehmy
        - Adding data with .commit
            - `.all`, `.order_by`, `desc`, `limit`, function filter, and loop compression to grab specific columns 
        - Querying data with `.query`
        - Updating data with `.update` and `.commit`
        - Deleting data with `.delete`

### Lecture Topics:
- Creating a Database 
- Creating a Schema 
    - Columns 
    - Constraints
    - Index
    - Default Values
- Alembic
    - Migrations
        - Configuring the Migration Environment
        - Creating Migrations 
        - Manual Migrations 
- CRUD 
    - Sessions 
    - Transactions
    - `__repr__`
    - Creating Records
        - Seeding Data
    - Reading Records
        - Selecting Specific Columns
        - Ordering
        - Limits
        - Filtering 
        - Func
    - Updating Data
    - Deleting Data

## 8: SQLAlchemy Associations
### Lecture Goals:
- Review relationships, Primary keys, and Foreign keys
- Demonstrate creating a table with a Foreign key and referencing another table using `relationship()` and `backref()`
- Demonstrate using Alembic to generate tables with relationships 
- Demonstrate querying methods to view table relationships
- Demonstrate a “one to many” association
- Demonstrate a “many to many” association with a join model 

### Lecture Topics:
- Design Database Tables
- One-to-Many 
- Foreign Key Columns 
- `relationship()` and `backref()`
- One-to-One
- Alembic Migrations to Generate Table Relationships
- Relation Query Methods 
- Many-to-Many 
