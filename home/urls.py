from django.urls import path

from . import views


urlpatterns = [
    path("", views.home_page, name="home"),
    path("career/", views.career, name="career"),
    path("travel/", views.travel, name="travel"),
    path("school/", views.school, name="school")
]
