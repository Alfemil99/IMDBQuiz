import psycopg2
import psycopg2.extras

conn = psycopg2.connect(
    dbname="myappdb",
    user="myuser",
    password="mypassword",
    host="localhost",
    port="5432"
)

db_cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
