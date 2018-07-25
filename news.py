#importing libraries
try:
    from bs4 import BeautifulSoup as soup
except ImportError:
    print "Install BeautifulSoup library"
try:
    from urllib import urlopen 
except ImportError:
    print "Install urllib library"
class news_report:

    def __init__(self):
        self.name = None #crating an instance
        
    def get_urls(self):
        urls = []
        urls_names = []
        urls.append("https://news.google.com/news/rss")
        urls_names.append("google news")
        return urls, urls_names

    def start_connection(self,url):
        client = urlopen(url)
        xml_page = client.read()
        client.close()
        return xml_page

    def read_news(self,xml_page):
        soup_page = soup(xml_page,"xml")
        news_list = soup_page.find_all("item")
        return news_list

    def show_data(self,urls_names,news_list):
        text = []
        for news in news_list:
            text.append(news.title.text)
        print "%s"%urls_names
        print "\n"
        try:
            for i in range(len(text)):
                print text[i]
                print "\n"
        except UnicodeEncodeError:
            pass
