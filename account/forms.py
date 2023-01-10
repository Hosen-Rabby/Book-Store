from django import forms
from .models import UserBase

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
        
    

