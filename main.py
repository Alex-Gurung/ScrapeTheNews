import bbc #Import all of the python files with their specific scraping solutions
import cnn
import nytimes
import nzherald
import wpost
from bs4 import BeautifulSoup, SoupStrainer #Imports the nessecary parts from BeautifulSoup
import urllib.request #PYTHON CHECK: if using python 2, import urllib2

def main(): #Main method, ideally this will program will be eventually used as a general scraping tool which calls the other files.
	website = input("Input website(cnn, nytimes, bbc, nzherald): ") #First requests for which website
	url = input("Input url: ") #Requests the url
	scraper(website, url) #Calls the scraper function, defined below

def scraper(website, url): #Function to complete the site specific scraping
	#print("%s, %s" % (website, url)) #Just prints the website and url
	inp = open(website+"urllist.txt", "w")
	inp.write(url)
	inp.close() #Unnessecary, but makes certain there isn't an issue
	if (website == "bbc"): #Current state: Pretty much works, aside form some minor formatting issues
		bbc.main()
	if (website == "cnn"): #Current state: Mostly works, but doesn't add the first paragraph
		cnn.main()
	if (website == "nytimes"): #Current state: urllib.error.HTTPError: HTTP Error 303: The HTTP server returned a redirect error that would lead to an infinite loop.
		nytimes.main()
	if (website == "nzherald"): #Current state: UnicodeEncodeError: 'charmap' codec can't encode character '\u2019' in position 859: character maps to <undefined>
		nzherald.main()
	if (website == "wpost"):
		wpost.main()
	
if __name__ == '__main__':   
     main()