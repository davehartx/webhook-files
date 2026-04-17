import requests
import json

webhook_url='https://webhook.site/14d4178c-264f-4a8c-ba74-2ed479210029'
webhook_url='http://127.0.0.1:5000/webhook'

data =  { 'name': 'Dave Jurnet' ,
          'channel url:': 'too much rabbit' }

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})  
