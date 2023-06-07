import psycopg2
import os

POSTGRES_API_KEY = os.getenv('POSTGRES_API_KEY')

conn = psycopg2.connect(host="localhost", database="test", user="postgres", password=POSTGRES_API_KEY)
try:
    with conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO user_account VALUES (%s, %s)", (9, "Настя"))

            cur.execute("SELECT * FROM user_account")
            rows = cur.fetchall()
            print(rows)
            for row in rows:
                print(row)

finally:
    conn.close()
