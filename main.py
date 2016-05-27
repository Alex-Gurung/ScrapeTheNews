def main(): #Main method, ideally this will program will be eventually used as a general scraping tool which calls the other files.
	website = input("Input website(cnn, nytimes, bbc, nzherald): ") #First requests for which website
	url = input("Input url: ") #Requests the url
	scraper(website, url) #Calls the scraper function, defined below
def scraper(website, url): #Function, to be expanded, which will due the scraping
	if ".com" not in url: #Other tests should be included, but the most obvious is if there isn't a .com
		print("Invalid url")
		exit() #Exits the program if the url isn't valid
	print("%s, %s" % (website, url))
if __name__ == '__main__':   
     main()