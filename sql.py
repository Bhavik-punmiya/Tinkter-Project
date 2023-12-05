import mysql.connector
# Creating connection object
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bhavik0310"
)

# Creating a cursor object
my_cursor = mydb.cursor()

# Executing SQL query to fetch database names
my_cursor.execute("SHOW DATABASES")

# Fetching all databases
databases = my_cursor.fetchall()

# Printing the number of databases and their names
print(f"Total databases: {my_cursor.rowcount}")

my_cursor.execute("USE djsanghvi")
my_cursor.execute("select * from Class")