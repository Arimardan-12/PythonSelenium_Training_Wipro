"""Parsing HTML (BeautifulSoup, lxml), Web automation basics
Write a Python program that:
1. Fetches an HTML webpage using the requests library
2. Parses the HTML using BeautifulSoup with the lxml parser
3. Extracts:
Page title, All hyperlinks, Specific table or list data
4. Converts the extracted data into JSON format
5. Saves the output into a file for further automation or analysis"""

import requests
from bs4 import BeautifulSoup
import json

url = "https://www.w3schools.com/html/html_tables.asp"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
pagetitle = soup.title.string if soup.title else "No title"
print(pagetitle)
for link in soup.find_all("a"):
    href = link.get("href")
    print(href)
tabledata = []
table = soup.find("table")
if table:
    rows = table.find_all("tr")
    for row in rows[1:]:
        columns = row.find_all("td")
        row_data = [col.text.strip() for col in columns]
        print(row_data)
        tabledata.append(row_data)
extracted_data = {
    "page_title": pagetitle,
    "total_links": len(href),
    "links": href,
    "table_data": tabledata
}
with open("extracteddata.json", 'w', encoding="utf-8") as file:
    json.dump(extracted_data, file, indent=4)

