__author__ = 'wangcl'
import urllib2

with open('/Users/wangcl/Documents/pictures/u=1983162016,2242015733&fm=58.jpeg', 'rb') as f:
    content = f.read()
    print content.encode("base64")


class User(object):
    def __init__(self):
        self.UserName = None
        self.PassWord = None

    def do(self):
        pass


def do():
    print "abc"
    pass

url = "http://wx.qlogo.cn/mmopen/KvibB8WtVs64FbBVOe5GnanmmoHN95fPNuU9gFYZrrg96McdOxJUlYnPXAPYm6qice9YH4OsujZTPkzKX3CiawSzKLQ8DpoVQng/132"
req = urllib2.urlopen(url)
CHUNK = 16 * 1024
while True:
    chunk = req.read(CHUNK)
    if not chunk: break
    print chunk.encode("base64")


do()
