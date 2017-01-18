from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.detail import DetailView
from . import models
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

class UserProfileView(DetailView):

    model = models.UserProfile
    template_name = 'Libracours/userProfile.html'
    
    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        return context
	
	
class LoginView(View):
	context = {}
	
	def get(self, request):
		context = self.context
		context['form'] = forms.LoginForm()
		return render(request, 'Libracours/login.html', context)
		
	def post(self, request):
		context = self.context
		form = forms.LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'],
								password=form.cleaned_data['password'])
			if user:
				login(request=request,
					  user=user)
				return redirect('index')
			else:
				context['error_message'] = 'Wrong username or password!'
		context['form'] = form
		return render(request, 'Libracours/index.html', context)
