#Reddit API Test
from collections import Counter
from pprint import pprint
import requests
import json

r = requests.get(r'http://www.reddit.com/user/rb640/comments/.json')

r.text

data = r.json()

for child in data['data']['children']:
    print child['data']['id'], "\r\n", child['data']['author'],child['data']['body']
