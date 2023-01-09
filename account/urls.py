from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.account_register, name='register'),
    path('activate/<slug:uid64>/<slug:token>', views.account_activate, name='activate'),

    path('dashboard/', views.account_dashboard, name='dashboard'),

]