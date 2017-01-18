import requests
url= "http://www.glamourmagazine.co.uk/?international"
r = requests.get(url)
lay = r.encoding
s= r.status_code
cookies = dict(cookies_are='working')

r = requests.get(url, cookies=cookies)
print r.text
print lay
print s










