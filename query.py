import pandas as pd
from sqlalchemy import create_engine


engine = create_engine('postgresql+psycopg2://barathraj:raj2004@localhost:5432/imdbs')


df = pd.read_sql_table('imdb_list', con=engine)   


df_filtered = df[df['rating'] > 8]


df_filtered.to_csv('movies_rating_above_8.csv', index=False)
print("CSV file created: movies_rating_above_8.csv")


df_from_csv = pd.read_csv('movies_rating_above_8.csv')
df_from_csv.to_json('movies_rating_above_8.json', orient='records', indent=4)
print(" JSON file created: movies_rating_above_8.json")