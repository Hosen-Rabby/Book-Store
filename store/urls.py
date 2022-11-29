from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_products, name = 'all_products'),
    path('item/<slug:slug>/', views.prod_details, name = 'prod_details'),
    path('category/<slug:category_slug>/', views.category_list, name = 'category_list'),
]
