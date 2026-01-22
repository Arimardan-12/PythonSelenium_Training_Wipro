import requests
#GET
url="http://127.0.0.1:5000/users"
response=requests.get(url)
print(response.status_code)
print(response.json())

#POST
import requests
url = "http://127.0.0.1:5000/users"
payload = {
    "name": "Sita"
}
headers = {
    "Content-Type": "application/json"
}
response = requests.post(url, json=payload, headers=headers)
print("Status Code:", response.status_code)
print("Response JSON:", response.json())


#put
url = "http://127.0.0.1:5000/users/1"   # update user with id = 1
payload = {
    "name": "Raja Updated"
}

headers = {
    "Content-Type": "application/json"
}
response = requests.put(url, json=payload, headers=headers)
print("Status Code:", response.status_code)
print("Response JSON:", response.json())


#Delete

url = "http://127.0.0.1:5000/users/2"  # delete user with id = 2

response = requests.delete(url)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())




