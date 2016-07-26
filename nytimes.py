from bs4 import BeautifulSoup, SoupStrainer
import urllib.request #PYTHON CHECK: if using python 2, import urllib2

def main():
    out = open('nytimesoutput.txt', 'w') #Opens two files, one for reading in urls, and one for printing output data
    inp = open('nytimesurllist.txt', 'r')
    for url in inp: #For every line in the input file
        opener = urllib.request.build_opener() #PYTHON CHECK: if using python 2, say urllib2 instead of urllib.request
        opener.addheaders = [('User-agent', 'Mozilla/5.0')] #Mozilla thing may not be nessecary
        soup = BeautifulSoup(opener.open(url), "html.parser")


        #1) Link to the website 
        #This is already defined as url
        #2) Date article published 
        date = "" #Creating a empty string
        for i in soup.find_all('time'): #For every span element in source code
            if i.has_attr('class'): #if it has the class element
                if i['class'] == "dateline": #And if that element is called "floatLeft storyDate"
                    try:
                        date = s.contents[0].strip() #Gets just the text
                        break #Get out of the loop, because the first one should be correct. Check to make sure though
                    except:
                        print("error") #If something goes wrong

        #3) title of article 
        title = soup.find("title").contents[0].strip() 
        #4) Text of the article, currently has a bug where it doesn't pull the first paragraph
        paragraphs = ""
        for i in soup.find_all('p'): #For every span element in source code
            if i.has_attr('class'): #if it has the class element
                if i['class'] == "story-body-text story-content": #And if that element is called "floatLeft storyDate"
                    try:
                        date = s.contents[0].strip()
                    except:
                        print("error") #If something goes wrong
        #Printing
        #print(date)
        print("Title: %s\n" % title) #prints it, comment out if don't want to see it in terminal/cmd
        out.write(title + "\n") #writes information to outfile
        print("Content: %s" % paragraphs)
        out.write(paragraphs)
    
if __name__ == '__main__':   
     main()