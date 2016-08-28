from bs4 import BeautifulSoup, SoupStrainer
import urllib.request #PYTHON CHECK: if using python 2, import urllib2

def main():
    out = open('nzheraldoutput.txt', 'wb') #Opens two files, one for reading in urls, and one for printing output data
    inp = open('nzheraldurllist.txt', 'r')
    for url in inp:
        opener = urllib.request.build_opener() #PYTHON CHECK: if using python 2, say urllib2 instead of urllib.request
        opener.addheaders = [('User-agent', 'Mozilla/5.0')] #Mozilla/5.0 may not be nessecary
        soup = BeautifulSoup(opener.open(url), "html.parser")


        #1) Link to the website 
        #This is already defined as url
        #2) Date article published 
        date = "" #Creating a empty string
        for i in soup.find_all('span'): #For every span element in source code
            if i.has_attr('class'): #if it has the class element
                if i['class'] == "floatLeft storyDate": #And if that element is called "floatLeft storyDate"
                    try:
                        date = s.contents[0].strip()
                    except:
                        print("error") #If something goes wrong

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
        temp = "Title: " + title + "\n"
        print(temp.encode("utf-8")) #prints it, comment out if don't want to see it in terminal/cmd
        temp = title + "\n"
        out.write(temp.encode("utf-8")) #writes information to outfile
        temp = "Content: " + paragraphs
        print(temp.encode("utf-8"))
        temp = paragraphs
        out.write(temp.encode("utf-8"))
    
if __name__ == '__main__':   
     main()