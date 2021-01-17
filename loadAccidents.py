from road_safety.maps.models import Accidents, Scores
from csv import reader

with open('accidentsTable.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in read_obj:
        print(row)

