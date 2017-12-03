import urllib3, simplejson
from datetime import datetime

http = urllib3.PoolManager()
# get basic information about the person

stateL = ["NULL",
"Alabama",
"Alaska",
"Arizona",
"Arkansas",
"California",
"Colorado",
"Connecticut",
"District of Columbia",
"Delaware",
"Florida",
"Georgia",
"Hawaii",
"Idaho",
"Illinois",
"Indiana",
"Iowa",
"Kansas",
"Kentucky",
"Louisiana",
"Maine",
"Maryland",
"Massachusetts",
"Michigan",
"Minnesota",
"Mississippi",
"Missouri",
"Montana",
"Nebraska",
"Nevada",
"New Hampshire",
"New Jersey",
"New Mexico",
"New York",
"North Carolina",
"North Dakota",
"Ohio",
"Oklahoma",
"Oregon",
"Pennsylvania",
"Rhode Island",
"South Carolina",
"South Dakota",
"Tennessee",
"Texas",
"Utah",
"Vermont",
"Virginia",
"Washington",
"West Virginia",
"Wisconsin",
"Wyoming"]

stateDict = { stateL[i]: i for i in range(0,52) }

def genCatStr(preconds):
    preconds = simplejson.loads(preconds)
    labels = ['a00_b99_high', 'a00_b99_med', 'a00_b99_low',
    'c00_d49_high', 'c00_d49_med', 'c00_d49_low',
    'd50_d89_high', 'd50_d89_med', 'd50_d89_low',
    'e00_e89_high', 'e00_e89_med', 'e00_e89_low',
    'f01_f99_high', 'f01_f99_med', 'f01_f99_low',
    'g00_g99_high', 'g00_g99_med', 'g00_g99_low',
    'h00_h59_high', 'h00_h59_med', 'h00_h59_low',
    'h60_h95_high', 'h60_h95_med', 'h60_h95_low',
    'i00_i99_high', 'i00_i99_med', 'i00_i99_low',
    'j00_j99_high', 'j00_j99_med', 'j00_j99_low',
    'k00_k95_high', 'k00_k95_med', 'k00_k95_low',
    'l00_l99_high', 'l00_l99_med', 'l00_l99_low',
    'm00_m99_high', 'm00_m99_med', 'm00_m99_low',
    'n00_n99_high', 'n00_n99_med', 'n00_n99_low',
    'o00_o9a_high', 'o00_o9a_med', 'o00_o9a_low',
    'p00_p96_high', 'p00_p96_med', 'p00_p96_low',
    'q00_q99_high', 'q00_q99_med', 'q00_q99_low',
    'r00_r99_high', 'r00_r99_med', 'r00_r99_low',
    's00_t88_high', 's00_t88_med', 's00_t88_low',
    'v00_y99_high', 'v00_y99_med', 'v00_y99_low',
    'z00_z99_high', 'z00_z99_med', 'z00_z99_low']
    dict = {el:0 for el in labels}
    rf = "Risk_factor"
    h = "High"
    m = "Medium"
    l = "Low"
    for precond in preconds:
        if(precond["ICD_CODE"][0] == 'A'):
            if (precond[rf] == h):
                dict["a00_b99_high"]+=1
            elif (precond[rf] == m):
                dict["a00_b99_med"]+=1
            elif (precond[rf] == l):
                dict["a00_b99_low"]+=1
        elif(precond["ICD_CODE"][0] == 'B'):
            if (precond[rf] == h):
                dict["a00_b99_high"]+=1
            elif (precond[rf] == m):
                dict["a00_b99_med"]+=1
            elif (precond[rf] == l):
                dict["a00_b99_low"]+=1
        elif(precond["ICD_CODE"][0] == 'C'):
            if (precond[rf] == h):
                dict["c00_d49_high"]+=1
            elif (precond[rf] == m):
                dict["c00_d49_med"]+=1
            elif (precond[rf] == l):
                dict["c00_d49_low"]+=1
        elif(precond["ICD_CODE"][0] == 'D'):
            if (precond["ICD_CODE"][1] <= '4'):
                if (precond[rf] == h):
                    dict["c00_d49_high"]+=1
                elif (precond[rf] == m):
                    dict["c00_d49_med"]+=1
                elif (precond[rf] == l):
                    dict["c00_d49_low"]+=1
            else:
                if (precond[rf] == h):
                    dict["d50_d89_high"]+=1
                elif (precond[rf] == m):
                    dict["d50_d89_med"]+=1
                elif (precond[rf] == l):
                    dict["d50_d89_low"]+=1
        elif(precond["ICD_CODE"][0] == 'E'):
            if (precond[rf] == h):
                dict["e00_e89_high"] += 1
            elif (precond[rf] == m):
                dict["e00_e89_med"] += 1
            elif (precond[rf] == l):
                dict["e00_e89_low"] += 1
        elif(precond["ICD_CODE"][0] == 'F'):
            if (precond[rf] == h):
                dict["f01_f99_high"] += 1
            elif (precond[rf] == m):
                dict["f01_f99_med"] += 1
            elif (precond[rf] == l):
                dict["f01_f99_low"] += 1
        elif(precond["ICD_CODE"][0] == 'G'):
            if (precond[rf] == h):
                dict["g00_g99_high"] += 1
            elif (precond[rf] == m):
                dict["g00_g99_med"] += 1
            elif (precond[rf] == l):
                dict["g00_g99_low"] += 1
        elif(precond["ICD_CODE"][0] == 'H'):
            if precond["ICD_CODE"][1] <= '5':
                if (precond[rf] == h):
                    dict["h00_h59_high"] += 1
                elif (precond[rf] == m):
                    dict["h00_h59_med"] += 1
                elif (precond[rf] == l):
                    dict["h00_h59_low"] += 1
            else:
                if (precond[rf] == h):
                    dict["h60_h95_high"] += 1
                elif (precond[rf] == m):
                    dict["h60_h95_med"] += 1
                elif (precond[rf] == l):
                    dict["h60_h95_low"] += 1
        elif(precond["ICD_CODE"][0] == 'I'):
            if (precond[rf] == h):
                dict["i00_i99_high"] += 1
            elif (precond[rf] == m):
                dict["i00_i99_med"] += 1
            elif (precond[rf] == l):
                dict["i00_i99_low"] += 1
        elif(precond["ICD_CODE"][0] == 'J'):
            if (precond[rf] == h):
                dict["j00_j99_high"] += 1
            elif (precond[rf] == m):
                dict["j00_j99_med"] += 1
            elif (precond[rf] == l):
                dict["j00_j99_low"] += 1
        elif(precond["ICD_CODE"][0] == 'K'):
            if (precond[rf] == h):
                dict["k00_k95_high"] += 1
            elif (precond[rf] == m):
                dict["k00_k95_med"] += 1
            elif (precond[rf] == l):
                dict["k00_k95_low"] += 1
        elif(precond["ICD_CODE"][0] == 'L'):
            if (precond[rf] == h):
                dict["l00_l99_high"] += 1
            elif (precond[rf] == m):
                dict["l00_l99_med"] += 1
            elif (precond[rf] == l):
                dict["l00_l99_low"] += 1
        elif(precond["ICD_CODE"][0] == 'M'):
            if (precond[rf] == h):
                dict["m00_m99_high"] += 1
            elif (precond[rf] == m):
                dict["m00_m99_med"] += 1
            elif (precond[rf] == l):
                dict["m00_m99_low"] += 1
        elif(precond["ICD_CODE"][0] == 'N'):
            if (precond[rf] == h):
                dict["n00_n99_high"] += 1
            elif (precond[rf] == m):
                dict["n00_n99_med"] += 1
            elif (precond[rf] == l):
                dict["n00_n99_low"] += 1
        elif(precond["ICD_CODE"][0] == 'O'):
            if (precond[rf] == h):
                dict["o00_o9a_high"] += 1
            elif (precond[rf] == m):
                dict["o00_o9a_med"] += 1
            elif (precond[rf] == l):
                dict["o00_o9a_low"] += 1
        elif(precond["ICD_CODE"][0] == 'P'):
            if (precond[rf] == h):
                dict["p00_p96_high"] += 1
            elif (precond[rf] == m):
                dict["p00_p96_med"] += 1
            elif (precond[rf] == l):
                dict["p00_p96_low"] += 1
        elif(precond["ICD_CODE"][0] == 'Q'):
            if (precond[rf] == h):
                dict["q00_q99_high"] += 1
            elif (precond[rf] == m):
                dict["q00_q99_med"] += 1
            elif (precond[rf] == l):
                dict["q00_q99_low"] += 1
        elif(precond["ICD_CODE"][0] == 'R'):
            if (precond[rf] == h):
                dict["r00_r99_high"] += 1
            elif (precond[rf] == m):
                dict["r00_r99_med"] += 1
            elif (precond[rf] == l):
                dict["r00_r99_low"] += 1
        elif(precond["ICD_CODE"][0] == 'S'):
            if (precond[rf] == h):
                dict["s00_t88_high"] += 1
            elif (precond[rf] == m):
                dict["s00_t88_med"] += 1
            elif (precond[rf] == l):
                dict["s00_t88_low"] += 1
        elif(precond["ICD_CODE"][0] == 'T'):
            if (precond[rf] == h):
                dict["s00_t88_high"] += 1
            elif (precond[rf] == m):
                dict["s00_t88_med"] += 1
            elif (precond[rf] == l):
                dict["s00_t88_low"] += 1
        elif(precond["ICD_CODE"][0] == 'V'):
            if (precond[rf] == h):
                dict["v00_y99_high"] += 1
            elif (precond[rf] == m):
                dict["v00_y99_med"] += 1
            elif (precond[rf] == l):
                dict["v00_y99_low"] += 1
        elif(precond["ICD_CODE"][0] == 'W'):
            if (precond[rf] == h):
                dict["v00_y99_high"] += 1
            elif (precond[rf] == m):
                dict["v00_y99_med"] += 1
            elif (precond[rf] == l):
                dict["v00_y99_low"] += 1
        elif(precond["ICD_CODE"][0] == 'X'):
            if (precond[rf] == h):
                dict["v00_y99_high"] += 1
            elif (precond[rf] == m):
                dict["v00_y99_med"] += 1
            elif (precond[rf] == l):
                dict["v00_y99_low"] += 1
        elif(precond["ICD_CODE"][0] == 'Y'):
            if (precond[rf] == h):
                dict["v00_y99_high"] += 1
            elif (precond[rf] == m):
                dict["v00_y99_med"] += 1
            elif (precond[rf] == l):
                dict["v00_y99_low"] += 1
        elif(precond["ICD_CODE"][0] == 'Z'):
            if (precond[rf] == h):
                dict["z00_z99_high"] += 1
            elif (precond[rf] == m):
                dict["z00_z99_med"] += 1
            elif (precond[rf] == l):
                dict["z00_z99_low"] += 1

    catstr = ""
    for lbl in labels:
        catstr += "%d," % dict[lbl]

    return catstr

