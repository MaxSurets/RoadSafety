from road_safety.maps.models import Accidents, Scores
from csv import reader

with open('accidentsTable.csv', 'r') as read_obj:
    #csv_reader = reader(read_obj)
    for i, row in enumerate(read_obj,start=1):
        if start == 1:
            continue
        else:
            entries = row.split(",")
            Accidents.objects.create(lat=entries[0],long=entries[1],street=entries[3],zip=int(entries[4]))

with open('scoresTable.csv', 'r') as read_obj:
    for i, row in enumerate(read_obj, start=1):
        if start == 1:
            continue
        else:
            entries = row.split(",")
            Scores.objects.create(street=entries[0], zip=int(entries[1]), score=float(entries[2]))


