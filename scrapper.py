# coding=iso-8859-1
from urllib.request import urlopen
import re
import os

url = "http://www.premina.ca/puppage.htm"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode('iso-8859-1')
isBorn = re.search('(born|prêts)', html, re.IGNORECASE)

filename = "output/born.txt"
os.makedirs(os.path.dirname(filename), exist_ok=True)

if isBorn:
    print("Il y a des bebes!")
    f = open(filename, "w")
    f.write("true")
    f.close()
else:
    print("Faut encore attendre")
    f = open(filename, "w")
    f.write("false")
    f.close()

