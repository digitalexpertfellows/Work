from django.urls import path

from . import views
urlpatterns = [
    path('home/',views.HomeTemplateView.as_view(), name='home')
]