from bs4 import BeautifulSoup, SoupStrainer #Import beautiful soup, remember you need to have installed this
import urllib.request #PYTHON CHECK: if using python 2, import urllib2

def main():
    out = open('cnnoutput.txt', 'w') #Opens two files, one for reading in urls, and one for printing output data
    inp = open('cnnurllist.txt', 'r')
    for url in inp:
        opener = urllib.request.build_opener() #PYTHON CHECK: if using python 2, say urllib2 instead of urllib.request
        opener.addheaders = [('User-agent', 'Mozilla/5.0')] #Mozilla thing may not be nessecary
        
        soup = BeautifulSoup(opener.open(url), "html.parser") #Sets a variable soup that opens the url with an html parser


        #1) Link to the website 
        #This is already defined as url
        #2) Date article published 
        date = soup.find("div", {"class":"cnn_strytmstmp"}) #This variable should be overwritten in the following loop
        for i in soup.find_all('meta'): #For every meta element in source code
            if i.has_attr('itemprop'): #if it has the itemprop element
                if i['itemprop'] == 'datePublished': #And if that element is called datePublished
                    if i.has_attr('content'): #If it has a content attribute(it should)
                        date = i['content'] #Set date equal to that
                        break

        #3) title of article 
        title = soup.find("div", {"id":"cnnContentContainer"}) #Same as above
        for i in soup.find_all('meta'):
            if i.has_attr('itemprop'): #Using has_attr prevents errors down the line
                if i['itemprop'] == 'headline':
                    if i.has_attr('content'):
                        title = i['content']
        #4) Text of the article
        paragraphs = ""
        for s in soup.find_all(class_="zn-body__paragraph"):
            try:
                paragraphs += s.contents[0].strip() #Fixes formatting errors
            except:
                print("error") #If can't strip
        #Printing
        #print(date)
        print("Title: %s\n" % title) #prints it, comment out if don't want to see it in terminal/cmd
        out.write(title + "\n") #writes information to outfile
        print("Content: %s" % paragraphs)
        out.write(paragraphs) #Writes paragraphs to outfile
    
if __name__ == '__main__':   
     main()