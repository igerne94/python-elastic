import json

print("Print inside environment")

queryurl = "http://159.65.56.87/test_insert/_search?pretty"

body=json.dumps( {"query": {"match_all": {}}} )
hdict = {'Content-type': 'application/json; charset=UTF-8'}

response = requests.post(queryurl, headers=hdict, data=body)

text = response.text
status = response.status_code
js = json.load(text)