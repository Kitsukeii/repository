import sqlite3
connection=sqlite3.connect("data.db")
cur = connection.cursor

# Create table variable
table_schema = """CREATE TABLE IF NOT EXISTS stats(
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR NOT NULL,
                skill VARCHAR NOT NULL
                stat INTEGER)"""

# Insert into table variable
insert_table = ('INSERT INTO stats (name, skill, stat) '
                        'VALUS (:name, :skill, :stat;')

# FUNCTIONS

def create_stats_table(connection):
    with connection:
        connection.execute(table_schema)

def add_stats(connection, name, skill, stat):
    with connection:
        connection.execute(insert_table, (name, skill, stat))

create_stats_table(connection)

# User prompt

user_prompt = """
--- Employee and Skills ---

#Please choose an option:
#1) Add new employee
#2) Exit

#Your selection:
"""

# Prompt function
def prompt():
    while (user_entry := input(user_prompt)) != "2":
        if user_entry == "1":
            name = input("What is the employee's name")
            skill = input("What is the employee's skill?")
            stat = input("What is their skill level out of 10?")

            add_stats(connection, name, skill, stat)
        else:
            print("Invalid input, please answer 1-2.")

prompt()

cur.close()
connection.close()
