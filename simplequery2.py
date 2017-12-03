import urllib3, simplejson

http = urllib3.PoolManager()
response = http.request('GET', "https://v3v10.vitechinc.com/solr/v_participant/select?indent=on&wt=json" + "&q=*:*" + "&rows=1482000" + "&fl=id,sex,longitude,latitude,state")
print(response.status)
json = simplejson.loads(response.data.decode('utf-8'))
print(json)
print(json['response']['numFound'], "documents found.")

# Print the fields of each document.

for document in json['response']['docs']:
    for doc_key in document:
        print(doc_key, "=", document[doc_key])