import random
from bs4 import BeautifulSoup
import requests
import string
import re


#This selects a random user agent so as to bypass Amazon and other website's anti-spam
def getkey():
    #Chooses a random User Agent from the list provided
    url = "https://developers.whatismybrowser.com/useragents/explore/software_name/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    providers = soup.find_all('tr')

    #Converts the entire list into a list for easy workaround
    list = [x.get_text().strip().split("\n") for x in providers[1:]]

    #Selects a random list of keys from the provider selected
    keys= findprovider(list)
    while(len(keys)==0):
        keys = findprovider(list)

    #Selects a random entry from the list of keys on the page
    if len(keys)>1:
        selected = random.randint(0,len(keys)-1)
    else:
        selected = 0
    #Returns user key
    print("The selected index is " + str(selected))
    return(keys[selected].get_text())

def findprovider(x):
    #Chooses a random page from the list of user agents
    cprovid = x[random.randint(0,len(x)-1)]
    #counts the number of related agents
    relatedagents = cprovid[1]
    #Chooses the user agent
    provider = cprovid[0]
    #Calculates the number of pages
    pages = 1+ int(relatedagents)//50
    pagenum = random.randint(1,int(pages))
    print("We have chosen %s with %s page(s) and have chosen %s pagenumber"%(provider,pages,pagenum))
    #Splits by spaces
    provider = provider.split(' ')
    if len(provider)>1:
        comps = [re.sub('[\W_]+', '',x).lower() for x in provider]
        provider = "-".join(comps)
    else:
        provider = provider[0]
    url = "https://developers.whatismybrowser.com/useragents/explore/software_name/" +provider+"/" + str(pagenum)+"?order_by=times_seen"
    url2="https://developers.whatismybrowser.com/useragents/explore/software_name/Wget/4?order_by=times_seen"
    print(url)
    #Logs an entire list of user agent data values
    page = requests.get(url)
    #Converts the page content to a BeautifulSoup
    soup = BeautifulSoup(page.content, 'html.parser')
    keys = soup.find_all('td', class_='useragent')
    print("The Length of keys is " + str(len(keys)))

    #Returns the list of keys from the page
    return keys
