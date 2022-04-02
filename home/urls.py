from django.urls import path

from . import views


urlpatterns = [
    path("", views.home_page, name="home"),
    path("career", views.career, name="career"),
    path("life", views.life, name="life"),
    path("contact", views.contact, name="contact")
]
