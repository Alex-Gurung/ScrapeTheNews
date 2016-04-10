def main():
	number = 0
	number = int(input("Input number of urls: ")) #Has to be a proper number
	for i in range(number):
		inp = input("%s: url: " % i)
		scraper(inp)
def scraper(arg):
	print(arg)
if __name__ == '__main__':   
     main()