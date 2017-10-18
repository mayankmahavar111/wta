import csv

file=open("DCoutput.csv","r")

data=[]
userCount=0
heading=['user ips']

output=open("UIoutput.csv","wb")
wr=csv.writer(output,dialect='excel')
wr.writerow(heading)

co=0

for x in file:
    if co==8:
        break
    (a)=x.split(",")
    print a
    co+=1

print userCount

for x in data:
    print x

