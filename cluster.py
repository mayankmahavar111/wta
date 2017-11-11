import os

def spil(x):
    x = x.split('/')[-1]
    x = x.split('?')[0]

    try:
        x = x.split('.')[1]
    except:
        pass
    x = x.split(" ")[0]
    x = x.split("-")[0]
    x = x.split(":")[0]

    x = x.split('docs')[0]

    return x

f=open('DCoutput.csv','r')
lis=f.readlines()
f.close()
dataset=[]
for i in range(1,len(lis)):
    dataset.append(lis[i].split(',')[3])
f=open('unique.txt','r')
topic=f.readlines()
f.close()


try:

    os.makedirs('cluster')
except:
    pass
test=[]
dic={}
i=0
for x in topic:
    f = open('cluster/' + x.split('\n')[0]+'.txt','wb')
    for j in dataset:
        temp=spil(j)
        if temp.isalpha():
            if temp+'\n' == x:
                f.write(j+'\n')

f.close()

print "Success"