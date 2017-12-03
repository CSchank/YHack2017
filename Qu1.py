import urllib3, simplejson, json

http = urllib3.PoolManager()

chunksize = 500
i = 0

def genOrStr(st,e):
    s = "&q=id:("
    for i in range(st,e - 1):
        s += str(i) + "%20OR%20"
    s += str(e - 1) + ")"
    return s

#   for doc_key in document:
#       print(doc_key, "=", document[doc_key])


def genCatStr(preconds,longitude,latitude):
    precondin = simplejson.loads(preconds)
    labels = ['heat_1_long',    'heat_1_lat',
    'heat_2_long', 'heat_2_lat',
    'heat_3_long', 'heat_3_lat',
    'heat_4_long', 'heat_4_lat',
    'heat_5_long', 'heat_5_lat',
    'heat_6_long', 'heat_6_lat',
    'heat_7_long', 'heat_7_lat',
    'heat_8_long', 'heat_8_lat',
    'heat_9_long', 'heat_9_lat',
    'heat_10_long', 'heat_10_lat',
    'heat_11_long', 'heat_11_lat',
    'heat_12_long', 'heat_12_lat',
    'heat_13_long', 'heat_13_lat',
    'heat_14_long', 'heat_14_lat',
    'heat_15_long', 'heat_15_lat',
    'heat_16_long', 'heat_16_lat',
    'heat_17_long', 'heat_17_lat',
    'heat_18_long', 'heat_18_lat',
    'heat_19_long', 'heat_19_lat',
    'heat_20_long', 'heat_20_lat',
    'heat_21_long', 'heat_21_lat']

    dict = {el:0 for el in labels}

    heat_1_long = []
    heat_1_lat = []
    heat_2_long = []
    heat_2_lat = []
    heat_3_long = []
    heat_3_lat = []
    heat_4_long = []
    heat_4_lat = []
    heat_5_long = []
    heat_5_lat = []
    heat_6_long = []
    heat_6_lat = []
    heat_7_long = []
    heat_7_lat = []
    heat_8_long = []
    heat_8_lat = []
    heat_9_long = []
    heat_9_lat = []
    heat_10_long = []
    heat_10_lat = []
    heat_11_long = []
    heat_11_lat = []
    heat_12_long = []
    heat_12_lat = []
    heat_13_long = []
    heat_13_lat = []
    heat_14_long = []
    heat_14_lat = []
    heat_15_long = []
    heat_15_lat = []
    heat_16_long = []
    heat_16_lat = []
    heat_17_long = []
    heat_17_lat = []
    heat_18_long = []
    heat_18_lat = []
    heat_19_long = []
    heat_19_lat = []
    heat_20_long = []
    heat_20_lat = []
    heat_21_long = []
    heat_21_lat = []

    for precond in precondin:
        if(precond["ICD_CODE"][0] == 'A'):
            heat_1_long.append(longitude)
            heat_1_lat.append(latitude)
        elif(precond["ICD_CODE"][0] == 'B'):
            heat_1_long.append(longitude)
            heat_1_lat.append(latitude)
        elif(precond["ICD_CODE"][0] == 'C'):
            heat_2_long.append(longitude)
            heat_2_lat.append(latitude)
        elif(precond["ICD_CODE"][0] == 'D'):
            if (precond["ICD_CODE"][1] <= '4'):
                heat_2_long.append(longitude)
                heat_2_lat.append(latitude)
            else:
                heat_3_long.append(longitude)
                heat_3_lat.append(latitude)
        elif(precond["ICD_CODE"][0] == 'E'):
            heat_4_long.append(longitude)
            heat_4_lat.append(latitude)
        elif(precond["ICD_CODE"][0] == 'F'):
            heat_5_long.append(longitude)
            heat_5_lat.append(latitude)
        elif(precond["ICD_CODE"][0] == 'G'):
            heat_6_long.append(longitude)
            heat_6_lat.append(latitude)
        elif(precond["ICD_CODE"][0] == 'H'):
            if precond["ICD_CODE"][1] <= '5':
                heat_7_long.append(longitude)
                heat_7_lat.append(latitude)
            else:
                heat_8_long.append(longitude)
                heat_8_lat.append(latitude)
        elif(precond["ICD_CODE"][0] == 'I'):
            heat_9_long.append(longitude)
            heat_9_lat.append(latitude)
        elif(precond["ICD_CODE"][0] == 'J'):
            heat_10_long.append(longitude)
            heat_10_lat.append(latitude)
        elif(precond["ICD_CODE"][0] == 'K'):
            heat_11_long.append(longitude)
            heat_11_lat.append(latitude)
        elif(precond["ICD_CODE"][0] == 'L'):
            heat_12_long.append(longitude)
            heat_12_lat.append(latitude)
        elif(precond["ICD_CODE"][0] == 'M'):
            heat_13_long.append(longitude)
            heat_13_lat.append(latitude)
        elif(precond["ICD_CODE"][0] == 'N'):
            heat_14_long.append(longitude)
            heat_14_lat.append(latitude)
        elif(precond["ICD_CODE"][0] == 'O'):
            heat_15_long.append(longitude)
            heat_15_lat.append(latitude)
        elif(precond["ICD_CODE"][0] == 'P'):
            heat_16_long.append(longitude)
            heat_16_lat.append(latitude)
        elif(precond["ICD_CODE"][0] == 'Q'):
            heat_17_long.append(longitude)
            heat_17_lat.append(latitude)
        elif(precond["ICD_CODE"][0] == 'R'):
            heat_18_long.append(longitude)
            heat_18_lat.append(latitude)
        elif(precond["ICD_CODE"][0] == 'S'):
            heat_19_long.append(longitude)
            heat_19_lat.append(latitude)
        elif(precond["ICD_CODE"][0] == 'T'):
            heat_19_long.append(longitude)
            heat_19_lat.append(latitude)
        elif(precond["ICD_CODE"][0] == 'V'):
            heat_20_long.append(longitude)
            heat_20_lat.append(latitude)
        elif(precond["ICD_CODE"][0] == 'W'):
            heat_20_long.append(longitude)
            heat_20_lat.append(latitude)
        elif(precond["ICD_CODE"][0] == 'X'):
            heat_20_long.append(longitude)
            heat_20_lat.append(latitude)
        elif(precond["ICD_CODE"][0] == 'Y'):
            heat_20_long.append(longitude)
            heat_20_lat.append(latitude)
        elif(precond["ICD_CODE"][0] == 'Z'):
            heat_21_long.append(longitude)
            heat_21_lat.append(latitude)

    returnArr = [ heat_1_long,
    heat_1_lat,
    heat_2_long,
    heat_2_lat,
    heat_3_long,
    heat_3_lat,
    heat_4_long,
    heat_4_lat,
    heat_5_long,
    heat_5_lat,
    heat_6_long,
    heat_6_lat,
    heat_7_long,
    heat_7_lat,
    heat_8_long,
    heat_8_lat,
    heat_9_long,
    heat_9_lat,
    heat_10_long,
    heat_10_lat,
    heat_11_long,
    heat_11_lat,
    heat_12_long,
    heat_12_lat,
    heat_13_long,
    heat_13_lat,
    heat_14_long,
    heat_14_lat,
    heat_15_long,
    heat_15_lat,
    heat_16_long,
    heat_16_lat,
    heat_17_long,
    heat_17_lat,
    heat_18_long,
    heat_18_lat,
    heat_19_long,
    heat_19_lat,
    heat_20_long,
    heat_20_lat,
    heat_21_long,
    heat_21_lat ]

    with open('TonsOfArrays.json', 'a') as fi:
        json.dump(returnArr, fi)

    with open('TonsOfArrays.txt', 'a') as f:
        json.dump(returnArr, f)

    print(returnArr)
    # return returnArr

#for i in range(0, 1482000, 5000):

for i in range(0, 1482000, 5000):
    respv_pard = http.request('GET', "https://v3v10.vitechinc.com/solr/v_participant_detail/select?indent=on&wt=json" + genOrStr(i, i + chunksize) + "&rows=1000" + "&fl=id,PRE_CONDITIONS")
    respv_par = http.request('GET', "https://v3v10.vitechinc.com/solr/v_participant/select?indent=on&wt=json" + genOrStr(i, i + chunksize) + "&rows=1000" + "&fl=id,longitude,latitude")
    v_par = simplejson.loads(respv_par.data.decode('utf-8'))
    v_pard = simplejson.loads(respv_pard.data.decode('utf-8'))
    for i in range(500):
        try:
            genCatStr(v_pard['response']['docs'][i]['PRE_CONDITIONS'], v_par['response']['docs'][i]['longitude'], v_par['response']['docs'][i]['latitude'])
        except:
            print("Whoops!")
