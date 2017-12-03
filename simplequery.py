import urllib3, simplejson

http = urllib3.PoolManager()

#respv_pard = http.request('GET',"https://v3v10.vitechinc.com/solr/v_participant_detail/select?indent=on&wt=json" + "&q=*:*" + "&rows=1" + "&sort=WEIGHT%20asc" + "&fl=id,HEIGHT,WEIGHT")
respv_par = http.request('GET', "https://v3v10.vitechinc.com/solr/v_participant/select?indent=on&wt=json" + "&q=*:*" + "&rows=1" + "&sort=latitude%20desc" + "&fl=id,DOB,city,sex,longitude,latitude,state")

v_par = simplejson.loads(respv_par.data.decode('utf-8'))

for document in v_par['response']['docs']:
    for doc_key in document:
        print(doc_key, "=", document[doc_key])