__author__ = 'wangcl'
import urllib

with open('/Users/wangcl/Documents/pictures/u=1983162016,2242015733&fm=58.jpeg', 'rb') as f:
    content = f.read()
    print content.encode("base64")


class User(object):
    def __init__(self):
        self.UserName = None
        self.PassWord = None

user = User()
user.UserName="aa"
