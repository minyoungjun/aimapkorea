import json, requests, csv

def address_to_coord(address):
    
    url = "https://apis.daum.net/local/geo/addr2coord?apikey=80082c0a08cf340076dbdc49c67c74ac&output=json&q=" + address
    source_json = json.loads(requests.get(url).text)
    coord = source_json['channel']['item'][0]
    lat = coord['lat']
    lng = coord['lng']
    
    return { 'lat' : lat, 'lng' : lng }

f = open("./korea_ai.csv", 'r')
csvReader = csv.reader(f)

csvfile = open("./korea_ai_result4.csv", 'w')
c = csv.writer(csvfile, delimiter = ',')

for row in csvReader:
    if (row[2] != "name"):
        res = address_to_coord(row[2])
        print(row[0], res['lat'], res['lng'])
        c.writerow( [row[0], row[1], row[2], row[3], row[4], res['lat'], res['lng']] )
csvfile.close()
f.close()