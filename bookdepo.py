from bs4 import BeautifulSoup
import requests
from userkey import getkey

def bookData(isbn,key):
    #STUB Testing
    base = "https://www.bookdepository.com/a/"
    headers = {'user-agent': key}
    url = base+isbn

    page = requests.get(url, headers=headers)
    #Converting it to a soup for scrapping
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find("h1").get_text()
    price = soup.find("span",class_="sale-price").get_text()[1:]

    return [title,price]
