import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/ASEAN"
table_class = "sortable wikitable plainrowheaders"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table with the class wikitable and all its rows
wiki_table = soup.find("table", {"class": table_class})
rows = wiki_table.find_all("tr")

# Creating an empty dictionary for the info
countries_dict = {}

