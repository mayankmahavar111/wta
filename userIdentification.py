import csv

file=open("DCoutput.csv","r")
data=[]
userCount=0
heading='user ips'+'\n'

output=open("UIoutput.csv","wb")
<<<<<<< HEAD
output.write(heading)
=======
"""
wr=csv.writer(output,dialect='excel')
wr.writerow(heading)
"""
co=0
>>>>>>> 71c17c8c7546b45490c319881f4f99506d3463e1

output.write("user ips"+'\n')

for x in file:
    (a)=x.split(",")
    data.append(a[0])
<<<<<<< HEAD

data=list(set(data))

print len(data)

for x in data:
    output.write(x+'\n')
=======
data=list(set(data))

print len(data)

k=0

for x in data:
    k+=1
    print k
    output.write(x+"\n")
>>>>>>> 71c17c8c7546b45490c319881f4f99506d3463e1


