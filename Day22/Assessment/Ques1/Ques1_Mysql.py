import mysql.connector


conn = mysql.connector.connect(
    host="localhost",        # your host
    user="root",             # your username
    password="Arvii@4138",     # your password
    database="feb2026"
)

cursor = conn.cursor()

query = "SELECT * FROM employees WHERE salary > %s"
cursor.execute(query, (50000,))

print("Employees with salary > 50,000:")
for row in cursor.fetchall():
    print(row)


insert_query = """
INSERT INTO employees (name, department, salary)
VALUES (%s, %s, %s)
"""
new_employee = ("Rahul Sharma", "IT", 60000)

cursor.execute(insert_query, new_employee)
conn.commit()
print("New employee inserted successfully!")


employee_id = 1  # Example ID

update_query = """
UPDATE employees
SET salary = salary * 1.10
WHERE id = %s
"""

cursor.execute(update_query, (employee_id,))
conn.commit()
print("Salary updated by 10%!")


cursor.close()
conn.close()
