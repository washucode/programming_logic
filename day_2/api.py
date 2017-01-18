import requests 
url= "http://www.glamourmagazine.co.uk/?international"
r = requests.get(url)
lay = r.encoding
s= r.status_code

print r.text 
print lay
print s










