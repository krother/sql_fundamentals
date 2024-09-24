"""
Helper script that parses the US baby name data,
strips entries < 100 and writes a single SQL file.
"""
import os

path = "names/"

def readfile(fn):
    for line in open(fn):
        name, sex, count = line.strip().split(",")
        year = fn[-8:-4]
        if int(count) >= 100:
            s = f" ({year},'{name}','{sex}',{count}),\n"
            data.append(s)

data = ["INSERT INTO babynames VALUES\n"]

for fn in os.listdir(path):
    if fn.startswith("yob"):
        print(fn)
        readfile(path + fn)

data[-1] = data[-1][:-2] + "\n;\n"
open("allnames.sql", "w").writelines(data)
