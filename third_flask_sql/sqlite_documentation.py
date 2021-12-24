import sqlite3

connection = sqlite3.connect('data.db')  # Initialise Connection

cursor = connection.cursor()  # It allows to select and start things. It's responsible to execute queries

''' Schema => What the data is gonna look like .
'users' is the name of table. () <= in here we specify columns of our table '''
create_table = "CREATE TABLE users (id int, username text, password text)"

cursor.execute(create_table)  # Run the query

user = (1, 'Eazy', '1234')  # Creating User
insert_query = "INSERT INTO users VALUES (?, ?, ?)"  # SQL query
cursor.execute(insert_query, user)  # Run the query

users = [
    (2, 'Eazy', '1234'),
    (3, 'Bob', 'test'),
    (4, 'Anna', 'pass'),
]
cursor.executemany(insert_query, users)  # Executes for each user in the list

# ------------------------------------Receive Data from DataBase---------------------------------------------------- #

''' Goes to the users table, finds every row and then selects all of data in each row
* can be replaced by 'id' and it's gonna select only ids in the table'''
select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

# ------------------------------------------------------------------------------------------------------------------ #
connection.commit()  # Save changes

connection.close()  # To avoid receiving data anymore
