from django import forms
from django.contrib.auth import authenticate
from django.forms import extras
from django.contrib.auth.models import User
from . import models
from . import utils


class UserForm(forms.ModelForm):
    confirmed_password = forms.CharField(label='Confirm password',
                                         widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput,
        }

    def clean(self, *args, **kwargs):
        password = self.cleaned_data['password']
        confirmed_password = self.cleaned_data['confirmed_password']

        if password and confirmed_password:
            if password != confirmed_password:
                raise forms.ValidationError('Password mismatch!')

        return super(UserForm, self).clean(*args, **kwargs)


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
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError('Wrong username or password!')

        return super(LoginForm, self).clean(*args, **kwargs)
