from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
print("Connected to MongoDB")

db = client["companyDB"]
collection = db["employees"]
employee_data = {
    "name": "Rahul Sharma",
    "department": "IT",
    "salary": 70000
}
existing_employee = collection.find_one({"name": "Rahul Sharma"})

if existing_employee:
    print("Employee Already Exists")
else:
    collection.insert_one(employee_data)
    print("Employee Inserted Successfully!")
print("\nAll Employees:")

for emp in collection.find():
    print(emp)

collection.update_one(
    {"name": "Rahul Sharma"},
    {"$set": {"salary": 75000}}
)

print("\nSalary Updated!")
client.close()
print("\nConnection Closed")
