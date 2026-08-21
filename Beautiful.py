from bs4 import BeautifulSoup
import requests

url="https://books.toscrape.com/"

headers = {
    "User-Agent": "Chrome/120.0.0.0 Safari/537.36"
}

try:
    res=requests.get(url, headers=headers, timeout=5)
    res.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error fetching page:", e)
    exit()

soup=BeautifulSoup(res.text, "html.parser")


print(soup.find("title").text)

# Links

def link_finder(soup):
    links=soup.find_all("a")
    print("Links Found:", len(links))
    for link in links:
        print(link.get("href"))

link_finder(soup)


# forms
forms=soup.find_all("form")
print("Total forms:", len(forms))

# js files

js=soup.find_all("script")
print("JavaScript Files:")
for i in js:
    print(i.get("src"))

# Images
img=soup.find_all("img")
print("Images:", len(img))
for i in img:
    src=i.get("src")
    if src:
        print(src)


# Hidden Inputs:

print("Hidden Inputs:")

hidden_inputs=soup.find_all("input")
for i in hidden_inputs:
    if i.get("type")=="hidden":
        print(i.get("name"),"=",i.get("value"))
    else:
        print("No hidden inputs")


