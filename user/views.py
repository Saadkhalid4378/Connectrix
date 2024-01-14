from django.shortcuts import render, redirect, HttpResponse
from user.forms import Signup, Profile
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def profile(request):
    pass

def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # return redirect('home')
            return redirect('create_thought')
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
            form.save()
        else:
            return HttpResponse(form.error_messages)
    context = {'form': form}
    return render(request, 'signup.html', context)

def home(request):
    return render(request, 'home.html')


def about(request):
    pass