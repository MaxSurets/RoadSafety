from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

from .models import Scores
import json
import urllib.request
import geocoder

def index(request):
    return HttpResponse("Hello, world. You're at the map index.")

def flatten(something):
    if isinstance(something, (list, tuple, set, range)):
        for sub in something:
            yield from flatten(sub)
    else:
        yield something

def split(arr, count):
     return [ arr[i:i+count] for i in range(0, len(arr), count) ]

class geojson_by_zip(View):
    def get(self, request, format="Json"):
        '''Return all streets with scores in geoJSON format'''

        zip_code = int(request.GET.get("zip"))
        BASE_URL = 'https://nominatim.openstreetmap.org/?format=json&polygon_geojson=1&addressdetails=1&q='
        GEOJSON = {
            "type": "FeatureCollection",
            "features": []
        }

        ID = 0
        COUNTRY_CODE = 'us'

        objects_in_zip = Scores.objects.filter(zip=zip_code)
        for obj in objects_in_zip:
        # obj = objects_in_zip[1]
            street = obj.street
            zip = obj.zip
            zip_str = str(zip).zfill(5)
            score = obj.score

            search_street_name = street.replace(" ", "+")
            url = f'{BASE_URL}{search_street_name}+US+{zip_str}'
            res_body = urllib.request.urlopen(url).read()
            content = json.loads(res_body.decode("utf-8"))
            streets = [x for x in content if x['address']['country_code'] == COUNTRY_CODE]
            streets = [d for d in streets if d.get('geojson', -1) != -1]
            coordinates = [street['geojson']['coordinates'] for street in streets if street['geojson']['type'] == 'LineString']
            all_coordinates = []

            if len(streets) > 0:
                all_coordinates = split(list(flatten(coordinates)), 2)

            ID += 1
            if len(all_coordinates) >= 1:
                street_geojson = {
                    "id": ID,
                        "type": "Feature",
                        "geometry": {
                            "type": "LineString",
                            "coordinates": all_coordinates},
                        "properties": {
                            "name": street,
                            "score": score
                        }
                }
                # add to geojson
                GEOJSON['features'].append(street_geojson)

        return JsonResponse(GEOJSON)

class location_from_zip(View):
    def get(self, request):
        '''Return latitude and longitude for given zip for centering map'''
        zip = request.GET.get("zip") + " US"
        g = geocoder.google(location=zip, key="AIzaSyAAq3MGrupeB1xxjMp_4G-RPFLx6KYGihY")
        return JsonResponse({"lat": g.latlng[0], "long":g.latlng[1]})