def calcAge(birthday):
    born = datetime.strptime(birthday[0:10], "%Y-%m-%d")

    today = datetime.now()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def processLine(v_par, v_pard, v_quotes):
    id = int(v_par["id"])
    age = calcAge(v_par["DOB"])
    height = v_pard["HEIGHT"]
    sex    = 0 if v_par["sex"] == "M" else 1
    weight = v_pard["WEIGHT"]
    city   = v_par["city"]
    try:
        state  = stateDict[v_par["state"]]
    except:
        state = stateDict["NULL"]
    long   = v_par["longitude"]
    lat    = v_par["latitude"]
    marst  = 1 if v_pard["MARITAL_STATUS"] == "M" else 0
    tobac  = 1 if v_pard["TOBACCO"] == "Yes" else 0
    optins = v_pard["OPTIONAL_INSURED"]
    anninc = v_pard["ANNUAL_INCOME"]
    peepcv = v_pard["PEOPLE_COVERED"]
    linestr = "%d,%d,%d,%d,%d,%s,%d,%d,%d,%d,%d,%d,%d,%d," %(id,age,sex,height,weight,city,state,long,lat,marst,tobac,optins,anninc,peepcv)
    try:
        linestr += genCatStr(v_pard["PRE_CONDITIONS"])
    except:
        linestr += "0,"*21*3
    bronze = v_quotes["BRONZE"]
    silver = v_quotes["SILVER"]
    gold = v_quotes["GOLD"]
    platin = v_quotes["PLATINUM"]
    if v_quotes["PURCHASED"] == "Bronze":
        purch = 0
    elif v_quotes["PURCHASED"] == "Silver":
        purch = 1
    elif v_quotes["PURCHASED"] == "Gold":
        purch = 2
    elif v_quotes["PURCHASED"] == "Platinum":
        purch = 3
    linestr += "%d,%d,%d,%d,%d" % (bronze, silver, gold, platin, purch)
    return linestr


