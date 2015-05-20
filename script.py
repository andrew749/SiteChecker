import smtplib
from urllib2 import urlopen
import time
from BeautifulSoup import BeautifulSoup
#checks if the hash of the current page has changed from last time
def checkWebsite(html1,html2):
	if(not html1 == html2):
		return True
	else:
		return False
oldhtml=urlopen("http://store.apple.com/ca/browse/home/specialdeals/mac/macbook_pro/13").read()
oldhtml=BeautifulSoup(oldhtml).find("div",{"id":"primary"})
def sendemail():
	server=smtplib.SMTP("smtp.gmail.com:587")
	server.starttls()
	server.login("andrewcod749@gmail.com","lcbzyxzlrlsboune")
	msg=str("There is a new mac mini available in the store")
	server.sendmail("andrewcod749@gmail.com","andrewcod749@gmail.com",msg);

while True:

	html=urlopen("http://store.apple.com/ca/browse/home/specialdeals/mac/mac_mini").read()
	html=BeautifulSoup(html).find("div",{"id":"primary"})
	if(checkWebsite(html, oldhtml)):
	    print("found change")
	    sendemail()
	    oldhtml=html
	time.sleep(30)
