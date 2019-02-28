# -*- coding: utf-8 -*-
import requests
from config import config
from DataHandle.urlStitching import createUrl
from DataHandle.dataHandle import DataHandleJson


class TaoBaoSpider(object):
    def __init__(self):
        self.start_url = createUrl().url_mod()
        self.session = requests.session()

    def parse_url(self, url):
        headers = config.headers
        headers["cookie"] = config.cookies
        return self.session.get(url, headers=headers).text

    def main(self):
        for temp in self.start_url:
            html_str = self.parse_url(temp)
            data = DataHandleJson().json_data(html_str)
            for temp in data:
                print(temp["raw_title"])
                print(temp["pic_url"])


if __name__ == '__main__':
    xx = TaoBaoSpider()
    xx.main()