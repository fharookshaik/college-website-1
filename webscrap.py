from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

myurl = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphic%20cards"

# Opening the connection and grabbing the page
uClient = uReq(myurl)
page_html = uClient.read()

uClient.close()

page_soup = soup(page_html,'html.parser')
page_soup.findAll("div",{"class"})