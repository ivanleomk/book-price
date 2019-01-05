from bs4 import BeautifulSoup
import requests

def betterData(isbn,key):
    #STUB Testing
    base = "https://www.betterworldbooks.com/product/detail/"
    headers = {'user-agent': key}
    url = base+isbn

    page = requests.get(url, headers=headers)
    #Converting it to a soup for scrapping
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find("h3").get_text()[27:]
    print(price)
    x = len(price)
    if(x==38):
        price = price[:len(price)-34]
    elif(x==42):
        price = price[:len(price)-37]
    else:
        price = "Out Of Stock"
    print(price)
    return [price,url]
