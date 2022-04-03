from curses.ascii import HT
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def home_page(request):
    return render(request, "home/home.html")


def career(request):
    return render(request, "home/career.html")


def travel(request):
    return render(request, "home/travel.html")


def school(request):
    return render(request, "home/school.html")
