from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('<slug:category_slug>', views.home, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>', views.productPage, name='product_detail'),
]