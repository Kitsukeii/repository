import sqlite3

#
# establishing a connection
#

# open a SQLite connection
# a database file called data.db will be created,
# if it does not exit
connection = sqlite3.connect('data.db')

# create a database cursor
cur = connection.cursor()

#
# creating the table
#

# create the database table if it doesn't exist
table_schema = """
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
);
"""
cur.execute(table_schema)

#
# inserting into the database
#

# x = int(input())
# y = input()

# the correct way
#cur.execute('SELECT * FROM abc WHERE x = ? AND y = ?', (x, y))

# NEVER DO THIS
#cur.execute(f'SELECT * FROM abc WHERE x = {x} AND y = "{y}"')

# NEVER DO THIS
#cur.execute('SELECT * FROM abc WHERE x = {} AND y = "{}"'.format(x, y))

# NEVER DO THIS
#cur.execute('SELECT * FROM abc WHERE x = %d AND y = "%s"' % (x, y))

name = input('Note name: ')
desc = input('Note description: ')

# insert some hard-coded data
insert_query = """
INSERT INTO notes (name, description)
VALUES (?, ?);
"""
cur.execute('SELECT * FROM notes WHERE name = ? AND description = ?', (name, desc))
cur.execute(insert_query, (name, desc))


# save it in the database file
connection.commit()

#
# querying the database
#

# query the database for ALL the data in the notes table
cur.execute('SELECT * FROM notes;')

# print the result
#result = cur.fetchall()
#print(result)
print('\nNotes:')
for row in cur.fetchall():
    display_name = row[1]
    display_desc = row[2]

    print(f'Note name: {display_name}\nNote description: {display_desc}\n')


#
# cleaning up
#

# close the cursor
cur.close()


# close the connection
connection.close()