if __name__ == "__main__":
    cats = ['a00_b99_high', 'a00_b99_med', 'a00_b99_low',
                'c00_d49_high', 'c00_d49_med', 'c00_d49_low',
                'd50_d89_high', 'd50_d89_med', 'd50_d89_low',
                'e00_e89_high', 'e00_e89_med', 'e00_e89_low',
                'f01_f99_high', 'f01_f99_med', 'f01_f99_low',
                'g00_g99_high', 'g00_g99_med', 'g00_g99_low',
                'h00_h59_high', 'h00_h59_med', 'h00_h59_low',
                'h60_h95_high', 'h60_h95_med', 'h60_h95_low',
                'i00_i99_high', 'i00_i99_med', 'i00_i99_low',
                'j00_j99_high', 'j00_j99_med', 'j00_j99_low',
                'k00_k95_high', 'k00_k95_med', 'k00_k95_low',
                'l00_l99_high', 'l00_l99_med', 'l00_l99_low',
                'm00_m99_high', 'm00_m99_med', 'm00_m99_low',
                'n00_n99_high', 'n00_n99_med', 'n00_n99_low',
                'o00_o9a_high', 'o00_o9a_med', 'o00_o9a_low',
                'p00_p96_high', 'p00_p96_med', 'p00_p96_low',
                'q00_q99_high', 'q00_q99_med', 'q00_q99_low',
                'r00_r99_high', 'r00_r99_med', 'r00_r99_low',
                's00_t88_high', 's00_t88_med', 's00_t88_low',
                'v00_y99_high', 'v00_y99_med', 'v00_y99_low',
                'z00_z99_high', 'z00_z99_med', 'z00_z99_low']

