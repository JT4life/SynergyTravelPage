from django.shortcuts import render
from django.http import HttpResponse
from . models import destination

def index(request):
    # dest = destination()
    # dest.name = "Bahamas"
    # dest.description = "Great spot for a vacation!"
    # dest.price = 1000
    # dest.img = "destination_1.jpg"
    # dest.offer = 1
    #
    # #create multiple objects
    # dest1 = destination()
    # dest1.name = "Hawaii"
    # dest1.description = "Best place for sushi!"
    # dest1.price = 1200
    # dest1.img = "destination_2.jpg"
    # dest1.offer = 1
    #
    # dest2 = destination()
    # dest2.name = "Paris"
    # dest2.description = "Best place to visit for pictures!"
    # dest2.price = 2000
    # dest2.img = "destination_3.jpg"

    dests = destination.objects.all()

    # dests =[dest,dest1,dest2]
    return render(request, "index.html", {'dests':dests})

