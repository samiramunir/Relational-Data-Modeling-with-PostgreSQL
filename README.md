# Relational-Data-Modeling-with-Postgres
Defined fact and dimension tables for a star schema for the purpose of user behavior for a start up music streaming app, and wrote an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL


### Introduction
> Sparkify is a startup music streaming app. The analytics team is interested in analyzing what kind of songs users are listening to and needs a data base designed to allow such analysis with easy queries.  The data they have resides in two directoreis: 

> 1. A directory of JSON logs on user activity on the app
> 2. A directory with JSON metadata on the songs in their app

Project Goals: Build a database with tables designed to optimize queries on song play analysis.

Project Description: 

In this project, you'll apply what you've learned on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, you will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.


why star schema: 
On the other hand, the star schema does simplify analysis. This is not just about query efficiency but also about simplifying future actions for business users. They may understand databases and know how to write queries, but why complicate things and include more joins if we can avoid it? A business user could have a template query that joins the fact table with all the dimension tables. Then they only need to add the appropriate selections and groupings. (This approach is close to Excel’s pivot tables.)