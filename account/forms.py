from django import forms
from .models import UserBase
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm

# user registration form
class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(label = 'Enter username', min_length=4, max_length=50, help_text='enter username')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={'required': 'Sorry, you will need an email.'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    repeat_password = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ('user_name', 'email')
    
    def clean_username(self):
        user_name = self.cleaned_data['user_name'].lower()
        r = UserBase.objects.filter(user_name = user_name)
        if r.count():
            raise forms.ValidationError('Username already exists.')
        return user_name
    
    # def clean_repeat_password(self):
    #     cd = self.cleaned_data
    #     if cd['password'] != ['repeat_password']:
    #         raise forms.ValidationError('Password do not match.')
    #     return cd['repeat_password']

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email = email).exists():
            raise forms.ValidationError('Please use another email, that is already taken.')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'class':'form-control mb-3', 'placeholder': 'Username'}
        )        
        self.fields['email'].widget.attrs.update(
            {'class':'form-control mb-3', 'placeholder': 'Email', 'name':'email'}
        )
        self.fields['password'].widget.attrs.update(
            {'class':'form-control mb-3', 'placeholder': 'Password'}
        )
        
        self.fields['repeat_password'].widget.attrs.update(
            {'class':'form-control mb-3', 'placeholder': 'Repeat Password'}
        )
        

# user login form
class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter email', 'id': 'login-username'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))
    


# user edit form
class UserEditForm(forms.ModelForm):

    email = forms.EmailField(
        label='Account email (can not be changed)', max_length=200, widget=forms.TextInput(
            attrs={'class':'form-control mb-3', 'placeholder':'email', 'id':'form_email', 'readonly':'readonly'}
        )
    )

    # user_name = forms.CharField(
    #     label='Firstname', min_length=4, max_length=50, widget=forms.TextInput(
    #         attrs={'class':'form-control mb-3', 'placeholder': 'User name','id':'form_firstname', 'readonly':'readonly'}
    #     )
    # )

    first_name = forms.CharField(
        label='Firstname', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class':'form-control mb-3', 'placeholder': 'First name','id':'first_name'}
        )
    )


    class Meta:
        model = UserBase
        fields = ('email', 'first_name')


    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['email'].required = True


class PwdResetForm(PasswordResetForm):
    
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={
        'class':'form-sontrol mb-3', 'placeholder':'Email', 'id':'form-email'
        }
    ))

    def clean_email(self):
        email = self.cleaned_data['email']
        print(email)
        u = UserBase.objects.filter(email = email)
        if not u:
            raise forms.ValidationError(
                'Unfortunately we can not find that email address'
            )
        return email
    


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New Password', widget=forms.PasswordInput(
        attrs={'class':'form-control mb-2', 'placeholder':'New Password', 'id':'form_newpassword1'}
        )
    )
    
    new_password2 = forms.CharField(
        label='New Password', widget=forms.PasswordInput(
        attrs={'class':'form-control mb-2', 'placeholder':'New Password', 'id':'form_newpassword2'}
        )
    )