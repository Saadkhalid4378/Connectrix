from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, HttpResponse,get_object_or_404, HttpResponseRedirect
# from django.urls import reverse
from user.forms import Signup, ProfileForm
from user.models import User, Profile
from thought.models import Thought
# from django.views import View
from thought.views import User_thought
from django.views.generic import TemplateView, ListView, CreateView, DeleteView
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
    return redirect("/thought/users_thoughts")
    # return render(request, 'user/home.html')


class User_thought(ListView):
    model = Thought
    template_name = 'profile.html'
    context_object_name = 'thought'

    def get_queryset(self):
        # Filter thoughts based on the is_private field and the current user
        if ['is_privste']:
            queryset = Thought.objects.filter(user = self.request.user)
            print(queryset)
            return queryset

# @method_decorator(login_required(login_url='login'), name='dispatch')
class Profile_view(User_thought, ListView):
    model = User
    form = ProfileForm
    template_name = 'profile.html'
    fields = '__all__'
    # context_object_name = 'profile' 
    # add a slug field in models.py according to user name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['thoughts'] = self.get_thoughts()  # Add thoughts to the context
        return context

    def get_thoughts(self):
        # You can customize this method to get additional thoughts data if needed
        return Thought.objects.filter(user=self.request.user, is_private=True)

    # def get_queryset(self) -> QuerySet[Any]:
    #     return super().get_queryset(User_thought)
    
    # def get(self, request: HttpRequest, *args: Any, **kwargs: Any):
    #      QuerySet = User_thought
    #      return super().get(QuerySet)

    # def get(self, request, *args, **kwargs):
    #     self.object_list = self.get_queryset(User_thought)
    #     allow_empty = self.get_allow_empty()




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