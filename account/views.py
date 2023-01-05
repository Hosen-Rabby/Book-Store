from django.shortcuts import render

from .forms import RegistraionForm 

def account_register(request):
    # if request.user.is_authenticated:
    #     return redirect('/')
    
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
            message = render_to_string('activate/registration/account_activation_email.html',{
                'user': user,
                'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            user.email_user(subject=sebject, message=message)
    else:
        registraionForm = RegistraionForm()
        return render(request, 'account/registration/register.html', {'form':registraionForm})
