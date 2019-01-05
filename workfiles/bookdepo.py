from bs4 import BeautifulSoup
import requests

def bookData(isbn,key):
    #STUB Testing
    base = "https://www.bookdepository.com/a/"
    headers = {'user-agent': key}
    url = base+isbn

    page = requests.get(url, headers=headers)

    #Converting it to a soup for scrapping
    soup = BeautifulSoup(page.content, 'html.parser')
    #Outputs HTML into textfile
    with open('url.txt', 'w', encoding='utf-8') as f_out:
        f_out.write(soup.prettify())

    price = soup.find("span",class_="sale-price")

    if (price==None):
        price = soup.find("p",class_="list-price")
        if(price==None):
            price = "Out Of Stock"

    if(price != "Out Of Stock"):
        price = price.get_text().strip()
        if("List price" in price):
            price = "Item is currently unavaliable"
        else:
            price = price[2:]

    return [price,url]

#bookData("9780872208438","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")
