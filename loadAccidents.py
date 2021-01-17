from maps.models import Accidents, Scores
from csv import reader

with open('C:/Users/Max/code/RoadSafety/accidentsTable.csv', 'r') as read_obj:
    for i, row in enumerate(read_obj,start=1):
        if i == 1:
            continue
        else:
            entries = row[:-1].split(",")
            # print(entries[1],entries[2],entries[4],int(float(entries[5])))
            Accidents.objects.create(lat=entries[1],long=entries[2],street=entries[4],zip=int(float(entries[5])))

with open('C:/Users/Max/code/RoadSafety/scoresTable.csv', 'r') as read_obj:
    for i, row in enumerate(read_obj, start=1):
        if i == 1:
            continue
        else:
            entries = row.split(",")
            Scores.objects.create(street=entries[1], zip=int(float(entries[2])), score=float(entries[3]))
