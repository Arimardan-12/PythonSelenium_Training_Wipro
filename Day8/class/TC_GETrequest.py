import requests
#GET 1
url="https://api.restful-api.dev/objects"
response=requests.get(url)
print(response.status_code)
print(response.json())


#GET 2
url="https://api.restful-api.dev/objects/7"
response=requests.get(url)
print(response.status_code)
print(response.json())


#post1
posturl = "https://api.restful-api.dev/objects"
body1 = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
}
r1 = requests.post(posturl, json=body1);
print("post status code", r1.status_code)
print(r1.json())

#put
object_id = "ff8081819782e69e019be414707c2eef"  # <-- use your real ID
put_url = f"https://api.restful-api.dev/objects/{object_id}"
updated_body = {
    "name": "Apple MacBook Pro 16 - Updated",
    "data": {
        "year": 2020,
        "price": 1999.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "2 TB",
        "color": "space gray"
    }
}
put_response = requests.put(put_url, json=updated_body)
print("PUT status:", put_response.status_code)
print(put_response.json())





