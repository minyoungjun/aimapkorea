import csv

def date_to_int(date):

    date_split = date.replace("월", "").replace("일", "").split(' ')
    
    if (int(date_split[0]) == 1):
        if (len(date_split[1]) == 2):
            return "2017-01-" + date_split[1]
        else:
            return "2017-01-0" + date_split[1]
        
    else:
        if (len(date_split[0]) == 1):
            date_split[0] =  "0" + date_split[0]
        if (len(date_split[1] ) == 1):
            date_split[1] = "0" + date_split[1]
            
        return "2016-" + date_split[0] + "-" + date_split[1]


f = open("./amount.csv", 'r')

csvReader = csv.reader(f)

csvfile = open("./amount2.csv", 'w')
c = csv.writer(csvfile, delimiter = ',')

for row in csvReader:
    if (row[2] != "name"):
        c.writerow( [row[0], row[1], row[2], date_to_int(row[3]), row[4], row[5], row[6], row[7] ])
    else:
        c.writerow( [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7] ])

csvfile.close()
f.close()