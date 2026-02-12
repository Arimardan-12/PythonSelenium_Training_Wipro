import mysql.connector

host = "localhost"
user = "root"
password = "Arvii@4138"
database = "feb2026"

conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor = conn.cursor()
print("connected to the database successfully")

query = "SELECT * FROM feb2026.emplyee;"
cursor.execute(query)

result = cursor.fetchall()

for row in result:
    print(row)
