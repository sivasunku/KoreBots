import requests
from flask import json

link = "https://www.nseindia.com/products/content/equities/indices/faqs.htm"
htmlraw = requests.get(link)
#print(f.text)
data = htmlraw.text
print("data\n")
print(data)

#jsonDumps = json.dumps(htmlraw.text)
#print("JSON")
#print(jsonDumps)
  
#get 
