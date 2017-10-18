import csv
RESULT = ['apple','cherry','orange','pineapple','strawberry']
with open("output.csv",'wb') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
    wr.writerow(RESULT)