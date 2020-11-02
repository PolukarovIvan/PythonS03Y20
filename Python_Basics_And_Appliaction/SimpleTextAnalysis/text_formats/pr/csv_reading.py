import csv
import re
import operator
d = {}
with open("C:/Users/vanis/Downloads/Crimes.csv") as file:
    for row in csv.reader(file):
        if "/2015" in "".join(row):
            if row[5] in d:
                d[row[5]] += 1
            else:
                d[row[5]] = 1

d_new = sorted(d, key=lambda x: d[x])
a = [(x, d[x]) for x in d_new]
print(a[-1])