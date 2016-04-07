from bs4 import BeautifulSoup, SoupStrainer
import urllib.request
import re

def main():
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    url = 'http://www.cnn.com/2013/10/29/us/florida-shooting-cell-phone-blocks-bullet/index.html?hpt=ju_c2'
    soup = BeautifulSoup(opener.open(url), "html.parser")
    #webpage= urllib.request.urlopen("http://www.cnn.com/2013/10/29/us/florida-shooting-cell-phone-blocks-bullet/index.html?hpt=ju_c2").read()

    #soup=BeautifulSoup(webpage)

    #1) Link to the website 

    #2) Date article published 
    #date = soup.find("div", {"class":"cnn_strytmstmp"}).text.encode('utf-8')
    date = soup.find("div", {"class":"cnn_strytmstmp"})
    for i in soup.find_all('meta'):
        if i.has_attr('itemprop'):
            if i['itemprop'] == 'datePublished':
                if i.has_attr('content'):
                    date = i['content']

    #3) title of article 
    #title = soup.find("div", {"id":"cnnContentContainer"}).find('h1').text.encode('utf-8')
    title = soup.find("div", {"id":"cnnContentContainer"})
    for i in soup.find_all('meta'):
        if i.has_attr('itemprop'):
            if i['itemprop'] == 'headline':
                if i.has_attr('content'):
                    title = i['content']
    #4) Text of the article
    #paragraphs = soup.find('div', {"class":"cnn_strycntntlft"}).find_all('p')
    paragraphs = soup.find('div', {"class":"cnn_strycntntlft"})
    #text = " ".join([ paragraph.text.encode('utf-8') for paragraph in paragraphs])
    print(url)
    print(date)
    print(title) 
    print(paragraphs)

if __name__ == '__main__':   
     main()