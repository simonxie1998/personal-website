from curses.ascii import HT
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def home_page(request):
    return render(request, "home/index.html")


def career(request):
    return render(request, "home/career.html")


def life(request):
    return render(request, "home/life.html")


def contact(request):
    return render(request, "home/contact.html")