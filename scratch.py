import psycopg2

# connect to bd

conn = psycopg2.connect(
    host="localhost",
    database="test",
    user="postgres",
    password="310715"
)

# create cursor
cur = conn.cursor()

# execute query
# cur.execute("INSERT INTO user_account VALUES (%s, %s)", (4, "Jon"))
cur.executemany("INSERT INTO user_account VALUES (%s, %s)",[(5, "Jeka"), (6, "Катя")])
cur.execute("SELECT * FROM user_account")
conn.commit()

rows = cur.fetchall()
print(rows)
for row in rows:
    print(row)

# close cursor and connection
cur.close()
conn.close()

