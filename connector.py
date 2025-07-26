
import pandas as pd
from sqlalchemy import create_engine
import psycopg2
conn = psycopg2.connect(
    dbname='postgres',
    user='barathraj',
    password='raj2004',
    host='localhost',
    port= 5432

)

conn.autocommit = True  
cur = conn.cursor()


cur.execute('CREATE DATABASE imdbs')

cur.close()
conn.close()

print("✅ Database created successfully!")

df = pd.read_csv('my_local_copy.csv')  


engine = create_engine(
    'postgresql+psycopg2://barathraj:raj2004@localhost:5432/imdbs')




df.to_sql('imdb_list', con=engine, if_exists='replace', index=False)



print("Data successfully written into the database!")
