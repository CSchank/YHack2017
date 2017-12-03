import urllib3, simplejson

respv_par = http.request('GET', "https://v3v10.vitechinc.com/solr/v_participant/select?indent=on&wt=json" + "&q=id:" + "&rows=1482000" + "&fl=id,sex,longitude,latitude,state")
v_par = simplejson.loads(respv_par.data.decode('utf-8'))

for document in v_par['response']['docs']:
    for doc_key in document:
        print(doc_key, "=", document[doc_key])