from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from  .models import Flight ,Airport,Passenger

# Create your views here.
def index(request):

    flights= Flight.objects.all()
    context={"Flights":flights}

    return render (request,"fligths/index.html",context)

def  flight(request,flight_id):
    flight=Flight.objects.get(pk=flight_id)
    passengers=flight.passengers.all()
    context={"fligth":flight,"passengers":passengers,"non_passengers":Passenger.objects.exclude(flights=flight).all()}
    return render (request,"fligths/flight.html",context)

def book(request,flight_id):
    if request.method=="POST":
        flight=Flight.objects.get(pk=flight_id)
        passenger=Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse('fligth',args=(flight.id,)))
        