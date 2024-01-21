from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, HttpResponse,get_object_or_404, HttpResponseRedirect
# from django.urls import reverse
from user.forms import Signup, ProfileForm
from user.models import User, Profile
from thought.models import Thought
# from django.views import View
# from thought.views import User_thought
from django.views.generic import TemplateView, ListView, CreateView,DetailView, DeleteView
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def logout_user(request):
    # if request.method == 'POST':
        if request.user.is_authenticated:
            logout(request) 
            return redirect('login')

def login_page(request):
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
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
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
        context = {'form': form}
        return render(request, 'signup.html', context)


def home(request):
    return redirect("/thought/users-thoughts")
    # return render(request, 'user/home.html')


# class UserThought(ListView):
#     model = Thought
#     template_name = 'profile.html'
#     context_object_name = 'thought'

#     def get_queryset(self):
#         # Filter thoughts based on the is_private field and the current user
#         # if ['is_private']:
#             user=self.request.user
#             queryset = Thought.objects.filter(user=user)
#             print(queryset)
#             return queryset

# @method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileView(ListView):
    model = User
    form = ProfileForm
    template_name = 'profile.html'
    # fields = '__all__'
    # context_object_name = 'profile' 
    # add a slug field in models.py according to user name
    def get_context_data(self, **kwargs: Any):
        user=self.request.user
        queryset = Thought.objects.filter(user=user)
        context = {'thought': queryset, 
                    'username': user.username,
                    'email': user.email,
                    #  'bio': user.bio,
                    #  'DOB': user.date_of_birth,
                    #  'phone': user.phone,
                    #  'city': user.city
                    } 
        return(context)

    # def get_queryset(self) -> QuerySet[Any]:
    #     return super().get_queryset(User_thought)
    
    # def get(self, request: HttpRequest, *args: Any, **kwargs: Any):
    #      QuerySet = User_thought
    #      return super().get(QuerySet)

    # def get(self, request, *args, **kwargs):
    #     self.object_list = self.get_queryset(User_thought)
    #     allow_empty = self.get_allow_empty()




class EditProfile(LoginRequiredMixin, UpdateView):
    model = Profile
    form = ProfileForm
    template_name = 'user/updateprofile.html'
    fields = ['bio', 'date_of_birth', 'phone', 'city', 'image']
    # context_object_name = 'editprofile'
    # slug_field = 'slug'
    # slug_url_kwarg = 'slug'

    def get_object(self, queryset=None):
        # Retrieve the Profile object based on the user ID
        user_id = self.request.user.id
        return get_object_or_404(Profile, user_id=user_id)