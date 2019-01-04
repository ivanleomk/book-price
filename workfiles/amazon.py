from bs4 import BeautifulSoup
import requests
from userkey import getkey

def amazonData(isbn,key):
    #STUB Testing
    base = "https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords="
    headers = {'user-agent': key}

    url = base+isbn

    page = requests.get(url, headers=headers)
    #Converting it to a soup for scrapping
    soup = BeautifulSoup(page.content, 'html.parser')
    while(len(soup)!=60):
        key = getkey()
        headers = {'user-agent': key}
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        print("Failed Attempt")
        print(len(soup))
    print(len(soup)) #Love in a fallen city == 60 , 41 and 38  and 36 do not work
    #Grabbing the item listing
    item = soup.find_all("div",class_="a-fixed-left-grid")
    #Finds the Title
    title = soup.find_all("h2",class_="s-access-title")[0].get_text()
    price = soup.find_all("span",class_="sx-price-large")[0].get_text().split('\n')
    price = price[1]+price[2]+"."+price[3]

    data = [title,price]
    #returns Amazon Title and Price
    return data
