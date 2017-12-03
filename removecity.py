import string

file = open("data.csv","r")
nf = open("new.csv","w")

lines = file.readlines();
newlines = []

for line in lines:
    stuff = line.split(",")
    newline = []
    for i in range(0,len(stuff)):
        if (i != 5):
            newline += [stuff[i]]
    newline = ','.join(newline)
    newlines += [newline]

nf.writelines(newlines)
nf.close()