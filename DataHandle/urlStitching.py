"""
拼接url
"""
import time
import random
from urllib import parse


class createUrl(object):
    def __init__(self):
        pass

    def url_mod(self):
        url_mod = {
            "data-key": "s,ps",
            "data-value": "0,1",
            "ajax": "true",
            "_ksTS": str(time.time()*1000) + '_' +str(random.randint(1000, 9999)),
            "callback": "jsonp" + str(random.randint(1000, 9999)),
            "initiative_id": "tbindexz_20170306",
            "ie": "utf8",
            "spm": "a21bo.2017.201856-taobao-item.2",
            "sourceId": "tb.index",
            "search_type": "item",
            "ssid": "s5-e",
            "commend": "all",
            "imgfile": "",
            "q": "牙膏",  # 关键字
            "suggest": "0_1",
            "_input_charset": "utf-8",
            "wq": "yagao", # 关键字拼写
            "suggest_query": "yagao",
            "source": "suggest",
            "p4ppushleft": "1,48",
            "s": "176",
        }
        url =  parse.urlencode(url_mod)
        url = "https://s.taobao.com/search?data-key=s&" + url
        url_list = list()
        url_list.append(url)
        for i in range(100):
            url_mod["data-value"] = (i + 1) * 44
            url_mod["s"] = i * 44
            cache_dic = url_mod.copy()
            url =  parse.urlencode(cache_dic)
            url = "https://s.taobao.com/search?data-key=s&" + url
            url_list.append(url)
        return url_list


if __name__ == '__main__':
    xx = createUrl()

    for temp in xx.url_mod():
        print(temp)




