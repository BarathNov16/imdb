import psycopg2
import json

print("Starting the script...")


try:
    conn = psycopg2.connect(dbname='imdb3re', user='barathraj',
                            password='raj2004', host='localhost', port=5432)
    cur = conn.cursor()
    print("Connected to database 'imdb3re' successfully.")
except Exception as e:
    print(" Failed to connect to the database:", e)
    exit(1)


try:
    query = "SELECT title, rating, genre, year FROM imdb_list3re WHERE rating >= 8"
    cur.execute(query)
    rows = cur.fetchall()
    print(f" Query executed successfully. Number of rows fetched: {len(rows)}")
except Exception as e:
    print(" Failed to run the query:", e)
    cur.close()
    conn.close()
    exit(1)


try:
    data = []
    for row in rows:
        data.append({
            'title': row[0],
            'rating': row[1],
            'genre': row[2],
            'year': row[3]
        })
    json_data = json.dumps(data, indent=4)
    print(" Data converted to JSON format successfully.")
except Exception as e:
    print("Failed to convert data to JSON:", e)
    cur.close()
    conn.close()
    exit(1)


try:
    with open('high_rating_movies.json', 'w') as jsonfile:
        jsonfile.write(json_data)
    print("JSON data written to 'high_rating_movies.json' successfully.")
except Exception as e:
    print("Failed to write JSON file:", e)


cur.close()
conn.close()
print(" Database connection closed. Script completed successfully!")
#ALTER
#SELECT json_agg(row_to_json(imdb_list2kl))
#FROM imdb_list2kl
#WHERE rating >= 8;