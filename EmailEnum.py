import re
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
try:
    response=requests.get(url, timeout=5)
    response.raise_for_status()
    emails=re.findall(r"\S+@\S+",response.text)
    print("-"*7,"EMAIL EXTRACTOR", "-"*7)
    print("Emails Found:", len(emails))
    print()
    for e in emails:
       print(e)

except requests.exceptions.RequestException as e:
    print("Error", e)
    exit()



