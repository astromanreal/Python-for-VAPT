import requests
from bs4 import BeautifulSoup

url="https://www.geeksforgeeks.org"

try:
    response=requests.get(url, timeout=5)
    response.raise_for_status()

    soup=BeautifulSoup(response.text, "html.parser")

    links=soup.find_all("a")
    unique_links=set()

    for link in links:
        href=link.get("href")
        if href:
            unique_links.add(href)
    for href in unique_links:
        print(href)
   


    for link in links:
        if link.get("href"):
            print(link.get("href"))
            print()
        

    # print(links)


except requests.exceptions.RequestException as e:
    print("Error:", e)