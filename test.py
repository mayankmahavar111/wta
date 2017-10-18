x='[18/Jul/2011:03:35:52]'
a='[18/Jul/2011:04:51:15]'
y=x.split(':')
a=a.split(':')
temp=""
temp2=""
for i in range(len(y)):
    if i == 0:
        continue
    if i==1:
        temp = temp + y[i]
        temp2 = temp2 + a[i]
        continue
    temp = temp +" "+y[i]
    temp2=temp2+" "+a[i]

temp=temp.split(']')[0]
temp2=temp2.split(']')[0]
print temp,'\n',temp2

temp=temp.split(' ')
temp2=temp2.split(' ')
temp3=""
for i in range(len(temp)):
    if i==0:
        temp3 += str(abs(int(temp[i]) - int(temp2[i])))
        continue
    temp3 += " "+ str(abs(int(temp[i]) - int(temp2[i])))

print temp3