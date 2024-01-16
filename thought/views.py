 
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Thought, Like
from .forms import ThoughtForm  
from django.views.generic import CreateView, ListView
from django.views.generic.detail import DetailView
from user.models import User

# Create your views here.

@login_required
def like_thought(request, thought_id):
    thought = get_object_or_404(Thought, pk=thought_id)
    likes = Like.objects.filter(thought=thought)
    is_liked = likes.filter(user=request.user).exists()

    if request.method == 'POST':
        if 'like_button' in request.POST:
            if not is_liked:
                like = Like(user=request.user, thought=thought)
                like.save()
            else:
                # Unlike if already liked
                likes.filter(user=request.user).delete()

            # Redirect to the same page after handling the like action
            return redirect('thought_detail', thought_id=thought.id)

    context = {
        'thought': thought,
        'likes': likes,
        'is_liked': is_liked,
    }

    return render(request, 'thought_detail.html', context)






class User_thoughts(ListView):
    model = Thought
    template_name = 'user/home.html'
    context_object_name = 'thoughts'
    # ordering = ['-creat_time']

# class Thought_detail(DetailView):
#     model = Thought
#     template_name = 'thought_detail.html'
#     context_object_name = 'thought'
    
@login_required
def thought_detail(request, thought_id):
    thought = get_object_or_404(Thought, pk=thought_id)
    return render(request, 'thought_detail.html', {'thought': thought})

@login_required
def create_thought(request):
    if request.method == 'POST':
        form = ThoughtForm(request.POST, request.FILES)
        if form.is_valid():
            thought = form.save(commit=False)
            thought.user = request.user
            # print("request.user: ",type(request.user))
            thought.save()
            return redirect('thought_detail', thought_id=thought.id)
    else:
        form = ThoughtForm()
    
    return render(request, 'thought.html', {'form': form})







# def like_thought(request):
#     thought = thought.objects.all()
#     likes = Like.objects.all()
#     context = {
#        'thought': thought,
#        'likes': likes,
#     }
#     return render(request, 'like_thought.html', context)
