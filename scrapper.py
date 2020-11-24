# coding=iso-8859-1
from urllib.request import urlopen
import re

url = "http://www.premina.ca/puppage.htm"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode('iso-8859-1')
isBorn = re.search('(born|prêts|a)', html, re.IGNORECASE)
if isBorn:
    print("Il y a des bebes!")
    f = open("born.txt", "w")
    f.write("true")
    f.close()
else:
    print("Faut encore attendre")
    f = open("born.txt", "w")
    f.write("false")
    f.close()

