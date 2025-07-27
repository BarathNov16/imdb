import csv
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
password = os.environ.get('DB_PASSWORD')
conn = psycopg2.connect(dbname='postgres', user='barathraj',
                        password='password', host='localhost', port=5432)
conn.autocommit = True
cur = conn.cursor()


cur.execute('CREATE DATABASE imdb3re')
print(" Database 'imdb3re' created successfully.")

cur.close()
conn.close()


conn = psycopg2.connect(dbname='imdb3re', user='barathraj',
                        password='raj2004', host='localhost', port=5432)
cur = conn.cursor()


cur.execute("""
CREATE TABLE imdb_list3re (
    title TEXT,
    rating FLOAT,
    genre TEXT,
    year INT
)
""")
print("Table 'imdb_list3re' created successfully.")


with open('my_local_copy.csv') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  
    for row in reader:
        clean_row = row[2:]
        cur.execute(
            "INSERT INTO imdb_list3re (title, rating, genre, year) VALUES (%s, %s, %s, %s)",
            clean_row
        )

conn.commit()
print(" Data inserted into 'imdb_list3re' successfully.")


cur.close()
conn.close()
print("All done!")