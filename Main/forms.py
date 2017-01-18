from django import forms
from django.forms import extras
from django.contrib.auth.models import User
from . import models
from . import utils


class UserForm(forms.ModelForm):
    confirmed_password = forms.CharField(label='Confirm password',
                                         widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput,
        }


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = models.UserProfile
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'birthdate': extras.SelectDateWidget(
                            years=utils.FormUtils.get_birthday_years()
                        ),
        }

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)