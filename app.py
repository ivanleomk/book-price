#Import
from bs4 import BeautifulSoup
import requests

#Abstracted Functions
from userkey import getkey
from amazon import amazonData

#Generates a user agent to use for the web scrapping
key = getkey()
#Using Request to grab the site
isbn = "9780199536009"
#Grabs Amazon Prices
amazondata = amazonData(isbn,key)
print(amazondata[0] +" retails at " + amazondata[1] + "on Amazon")

#Grabs book depo prices