def genHeader():
    header = "id,age,sex,height,weight,city,state,longitude,latitude,marital_status,tobacco,optional_insurance,annual_income,people_covered,"
    for str in cats:
        header += str + ","
    header += "bronze_quote,silver_quote,gold_quote,platinum_quote,purchased_plan"

    return header + '\n'

def genOrStr(st,e):
    s = "&q=id:("
    for i in range(st,e - 1):
        s += str(i) + "%20OR%20"
    s += str(e - 1) + ")"
    return s

if __name__ == "__main__":
    f = open("data.csv", "w")
    f.write(genHeader())

    startrow  = 1
    chunksize = 500
    fetchrows = 1482000
    for i in range(startrow,fetchrows+1,chunksize):
        respv_par = http.request('GET', "https://v3v10.vitechinc.com/solr/v_participant/select?indent=on&wt=json" + genOrStr(i,i+chunksize) + "&rows=1000" + "&fl=id,DOB,city,sex,longitude,latitude,state")
        respv_pard = http.request('GET', "https://v3v10.vitechinc.com/solr/v_participant_detail/select?indent=on&wt=json" + genOrStr(i,i+chunksize) + "&rows=1000" + "&fl=id,EMPLOYMENT_STATUS,PEOPLE_COVERED,TOBACCO,MARITAL_STATUS,ANNUAL_INCOME,OPTIONAL_INSURED,HEIGHT,WEIGHT,PRE_CONDITIONS")
        respv_quotes = http.request('GET', "https://v3v10.vitechinc.com/solr/v_quotes/select?indent=on&wt=json" + genOrStr(i,i+chunksize) + "&rows=1000" "&fl=id,BRONZE,SILVER,GOLD,PLATINUM,PURCHASED")

        print("Status: "+ str(respv_par.status))
        v_par = simplejson.loads(respv_par.data.decode('utf-8'))
        v_pard = simplejson.loads(respv_pard.data.decode('utf-8'))
        v_quotes = simplejson.loads(respv_quotes.data.decode('utf-8'))

        for j in range(chunksize):
            line = processLine(v_par['response']['docs'][j],v_pard['response']['docs'][j],v_quotes['response']['docs'][j]) + '\n'
            f.write(line)

        print("Loaded row %d of %d (%.1f %%)" % (i+chunksize-1, fetchrows, 100*(i+chunksize-1)/fetchrows))

    f.close()