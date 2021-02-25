from django.shortcuts import render
from .models import Place

def travel_index(request):

    #p1 = Place("Chennai","Chennai.jpg",550)
    p1 = Place()
    p1.destination = "Chennai"
    p1.price = 500
    
    #p2=Place("Mumbai","Mumbai.jpg",800)
    p2 = Place()
    p2.destination = "Mumbai"
    p2.price=800

    #p3 = Place("Bangalore","Bangalore.jpg",550)
    p3 = Place()
    p3.destination = "Bangalore"
    p3.price = 500

    p4 = Place()
    p4.destination = "Hyderabad"
    p4.price = 350

    p5 = Place()
    p5.destination = "Pune"
    p5.price = 450

    p6 = Place()
    p6.destination = "Trivandrum"
    p6.price = 500


    
    dests = [p1,p2,p3,p4,p5,p6]
    #dests = {"Name":'Chenna',"Image":"Chennai.jpg","Price":500}
    return render(request,"travel_agency/index.html",{'dests':dests})
# Create your views here.
