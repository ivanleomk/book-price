#Import
from bs4 import BeautifulSoup
import requests
from userkey import getkey

#Generates a user agent to use for the web scrapping
key = getkey()
#Using Request to grab the site
headers = {'user-agent': key}

#STUB Testing
base = "https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords="
isbn = "9780872208438"
url = base+isbn

page = requests.get(url, headers=headers)
#Converting it to a soup for scrapping
soup = BeautifulSoup(page.content, 'html.parser')
while(len(soup)==3):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    print("Failed Attempt")
    print(len(soup))

#Grabbing the item listing
item = soup.find_all("div",class_="a-fixed-left-grid")
#Finds the Title
title = soup.find_all("h2",class_="s-access-title")[0].get_text()
price = soup.find_all("span",class_="sx-price-large")[0].get_text().split('\n')
price = price[1]+price[2]+"."+price[3]

print(title+ " is "+price.strip('\n') +" on Amazon")
