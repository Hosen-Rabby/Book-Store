from django.shortcuts import render

from .forms import RegistraionForm 

def account_register(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        registraionForm = RegistraionForm(request.POST)