# home/views.py
from django.http import HttpResponse
from django.shortcuts import render

people =[

    {"name": "pushpraj", "age": 23},
    {"name": "aalok", "age": 233},
    {"name": "nimesh", "age": 24},
    {"name": "rishav", "age": 12},
    {"name": "saurab", "age": 22}
    

]


def home(request):
    return render(request, "index.html", context={"people": people})



def home(request):
    return render(request, "contact.html", context={"people": people})

# def home(request):
#     return render(request, "aboutus.html", context={"people": people})
