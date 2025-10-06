import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='komalvarale@#$',
    database='traffic_db'
)
cursor = conn.cursor()
cursor.execute(
    "INSERT INTO traffic_live (id, junction, datetime, vehicles, processed) VALUES (%s, %s, %s, %s, %s)",
    (2025100516001, 3, '2025-10-05 16:00:00', 17, 0)
)
conn.commit()
cursor.close()
conn.close()

print("Live data inserted!")
