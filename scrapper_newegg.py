# coding=iso-8859-1
import json
from datetime import datetime
from urllib.request import urlopen

import nexmo

time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(time + ": Started running Scrapper Newegg...")

products = ["14-932-336", "14-487-518", "14-137-598", "14-137-597",
            "14-487-520", "14-126-452", "14-932-329", "14-126-457",
            "14-126-453", "14-932-330", "14-932-337", "14-487-519",
            "14-487-521", "14-487-522", "14-137-600", "14-932-367",
            "14-133-809", "14-932-345",
            "14-137-603", "14-126-459", "14-137-601", "14-487-528",
            "14-932-342", "14-932-359", "14-932-360", "14-137-602",
            "14-487-529", "14-487-531", "14-487-530", "14-137-605",
            "14-126-458", "14-487-532", "14-126-466", "14-126-461",
            "14-932-344", "14-126-460", "14-932-343"]
results = []
for product in products:
    url = "https://www.newegg.ca/product/api/ProductRealtime?ItemNumber=" + product + "&RecommendItem=&BestSellerItemList=&IsVATPrice=true"
    page = urlopen(url)
    html_bytes = page.read()
    jsonTxt = html_bytes.decode('utf-8')
    y = json.loads(jsonTxt)

    item = y['MainItem']
    hasQuantity = item['Qty'] > 0
    inStock = item['Instock']
    hasStock = item['Stock'] > 0
    if hasQuantity or inStock or hasStock:
        results.append("https://www.newegg.ca/p/pl?d=" + item['Description']['UrlKeywords'])

if results:
    print(time + ": Found an item on newegg")
    client = nexmo.Client(key='2e2108e3', secret='xR7tZzs8bqSEMJJj')
    client.send_message({
        'from': '12262471505',
        'to': '15145548991',
        'text': 'Hey video card are ready: ' + ' , '.join(results),
    })

else:
    print(time + ": Faut encore attendre pour newegg")
