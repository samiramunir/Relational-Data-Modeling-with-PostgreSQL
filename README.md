# Relational-Data-Modeling-with-Postgres
Defined fact and dimension tables for a star schema for the purpose of user behavior for a start up music streaming app, and wrote an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL


### Introduction

Sparkify is a startup music streaming app. The analytics team is interested in analyzing what kind of songs users are listening to and needs a data base designed to allow such analysis with easy queries.  The data they have resides in two directoreis: 

1. A directory of JSON logs on user activity on the app
2. A directory with JSON metadata on the songs in their app

Project Goals: Build a database with tables designed to optimize queries on song play analysis.

Project Description: 

The database was designed in a star schema to allow query efficiency and to simplify actions for busines users. 

The ETL pipeline: 

> sql_queries.py : Holds query scripts for creating tables, inserting into tables and dropping tables. 

> create_tables.py : Script to create fresh database and tables. 

> etl.py: Script to parse the log files and and extract data and populate the database with data. 

> config.py: script that holds user and password for connecting to the database

> test.ipynb: Run queries to test database integrity