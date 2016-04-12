def main():
	website = input("Input website(cnn, nytimes, bbc, nzherald): ") #First requests for which website
	url = input("Input url: ") #Requests the url
	scraper(website, url)
def scraper(website, url): #Function, to be expanded, which will due the scraping
	if ".com" not in url: #Other tests should be included, but the most obvious is if there isn't a .com
		print("Invalid url")
		exit()
	print("%s, %s" % (website, url))
if __name__ == '__main__':   
     main()