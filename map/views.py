from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from .models import PointFeature


# Create your views here.

def map(request):
    lastView = PointFeature.objects.order_by("id").last()
    coords = {"coords": list(PointFeature.objects.values()), "lastview": lastView if lastView else {"latitude": 0, "longitude": 0, "zoom": 3}}
    #print(coords)
    return render(request, "map/index.html", coords)

@csrf_exempt
def create_point(request):
    if request.method == "POST":
        coords = json.loads(request.body)
        print(coords)

        PointFeature.objects.create(
            latitude=coords["latitude"], 
            longitude=coords["longitude"],
            zoom=coords["zoom"])

        return HttpResponse(status=200)
    elif request.method == "DELETE":
        id = json.loads(request.body)
        print(id)
        PointFeature.objects.filter(id=id["id"]).delete()
        return HttpResponse(status=200)

