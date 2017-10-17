import csv
import re

def extract(x):
    data=re.split(', |- |,-|-,|"',x)
    #print data
    temp=""
    for x in data:
        if x !='-':
            temp=temp+x+" "
    data= temp.split('  ')
    temp=""
    for i in range(len(data)):
        if i==1:
            data[i]=data[i].split(' -')[0]+"] "
        temp= temp +data[i]+" "
    data=temp.split("  ")
    temp=""
    for i in range(len(data)):
        if i == len(data)-2:
            temp=temp+data[i]
            break
        temp=temp+data[i]+','
    #print temp
    return temp


if __name__ == '__main__':
    with open('access.txt', 'rb') as f:
        data = f.readlines()
    #extract(data[17])
    f=open('data.txt','wb')
    f.write('ip address,'+'time stamp,'+'method-url,'+'browser'+'\n')
    for i in range(len(data)):
        print i
        f.write(extract(data[i]))
    f.close()


