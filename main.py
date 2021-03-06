import bbc #Import the other python files with their specific scraping solutions(the specific tags to search for)
import cnn
import nytimes
import nzherald
import wpost
from bs4 import BeautifulSoup, SoupStrainer #Imports what's necessary from BeautifulSoup(though might be unnecessary for main)
import urllib.request #PYTHON CHECK: if using python 2, import urllib2

def main(): #Main method, ideally this will program will be eventually used as a general scraping tool which calls the other files.
	website = input("Input website(cnn, nytimes, bbc, nzherald, wpost): ") #First requests for which website
	url = input("Input url: ") #Requests the url from the user
	scraper(website, url) #Calls the scraper function, defined below

def scraper(website, url): #Function to complete the site specific scraping
	#print("%s, %s" % (website, url)) #Just prints the website and url, which should be included in each specific scraper
	inp = open(website+"urllist.txt", "w") #Opens the url file to write
	inp.write(url)
	inp.close() #Should be unnessecary, but makes certain there isn't an issue with the file still being open
	if (website == "bbc"): #Current state: Pretty much works, aside form some minor formatting issues
		bbc.main()
	elif (website == "cnn"): #Current state: Mostly works, but doesn't add the first paragraph
		cnn.main()
	elif (website == "nytimes"): #Current state: urllib.error.HTTPError: HTTP Error 303: The HTTP server returned a redirect error that would lead to an infinite loop.
		nytimes.main()
	elif (website == "nzherald"): #Current state: Mostly works, some promotional stuff at the end(included in article, most likely will keep it there)
		nzherald.main()
	elif (website == "wpost"): #Current state: pretty much works
		wpost.main()
	else:
		print("Error, bad initial input") #If the name of the website doesn't match those available

	
if __name__ == '__main__': #To run main method(Don't really need this)
     main() 