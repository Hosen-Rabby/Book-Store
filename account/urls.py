from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from .forms import ( UserLoginForm, PwdResetForm, PwdResetConfirmForm)
from . import views

app_name = 'account'


urlpatterns = [
    # login
    path('login/', auth_views.LoginView.as_view(template_name='account/registration/login.html', form_class=UserLoginForm), name = 'login'),
    # logout
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name = 'logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='account/user/password_reset_form.html', 
        success_url = 'password_reset_email_confirm', 
        email_template_name = 'account/user/password_reset_email.html', form_class=PwdResetForm), name = 'password_reset'),

    path('password_reset_confirm/<slug:uidb64>/<slug:token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='account/user/password_reset_confirm.html',
        success_url = 'password_reset_complete',
        form_class=PwdResetConfirmForm), name = 'password_reset_confirm'),

    path('register/', views.account_register, name='register'),
    path('activate/<uidb64>/<token>', views.account_activate, name='activate'),
    path('dashboard/', views.account_dashboard, name='dashboard'),

    # delete account
    path('frofile/edit/', views.profile_edit, name='profile_edit'),
    path('frofile/delete/', views.profile_delete, name='profile_delete'),
    path('profile/delete_confirm', TemplateView.as_view(template_name='account/user/delete_confirm.html'), name = 'delete_confirmation'),
]