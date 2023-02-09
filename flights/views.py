from django.shortcuts import render
from  .models import Flight ,Airport

# Create your views here.
def index(request):

    flights= Flight.objects.all()
    context={"Flights":flights}

    return render (request,"fligths/index.html",context)

def  flight(request,flight_id):
    flight=Flight.objects.get(pk=flight_id)
    passengers=flight.passengers.all()
    context={"fligth":flight,"passengers":passengers}
    return render (request,"fligths/flight.html",context)