import urllib.request
import json
import csv

APIkey = '0000000-0000-0000-0000-000000000000'

halldict = {}

hall = urllib.request.urlopen("https://rnd.kassir.ru/frame/feed/venue?key=" + APIkey + "&format=json")
hall = json.loads(hall.read())
print()


for x in range(0,len(hall)):
    #print(hall[x]['id'], hall[x]['name'])
    halldict[int(hall[x]['id'])] = hall[x]['name']

data = urllib.request.urlopen("https://rnd.kassir.ru/frame/feed/event?key=" + APIkey + "&format=json")
data = data.read()
print("loaded - ok")
parsed = json.loads(data)


with open('test.csv', 'w', newline="") as fileprint: #encoding='utf-8'
    writer = csv.writer(fileprint, delimiter=';', dialect='excel')
    writer.writerow(["EventID", "Name", "Venue", "URL"])  # write header

    for x in parsed:

        if parsed[x]['venue'] not in halldict:
            writer.writerow([str(x), str(parsed[x]['name']), str('not avalible ') + str(parsed[x]['venue']), str(parsed[x]['url'])])
        else:
            writer.writerow([str(x), str(parsed[x]['name']), halldict[parsed[x]['venue']], str(parsed[x]['url'])])
