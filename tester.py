file=open("log/data.csv","r")
data=[]
co=0
for x in file:
    if co==2:
        break
    (a)=x.split(",")
    data.append(a)
    co+=1
print len(data[1][3])