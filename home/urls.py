from django.urls import path

from . import views


urlpatterns = [
    path("", views.home_page, name="home"),
    path("career/", views.career, name="career"),
    path("travel/", views.travel, name="travel"),
    path("school/", views.school, name="school"),
    path("penguins/", views.penguins, name="penguins"),
    path("career/ontology/", views.ontology, name="ontology"),
    path("career/cci", views.cci, name="cci"),
    path("career/klarity-demo", views.klarity_demo, name="klarity-demo"),
    path("career/legacy-processing", views.legacy_processing, name="legacy-processing"),
]
