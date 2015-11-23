# -*- coding: utf-8 -*-
__author__ = 'sswy'
from lxml import html
import requests

page = requests.get('http://public-dns.tk/nameserver/hk.html')
tree = html.fromstring(page.content)

ips = [tr.text.strip() for tr in tree.xpath(
    "//table/tbody/tr/td[count(preceding-sibling::td)+1 = count(ancestor::table/thead/tr/th[.='Price']/preceding-sibling::th)+1]")]


print ips
