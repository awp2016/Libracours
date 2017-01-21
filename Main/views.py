from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from . import forms


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        context = {'username': request.user.username}
        return render(request, 'Libracours/index.html', context)


class RegisterView(View):
    user_form_class = forms.UserForm
    user_profile_form_class = forms.UserProfileForm
    template_name = 'Libracours/register.html'
    context = {}

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')

        user_form = self.user_form_class()
        user_profile_form = self.user_profile_form_class()
        context = self.context
        context['user_form'] = user_form
        context['user_profile_form'] = user_profile_form

        return render(request, self.template_name, context)

    def post(self, request):
        user_form = self.user_form_class(request.POST)
        user_profile_form = self.user_profile_form_class(request.POST,
                                                         request.FILES)
        context = self.context
        context['user_form'] = user_form
        context['user_profile_form'] = user_profile_form

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
                messages.success(request, 'Account created successfully.')
                return redirect('login')

        return render(request, self.template_name, context)


class UserProfileView(LoginRequiredMixin, DetailView):

    model = models.UserProfile
    template_name = 'Libracours/userProfile.html'

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        return context


class LoginView(View):
    context = {}
    template_name = 'Libracours/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')

        context = self.context
        context['form'] = forms.LoginForm()
        return render(request, self.template_name, context)

    def post(self, request):
        context = self.context
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            login(request=request,
                  user=user)
            return redirect('index')

        context['form'] = form
        return render(request, self.template_name, context)


class LogoutView(RedirectView):
    pattern_name = 'login'

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)


class HomeView(View):
    def get(self, request):
        return render(request, 'Libracours/home.html')


class SubmitPost(LoginRequiredMixin, View):
    template_name = 'Libracours/submitPost.html'
    post_form_class = forms.PostForm

    def get(self, request):
        post_form = self.post_form_class()
        context = {'form': post_form}
        return render(request, self.template_name, context)

    def post(self, request):
        return render(request, self.template_name, {})
        # post_form = self.post_form_class(request.POST)
        # files = request.FILES.getlist('file_field')

        # if post_form.is_valid():
        # post = post_form.save(commit=False)
        # post.author = request.user

