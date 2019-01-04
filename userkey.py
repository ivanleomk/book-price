import random
from bs4 import BeautifulSoup
import requests

def userkey():
    #Chooses a random page from the list of chrome browsers
    pagenum = random.randint(1,4425)
    url = "https://developers.whatismybrowser.com/useragents/explore/software_name/chrome/" + str(pagenum)+"?order_by=times_seen"
    #Logs an entire list of user agent data values
    page = requests.get(url)

    #Converts the page content to a BeautifulSoup
    soup = BeautifulSoup(page.content, 'html.parser')
    keys = soup.find_all('td', class_='useragent')

    selected = random.randint(1,)
    print(keys[0].get_text())

    #Returns user key

userkey()
