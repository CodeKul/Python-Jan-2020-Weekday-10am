from bs4 import BeautifulSoup
import requests
import sys
import re

url = "http://www.codekul.com/"
response = None
try:
    response = requests.get(url)
except Exception as e:
    print(repr(e))
    sys.exit(1)

if response.status_code != 200:
    print("Non success status code returned "+str(response.status_code))
    sys.exit(1)

soup = BeautifulSoup(response.text, 'html.parser')

links = soup.find_all("a",attrs={'href': re.compile("^http://")})

linkList = []
for link in links:
    href = link.get('href')
    linkList.append(href)

print(linkList)
