import requests
from bs4 import BeautifulSoup

url="https://books.toscrape.com/"

try:
    response=requests.get(url, timeout=5)
    response.raise_for_status()

    soup=BeautifulSoup(response.text, "html.parser")

    forms=soup.find_all("form")
    
    for form in forms:
        print(form.get("action"))
        print(form.get("method", "get"))

        inputs=form.find_all("input")
        for i in inputs:
             print(i.get("name"))
             print(i.get("type"))


except requests.exceptions.RequestException as e:
    print("Error", e)
