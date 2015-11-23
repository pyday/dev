__author__ = 'sswy'
import requests

response = requests.post('http://dwz.cn/create.php', data={'url': 'http://sswyuan.com/ycloud_base1/cfg/911c79db-ffdc-4b5a-8b15-36a89fc013e5'})
print response.json()['tinyurl']


