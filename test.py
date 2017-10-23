from operator import itemgetter

a=[7,0,1]
b=[8,5,2]
c=[9,6,3]

file=open("tester.csv","wb")

d=[]

for i in range(0,len(a)):
   temp=[]
   temp.append(a[i])
   temp.append(b[i])
   temp.append(c[i])
   d.append(temp)


d=sorted(d,key=itemgetter(2))

for i in d:
    print i

#for i in range(0,len(d)):
    #file.write(str(d[i][0])+','+str(d[i][1])+','+str(d[i][2])+'\n')