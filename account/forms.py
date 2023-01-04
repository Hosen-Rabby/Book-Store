from django import forms
from .models import UserBase

class RegistraionForm(forms.ModelForm):
    user_name = forms.CharField(label = 'Enter username', min_length=4, max_length=50, help_text='enter username')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={'required': 'Sorry, you will need an email.'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    repeat_password = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ('user_name', 'email')