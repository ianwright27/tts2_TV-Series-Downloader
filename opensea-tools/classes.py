import requests
from bs4 import BeautifulSoup


sample_header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

class LinkFromHref:
    def __init__(self, link):
        self.link = link
        pass

    def get_collection_data(self):
        # use bs4
        url_prefix = "https://opensea.io"
        sp = BeautifulSoup(self.run_request(), 'lxml')
        div = sp.select('.CollectionLinkreact__DivContainer-sc-gv7u44-0.jMcPQU')
        # link
        collection_link = f"{url_prefix}{div[0].a.get('href')}"
        # name
        collection_name = div[0].a.string
        # print("COLLECTION_NAME: ", collection_name)

        div = sp.select('.Blockreact__Block-sc-1xf18x6-0 .elqhCm .item--description-text')
        div2 = ""
        if div == []:
            # print('Empty description')
            div2 = "[Empty description]"
        else:
            div2 = div[0].div.get_text()
        # desc
        collection_desc = div2
        return {'name': collection_name, 'link': collection_link, 'desc': collection_desc}
    
    def get_other_collection_data(self):
        # for other featured collections
        # use bs4
        url_prefix = "https://opensea.io"
        sp = BeautifulSoup(self.run_request(), 'lxml')
        div = sp.select('h1')
        # link
        collection_link = self.link
        # name
        collection_name = div[0].string
        div = sp.select('.CollectionHeader--description')
        try:
            div2 = div[0].p.get_text()
        except AttributeError:
            div2 = div[0].get_text()
        # desc
        collection_desc = div2
        return {'name': collection_name, 'link': collection_link, 'desc': collection_desc}

    def run_request(self):
        # use requests
        s = requests.Session()
        s.headers.update(sample_header)
        r = s.get(self.link)
        return r.text

