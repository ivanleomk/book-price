#Import
from bs4 import BeautifulSoup
import requests

#Abstracted Functions
from userkey import getkey
from amazon import amazonData
from bookdepo import bookData

prices = []
#Generates a user agent to use for the web scrapping
key = getkey()
#Using Request to grab the site
isbn = "9780199536009"
#Grabs Amazon Prices
amazondata = amazonData(isbn,key)
prices.append(["Amazon",amazondata[0],amazondata[1]])
#Grabs book depo prices
bookdata = bookData(isbn,key)
prices.append(["Book Depository",bookdata[0],bookdata[1]])
#Grabs BetterWorldBooks prices

#Prints out the prices
for i in prices:
    print("%s retails at %s on %s"%(i[1],i[2],i[0]))
