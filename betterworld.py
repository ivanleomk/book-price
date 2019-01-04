from bs4 import BeautifulSoup
import requests
from userkey import getkey
import re

def betterData(isbn,key):
    #STUB Testing
    base = "https://www.betterworldbooks.com/product/detail/"
    headers = {'user-agent': key}
    url = base+isbn

    page = requests.get(url, headers=headers)
    #Converting it to a soup for scrapping
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find("h1").get_text()[1:]
    title = (' ').join(title.split("\n"))[:-3]
    price = soup.find("h3").get_text()[27:]
    x = len(price)
    if(x==38):
        price = price[:len(price)-34]
    elif(x==42):
        price = price[:len(price)-37]
    else:
        price = "Out Of Stock"
    print(title)

    return [title,price]
