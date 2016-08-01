import bbc
import cnn
import nytimes
import nzherald
import wpost
from bs4 import BeautifulSoup, SoupStrainer
import urllib.request #PYTHON CHECK: if using python 2, import urllib2

import os
import subprocess
def main(): #Main method, ideally this will program will be eventually used as a general scraping tool which calls the other files.
	website = input("Input website(cnn, nytimes, bbc, nzherald): ") #First requests for which website
	url = input("Input url: ") #Requests the url
	scraper(website, url) #Calls the scraper function, defined below
def scraper(website, url): #Function, to be expanded, which will due the scraping
	if ".com" not in url: #Other tests should be included, but the most obvious is if there isn't a .com
		print("Invalid url")
		exit() #Exits the program if the url isn't valid
	print("%s, %s" % (website, url)) #Currenyly just prints, but later shold be switched for calling the other programs
	inp = open(website+"urllist.txt", "w")
	inp.write(url)
	inp.close() #Unnessecary, but makes certain there isn't an issue
	if (website == "bbc"):
		bbc.main()
	if (website == "cnn"):
		cnn.main()
	if (website == "nytimes"):
		nytimes.main()
	if (website == "nzherald"):
		nzherald.main()
	if (website == "wpost"):
		wpost.main()
	
if __name__ == '__main__':   
     main()