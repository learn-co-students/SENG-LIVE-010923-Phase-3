# SQLAlchemy & Alembic

## Learning Goals

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
            - `.all`, `.order_by`, `desc`, `limit`, `funcfilter`, and loop compression to grab specific columns 
        - Querying data with `.query`
        - Updating data with `.update` and `.commit`
        - Deleting data with `.delete`
