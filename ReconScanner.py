import requests
from bs4 import BeautifulSoup

url="https://books.toscrape.com/"

try:
    response=requests.get(url, timeout=5)
    response.raise_for_status()
    soup=BeautifulSoup(response.text, "html.parser")
    print("-"*7," Recon Scanner", "-"*7)

    # title
    print(soup.find("title").text)

    # links
    def links_finder(soup):
        links=soup.find_all("a")
        print("Links Found:", len(links))
        if links:
            for link in links:
                print(link.get("href"))
    
    links_finder(soup)
    



except requests.exceptions.RequestException as e:
    print("Error", e)
    exit()