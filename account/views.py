from django.shortcuts import redirect, render

from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# from orders.views import user_orders

from .forms import RegistraionForm
from .tokens import account_activation_token
from .models import UserBase


# login required
@login_required
def account_dashboard(request):
    return render(request, 'account/user/dashboard.html')

def account_register(request):
    
    if request.method == 'POST':
        registraionForm = RegistraionForm(request.POST)
        if registraionForm.is_valid():
            user = registraionForm.save(commit=False)
            user.email = registraionForm.cleaned_data['email']
            user.set_password(registraionForm.cleaned_data['password'])
            user.is_active = False
            user.save()

            # setup email
            current_site = get_current_site(request)
            subject = 'Activate your account'
            message = render_to_string('account/registration/account_activation_email.html',{
                'user': user,
                'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message)
            return HttpResponse('Successful')
    else:
        registraionForm = RegistraionForm()


    return render(request, 'account/registration/register.html', {'form':registraionForm})


def account_activate(request, uidb64, token):
    try:                
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)
    except():
        pass
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('account:dashboard')
    else:
        return render(request, 'account/registraion/activation_invalid.html')