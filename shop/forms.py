from django import forms
from .models import ContactUs,CustomUser
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'



class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username','password']




class RegistrationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields =['first_name','last_name',
                  'username','email',
                  'phone_num','adres',
                  'password1','password2']


