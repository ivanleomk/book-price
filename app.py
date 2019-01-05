#Import
from bs4 import BeautifulSoup
import requests

#Abstracted Functions
from workfiles.userkey import getkey
from workfiles.amazon import amazonData
from workfiles.bookdepo import bookData
from workfiles.betterworld import betterData

def getPrices(isbn):
    #[logo,price,link]
    prices = []
    #Generates a user agent to use for the web scrapping
    key = getkey()
    #Using Request to grab the site
    #Grabs Amazon Prices
    amazondata = amazonData(isbn,key)
    prices.append(["static/amazon.png",amazondata[1],amazondata[2]])
    title = amazondata[0]
    #Grabs book depo prices
    bookdata = bookData(isbn,key)
    prices.append(["static/bookdepo.png",bookdata[0],bookdata[1]])

    #Grabs BetterWorldBooks prices
    betterdata = betterData(isbn,key)
    prices.append(["static/bwb.png",betterdata[0],betterdata[1]])

    #Grabs Kinokuniya prices
    #kinodata = kinoData(isbn,key)
    print(prices)
    #Prints out the prices

    return [prices,title]
