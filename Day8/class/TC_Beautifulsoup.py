"""import requests
from bs4 import BeautifulSoup



url = "https://www.w3schools.com/html/html_tables.asp"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

pagetitle=soup.title.string if soup.title else "No title"

print(pagetitle)

for link in soup.find_all("a"):
    href = link.get("href")
    print(href)"""


