import psycopg2
import psycopg2.extras

# Connect to the PostgreSQL database using the given credentials
conn = psycopg2.connect(
    dbname="myappdb",
    user="myuser",
    password="mypassword",
    host="localhost",
    port="5432"
)

# Create a cursor that returns rows as dictionaries instead of tuples
db_cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
