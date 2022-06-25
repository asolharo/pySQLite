# Overview

This is a program delevoped on Python3 to practice and demonstrate a connection to an SQL database.

I a menu with 6 options to manage the program. The options are:

1. Create user
   This is to add a new record into the database
2. View list of users
   This is to print all the record from the database
3. Update user
   With this function you can modify a record
4. Delete user
   Using this function you can delete an specific record
5. Search user
   Here you can look for a record base on one data
6. Exit
   To close the program

[Software Demo Video](https://youtu.be/EHp3HwF8KIg)

# Relational Database

SQLite. This library is based on C and creates a local database with the benefit of not needing another server process. Even you can program an internal data storage contained in the applications.

The database I'm using here is a basic one:
database:
"users" (
"id" INTEGER NOT NULL,
"name" TEXT NOT NULL,
"email" TEXT NOT NULL,
PRIMARY KEY("id" AUTOINCREMENT)
)

# Development Environment

• VSCode 2 = for editing
• Python3 = base language
• I imported "time" to add a delay during menu selections
• I imported "system" from "os" to clear the terminal during tasks.
• SQLite3 = SQL library for database and connection
• DB Browser for SQLite = application to monitor the content of the database

# Useful Websites

- [SQLite Python: Creating Tables](https://www.sqlitetutorial.net/sqlite-python/creating-tables/)
- [sqlite3 — DB-API 2.0 interface for SQLite databases](https://docs.python.org/3.8/library/sqlite3.html)

# Future Work

- Update individual keys
- More options to search
