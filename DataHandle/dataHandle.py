# -*- coding: utf-8 -*-
import re
import json


class DataHandleJson(object):

    def data_clear(self, data):
        """
        清理抓取到的数据，并转换为json格式
        :return:
        """
        p = re.compile("jsonp\d{2,4}")
        data = re.sub(p, "jsonp", data)
        data = data.replace("jsonp(", "").replace(" ", "").replace('"{', "{").replace(" ,", "").replace('}"', "}")[:-2:]
        return data

    def data_handle(self, data):
        try:
            data = json.loads(data)
        except:
            data = data.replace('\\"', '"')
            data = json.loads(data)
        return data

    def json_data(self, data):
        data = self.data_clear(data)
        print(data)
        data = self.data_handle(data)
        return data["mods"]["itemlist"]["data"]["auctions"]


def parse_js(expr):
    """
    解析非标准JSON的Javascript字符串，等同于json.loads(JSON str)
    :param expr:非标准JSON的Javascript字符串
    :return:Python字典
    """
    import ast
    m = ast.parse(expr)
    a = m.body[0]
    def parse(node):
        if isinstance(node, ast.Expr):
            return parse(node.value)
        elif isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.Str):
            return node.s
        elif isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Dict):
            return dict(zip(map(parse, node.keys), map(parse, node.values)))
        elif isinstance(node, ast.List):
            return map(parse, node.elts)
        else:
            raise NotImplementedError(node.__class__)
    return parse(a)


if __name__ == '__main__':
    pass
    # yy = xx["mods"]["itemlist"]["data"]["auctions"]
    # print(yy)
    # print(len(yy))
    # for temp in yy:
    #     print(temp["raw_title"])
    #     print(temp["pic_url"])