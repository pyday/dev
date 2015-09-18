# __author__ = 'sswy'
# import werkzeug
# from collections import OrderedDict
#
# params = dict(
#
#     redirect_uri='aaaa',
#     response_type='code',
#     scope='aaaaddd',
#     appid='abc',
# )
# print OrderedDict(sorted(params.items(), key=lambda t: t[0]))
#
# print params
# print werkzeug.url_encode(params)

str1="%7B%22p%22%3A+4%2C+%22r%22%3A+%22web%22%2C+%22d%22%3A+%22odoo%22%7D"
str0 = str1.encode('base64')
print str0
str2= "eyJwIjogNCwgInIiOiAiaHR0cDovLzE5Mi4xNjguMzEuMTEwOjgwNjkvd2ViIiwgImQiOiAib2Rv"

print len(str2)

print str2.decode('base64')
