__author__ = 'wangcl'

import os
path = os.path.join(os.path.dirname(__file__), "verified")
path1 = os.path.abspath(__file__)

path2 = os.path.join(__file__, '..', '..', '..', '..')
print path, path1, os.path.join(path2,"logs")