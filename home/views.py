from django.shortcuts import render
from django.http import HttpResponse

from .project_summaries import SUMMARIES

# Create your views here.


def home_page(request):
    return render(request, "home/home.html")


def career(request):
    return render(request, "home/career.html")


def travel(request):
    return render(request, "home/travel.html")


def school(request):
    return render(request, "home/school.html")


def penguins(request):
    return render(request, "home/penguins.html")


def ontology(request):
    context = {
        "project_name": "Ontology Builder",
        "project_summary_p1": SUMMARIES["ontology_p1"],
        "project_summary_p2": SUMMARIES["ontology_p2"],
    }
    return render(request, "home/ontology.html", context)


def cci(request):
    context = {
        "project_name": "Customer Configuration Interface v3",
        "project_summary_p1": "",
        "project_summary_p2": "",
    }
    return render(request, "home/project_base.html", context)


def klarity_demo(request):
    context = {
        "project_name": "Klarity Marketing Demo",
        "project_summary_p1": "",
        "project_summary_p2": "",
    }
    return render(request, "home/project_base.html", context)


def legacy_processing(request):
    context = {
        "project_name": "Legacy Processing",
        "project_summary_p1": "",
        "project_summary_p2": "",
    }
    return render(request, "home/project_base.html", context)


def vlcm(request):
    context = {
        "project_name": "VMware Lifecycle Manager",
        "project_summary_p1": "",
        "project_summary_p2": "",
    }
    return render(request, "home/project_base.html", context)
