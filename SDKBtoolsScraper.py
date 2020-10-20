import requests
from bs4 import BeautifulSoup
import re
import os
import urllib.request

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }



def scraplinks(urli):
	links = []
	url = urli
	req = requests.get(url, headers)
	soup = BeautifulSoup(req.content, 'html.parser')
	for link in soup.findAll('a'):
    		#print(link.get('href'))
		if ".zip" in str(link.get('href')) and "windows" in str(link.get('href')):
			#print(link.get('href'))
			links.append(str(link.get('href')))
	return links
def scrape_download_links(urli,downloadat,savefileas):
    print(urli)
    url = urli
    print('Beginning file download with urllib2...')
    url4dl = str(urli)
    urllib.request.urlretrieve(url4dl,downloadat+savefileas)
            #print(link.get('href'))
    #print(ii)

def create_directory(name):
	if not os.path.exists(name):
    		os.mkdir(name)

def replace_string(string, fromi, toi):
	return string.replace(fromi, toi)

scraped_links = scraplinks("https://androidsdkmanager.azurewebsites.net/Buildtools")
fnames = []
for x in scraped_links:
    #print(str(x))
    xin = replace_string(x,"https://dl.google.com/android/repository/","")
    savefileas = replace_string(x,"https://dl.google.com/android/repository/","")
    xin = replace_string(xin,".zip","")
    create_directory("SDKTools/"+xin)
    scrape_download_links(x,"SDKTools/"+xin+"/",savefileas)
print("done")
#create_directory("ali")