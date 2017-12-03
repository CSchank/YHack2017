import string
from random import randint

file = open("/Users/macoutreachadmin/Documents/withwy.csv","r")
olines = file.readlines()
nf = open("6krand.csv","w")

nlines = []
nlines += olines[0]

used = []
for i in range(1,20000):
    nrand = randint(0,1482000)
    while(nrand in used):
        nrand = randint(0, 1482000)
    used += [nrand]
    print(nrand)
    nlines += [olines[nrand]]

nf.writelines(nlines)