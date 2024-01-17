from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, HttpResponse,get_object_or_404, HttpResponseRedirect
# from django.urls import reverse
from user.forms import Signup, ProfileForm
from user.models import User, Profile
# from django.views import View
# from thought.views import User_thoughts
from django.views.generic import TemplateView, ListView, CreateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def logoutuser(request):
    # if request.method == 'POST':
        if request.user.is_authenticated:
            logout(request) 
            return redirect('login')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
            # return redirect('create_thought')
            # return HttpResponse('homepage') 
        else:
            return HttpResponse(user)
    context = {'login': login}
    return render(request, 'login.html', context)

def signup(request):
        form = Signup()
        if request.method == 'POST':
            form = Signup(request.POST)
            if form.is_valid():
                user = form.save()
                profile = Profile(user=user)
                profile.save()
                return redirect('login')
            else:
                return HttpResponse(form.error_messages)
        context = {'form': form}
        return render(request, 'signup.html', context)


def home(request):
    return redirect("/thought/users_thought")
    # return render(request, 'user/home.html')

# @method_decorator(login_required(login_url='login'), name='dispatch')
class Profile_view(ListView):
    model = User
    form = ProfileForm
    template_name = 'profile.html'
    fields = '__all__'
    # context_object_name = 'profile' 
    # add a slug field in models.py according to user name


class Edit_profile(UpdateView):
    model = Profile
    form = ProfileForm
    template_name = 'profile.html'
    fields = '__all__'
    context_object_name = 'editprofile'
    # slug_field = 'slug'
    # slug_url_kwarg = 'slug'

    def get_object(self, queryset=None):
        # Retrieve the Profile object based on the user ID
        user_id = self.request.user.id
        return get_object_or_404(Profile, user_id=user_id)