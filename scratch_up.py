import psycopg2

conn = psycopg2.connect(host="localhost", database="test", user="postgres", password="310715")
try:
    with conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO user_account VALUES (%s, %s)", (8, "Yamamma"))

            cur.execute("SELECT * FROM user_account")
            rows = cur.fetchall()
            print(rows)
            for row in rows:
                print(row)

finally:
    conn.close()
