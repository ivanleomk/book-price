from bs4 import BeautifulSoup
import requests
from userkey import getkey
import re

def kinoData(isbn,key):
    #STUB Testing
    base = "https://singapore.kinokuniya.com/bw/"
    headers = {'user-agent': key}
    url = base+isbn

    url = "https://singapore.kinokuniya.com/bw/9780199536009"

    page = requests.get(url, headers=headers)
    #Converting it to a soup for scrapping
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find("li",class_="price")

    return price;

print(kinoData("9780199536009","Mozilla/5.0 (Linux; Android 6.0.1; Nexus 4 Build/MOB30Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.106 Mobile Safari/537.36"))
