import requests

# constants
RUN_URL = u'http://api.hackerearth.com/code/run/'

CLIENT_SECRET = 'e9b31d9bff43f1a393ec3519515a9cd0b4bc7438'

source = open('hello.py', 'r')
"""
test.py
#! -*- coding: utf-8 -*-

def square(no):
    return no * no

print(square(-23))
"""

data = {
    'client_secret': CLIENT_SECRET,
    'async': 0,
    'source': source.read(),
    'lang': "PYTHON",
    'time_limit': 5,
    'memory_limit': 262144,
}

r = requests.post(RUN_URL, data=data)
source.close()
print r.json()
