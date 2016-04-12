def main():
	website = input("Input website(cnn, nytimes, bbc, nzherald): ") #First requests for which website
	url = input("Input url: ")
	scraper(website, url)
def scraper(website, url):
	if ".com" not in url:
		print("Invalid url")
		exit()
	print("%s, %s" % (website, url))
if __name__ == '__main__':   
     main()