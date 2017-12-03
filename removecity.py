import string
from random import randint

file = open("data.csv","r")
olines = file.readlines()
nf = open("withwy.csv","w")

#nlines = []
#nlines += olines[0]

#used = []
#for i in range(1,20000):
#    nrand = randint(0,1482000)
#    while(nrand in used):
#        nrand = randint(0, 1482000)
#    used += [nrand]
#    print(nrand)
#    nlines += [olines[nrand]]

#nf.writelines(nlines)






lines = file.readlines();
newlines = []

for i,line in enumerate(lines):
    if i % 10000 == 0:
        print("%d of 1482000 (%.1f%%)" % (i, i/1482000))
    stuff = line.split(",")
    newline = []
    for i in range(0,len(stuff)):
        if (i != 5):
            newline += [stuff[i]]
    newline = ','.join(newline)
    newlines += [newline]

nf.writelines(newlines)
nf.close()