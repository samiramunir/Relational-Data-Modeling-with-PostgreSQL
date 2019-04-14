# Relational-Data-Modeling-with-Postgres
Modeled a relational database for a startup music streaming app to analyze songs streaming trends. Defined fact and dimension tables for a star schema, wrote an ETL pipeline that transfers data from json files in two local directories using PostgreSQL and Python.  

### Introduction

Sparkify is a startup music streaming app. The analytics team is interested in analyzing what kind of songs users are listening to and needs a data base designed to allow such analysis with easy queries.  The data they have resides in two directories: 

1. A directory of JSON logs on user activity on the app
2. A directory with JSON metadata on the songs in their app

**Project Goals**: Build a database with tables designed to optimize queries on song play analysis.


**Schema:** The database was designed in a star schema to allow query efficiency and to simplify actions for busines users. 

### The ETL pipeline: 

> config.py: Script that holds user and password for connecting to the database 

> sql_queries.py : Holds query scripts for creating tables, inserting into tables and dropping tables. 

> create_tables.py : Script to create fresh database and tables. 

> etl.py: Script to parse the log files and and extract data and populate the database with data. 

> test.ipynb: Run queries to test database integrity

### Requirements: 

PostgreSQL : Setup instructions- https://www.codementor.io/engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb

Psycopg2 - To connect to PostgreSQL - https://pynative.com/python-postgresql-tutorial/
