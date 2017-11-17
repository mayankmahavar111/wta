import os

os.makedirs('predict')

for x in os.listdir("cluster") :
    try:
        f=open('predict/'+x ,'w')
        f.close()
    except:
        pass
