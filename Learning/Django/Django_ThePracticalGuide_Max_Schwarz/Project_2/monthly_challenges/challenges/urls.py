from django.urls import path
from . import views

#URL CONF

urlpatterns = [
    #PATH Function
    path("", views.index), #/challenges/
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),

]

