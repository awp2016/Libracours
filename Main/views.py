from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from . import forms


class IndexView(View):
    def get(self, request):
        context = {'username': request.user.username}
        return render(request, 'Libracours/index.html', context)


class RegisterView(View):
    user_form_class = forms.UserForm
    user_profile_form_class = forms.UserProfileForm
    template_name = 'Libracours/register.html'
    context = {}

    def get(self, request):
        user_form = self.user_form_class()
        user_profile_form = self.user_profile_form_class()
        context = self.context
        context['user_form'] = user_form
        context['user_profile_form'] = user_profile_form
        context['forms'] = (user_form, user_profile_form)

        return render(request, self.template_name, context)

    def post(self, request):
        user_form = self.user_form_class(request.POST)
        user_profile_form = self.user_profile_form_class(request.POST,
                                                         request.FILES)
        context = self.context
        context['user_form'] = user_form
        context['user_profile_form'] = user_profile_form
        context['forms'] = (user_form, user_profile_form)

        if user_form.is_valid() and user_profile_form.is_valid():
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']

            user = user_form.save(commit=False)
            user.set_password(password)  # hashes the raw password
            user.save()

            user_profile = user_profile_form.save(commit=False)
            user_profile.user = user  # link profile with django User object
            user_profile.save()

            user = authenticate(username=username, password=password)
            if user:
                login(request=request, user=user)
                return redirect('index')

        return render(request, self.template_name, context)
