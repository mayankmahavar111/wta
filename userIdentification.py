import csv

file=open("DCoutput.csv","r")

data=[]
userCount=0
heading=['user ips']

output=open("UIoutput.csv","wb")
"""
wr=csv.writer(output,dialect='excel')
wr.writerow(heading)
"""
co=0

output.write("user ips"+'\n')

for x in file:
    (a)=x.split(",")
    data.append(a[0])
data=list(set(data))

print len(data)

for x in data:
    output.write(x+"\n")


