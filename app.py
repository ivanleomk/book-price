#Import
from bs4 import BeautifulSoup
import requests

#Abstracted Functions
from userkey import getkey
from amazon import amazonData
from bookdepo import bookData
from betterworld import betterData

#[Location,Price]
prices = []
#Generates a user agent to use for the web scrapping
key = getkey()
#Using Request to grab the site
#Out Of Stock
isbn = "9780199536009"
#Grabs Amazon Prices
amazondata = amazonData(isbn,key)
prices.append(["Amazon",amazondata[1]])
title = amazondata[0]
#Grabs book depo prices
bookdata = bookData(isbn,key)
prices.append(["Book Depository",bookdata[1]])

#Grabs BetterWorldBooks prices
betterdata = betterData(isbn,key)
prices.append(["BetterWorldBooks",betterdata[1]])

#Prints out the prices
for i in prices:
    print("%s is %s at %s"%(title,i[1],i[0]))
