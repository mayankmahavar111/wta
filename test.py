count=0
data=[]
with open('log/data.csv','rb') as f:
    for x in f:
        a = x.split(",")
        if len(a) > 5:
            try:
                if int(a[4])/100 == 2 or int(a[5])/100 == 2:
                    if (
                    not (a[3].endswith(".jpg") or a[3].endswith(".ico") or a[3].endswith(".gif") or a[3].endswith(".css"))):
                        data.append(a)
                        count += 1
            except:
                continue
        print count