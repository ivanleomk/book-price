#Import
from bs4 import BeautifulSoup
import requests


#Scrapping a list of user-agent combinations


#STUB Testing
base = "https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords="
isbn = "9780872208438"
url = base+isbn

#Using Request to grab the site
headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 4 Build/MOB30Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.106 Mobile Safari/537.36',
    }
page = requests.get(url, headers=headers)

#Converting it to a soup for scrapping
soup = BeautifulSoup(page.content, 'html.parser')

#Grabbing the item listing
soup.find

#Grabbing the item that fits the ISBN number
