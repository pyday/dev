__author__ = 'wangcl'
import urllib2
#
# with open('/Users/wangcl/Documents/pictures/u=1983162016,2242015733&fm=58.jpeg', 'rb') as f:
#     content = f.read()
#     print content.encode("base64")

class Base(object):
    def __init__(self):
        print "Base"
    def do(self):
        pass
    def console(self):
        self.do()
        self.do()

class User(Base):
    def __init__(self):
        super(User, self).__init__()
        self.UserName = None
        self.PassWord = None
        self.console()
        print "User"

    def do(self):
        print "dodododod"


def do():
    print "abc"
    pass

# url = "http://wx.qlogo.cn/mmopen/KvibB8WtVs64FbBVOe5GnanmmoHN95fPNuU9gFYZrrg96McdOxJUlYnPXAPYm6qice9YH4OsujZTPkzKX3CiawSzKLQ8DpoVQng/132"
# req = urllib2.urlopen(url)
# CHUNK = 16 * 1024
# while True:
#     chunk = req.read(CHUNK)
#     if not chunk: break
#     print chunk.encode("base64")

# import log_ext
#
# logger = log_ext.getLogger("chun")
# logger.debug("debugger")
# logger.info("Info")
# logger.error("Error")
# logger.fatal("Fatal")


user = User()

import path
