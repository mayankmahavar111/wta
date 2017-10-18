import csv
from collections import defaultdict

mylist=[]

columns = defaultdict(list)  # each value in each column is appended to a list

with open('DCoutput.csv') as f:
    reader = csv.DictReader(f)  # read rows into a dictionary format
    for row in reader:  # read a row as {column1: value1, column2: value2,...}
        for (k, v) in row.items():
            mylist.append(k)  # go over each column name and value
            columns[k].append(v)
mylist = list(set(mylist))
# print len(columns),len(mylist)
print len(mylist),len(columns)
print mylist[0],len(columns[mylist[0]])

k=0


for x in columns[mylist[0]]:
    print x
    k+=1
    if k>10 :
        break