import sqlite3

# Connect to the database
conn = sqlite3.connect('')

# Create a cursor object
c = conn.cursor()

# Create a table
c.execute('''CREATE TABLE employees
             (id INT PRIMARY KEY NOT NULL,
              name TEXT NOT NULL,
              age INT NOT NULL)''')

# Save the changes
conn.commit()

# Close the connection
conn.close()