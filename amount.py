import json, requests, csv

f = open("./korea_ai_result.csv", 'r')
csvReader = csv.reader(f)

csvfile = open("./amount.csv", 'w')
c = csv.writer(csvfile, delimiter = ',')

for row in csvReader:
    if (row[2] != "name"):
        res = row[4].split()
        c.writerow( [row[0], row[1], row[2], row[3], res[0], res[1], row[5], row[6]] )
csvfile.close()
f.close()