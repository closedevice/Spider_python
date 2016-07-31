from com.spider.downloader import html_downloader
from com.spider.manager import url_manager
from com.spider.parser import html_parser
from com.spider.store import html_outputer


class Main(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():

            try:
                new_url = self.urls.get_new_url()
                print('craw %d:%s' % (count, new_url))
                html_cont = self.downloader.downloader(new_url)
                new_urls, new_data = self.parser.parser(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 500:
                    break;

                count = count + 1
            except:
                print('craw failed', new_url)

        self.outputer.output_html()


if __name__ == '__main__':
    root_url = "http://baike.baidu.com/view/21187.htm"
    obj_spider = Main()
    # print(dir(obj_spider))
    # obj_spider.craw(root_url)
