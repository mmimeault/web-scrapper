# coding=iso-8859-1
from urllib.request import urlopen
import re

url = "http://www.premina.ca/puppage.htm"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode('iso-8859-1')
isBorn = re.search('(born|prêts)', html, re.IGNORECASE)
if isBorn:
    print("Il y a des bebes!")
else:
    print("Faut encore attendre")

