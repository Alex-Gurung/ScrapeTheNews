from bs4 import BeautifulSoup, SoupStrainer
import urllib.request
import re

def main():
    out = open('output.txt', 'w')
    inp = open('bccurllist.txt', 'r')
    for u in inp:
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        url = u
        soup = BeautifulSoup(opener.open(url), "html.parser")


        #1) Link to the website 
        #This is already defined as url
        #2) Date article published 
        #date = soup.find("div", {"class":"cnn_strytmstmp"}) #This variable should be overwritten in the following loop
        date = ""
        for i in soup.find_all('span'): #For every span element in source code
            if i.has_attr('class'): #if it has the class element
                if i['class'] == "floatLeft storyDate": #And if that element is called "floatLeft storyDate"
                    try:
                        date = s.contents[0].strip()
                    except:
                        print("error")

        #3) title of article 
        title = soup.find("title").contents[0].strip() 
        #4) Text of the article, currently has a bug where it doesn't pull the first paragraph
        paragraphs = ""
        for s in soup.find_all('p'):
            if not s.has_attr('class'):
                try:
                    paragraphs += s.contents[0].strip()
                except:
                    print("error")
        #Printing
        #print(date)
        print("Title: %s\n" % title) #prints it, comment out if don't want to see it in terminal/cmd
        out.write(title + "\n") #writes information to outfile
        #print("Content: %s" % paragraphs)
        out.write(paragraphs)
    
if __name__ == '__main__':   
     main()