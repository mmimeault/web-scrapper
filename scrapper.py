# coding=iso-8859-1
import os
import re
from datetime import datetime
from urllib.request import urlopen

import nexmo

time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(time + ": Started running Scrapper Newegg...")

url = "http://www.premina.ca/puppage.htm"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode('iso-8859-1')
isBorn = re.search('(born|prêts)', html, re.IGNORECASE)

if isBorn:
    print(time + ": Il y a des bebes!")
    client = nexmo.Client(key='2e2108e3', secret='xR7tZzs8bqSEMJJj')
    client.send_message({
        'from': '12262471505',
        'to': '15145548991',
        'text': 'Hey puppies are ready -> http://www.premina.ca/puppage.htm',
    })
else:
    print(time + ": Faut encore attendre")
