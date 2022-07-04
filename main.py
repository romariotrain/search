import requests
from datetime import datetime
from pprint import pprint

def search_tag(days, tag):
    date_nowadays = datetime.timestamp(datetime.now())
    date_in_past = date_nowadays - days * 86400
    url = 'https://api.stackexchange.com/2.3/questions'
    params = {'from date': date_in_past,
              'to_date': date_nowadays,
              'tagged': tag,
              'site': 'stackoverflow'}
    response = requests.get(url,params=params)
    pprint(response.json())
search_tag(2,'python')