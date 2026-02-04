from bs4 import BeautifulSoup

html = """
<table>
<tr><th>Name</th><th>Age</th><th>Disease</th><th>Doctor</th></tr>
<tr><td>John</td><td>30</td><td>Fever</td><td>Dr. Smith</td></tr>
</table>
"""

soup = BeautifulSoup(html, "lxml")

for row in soup.find_all("tr")[1:]:
    cols = row.find_all("td")
    print(cols[0].text, cols[1].text, cols[2].text, cols[3].text)
