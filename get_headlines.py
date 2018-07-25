import news

instance = news.news_report()
            
def start_execution():
    print "starting news display"
    urls, urls_names = instance.get_urls()
    for i in range(len(urls)):
        xml = instance.start_connection(urls[i])
        news = instance.read_news(xml)
        instance.show_data(urls_names[i],news)

start_execution()
