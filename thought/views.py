 
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Thought, Like, Comment, Comment_reply, Share
from .forms import ThoughtForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
from django.http import JsonResponse


# Create your views here.

class DeleteTHoughts(LoginRequiredMixin, DeleteView):
    model = Thought
    template_name = 'deletethought.html'
    context_object_name = 'delete'
    success_url = reverse_lazy('users-thoughts')


class UsersThoughts(ListView):
    model = Thought
    template_name = 'user/home.html'
    context_object_name = 'thoughts'
   
    def get_queryset(self):
        queryset = Thought.objects.filter(is_private=False)
        return queryset


"""  this function is use to add repply on the
     comments function will get id of comment 
     for reply "replyes" will store the comment id 
     and thought.id on which person is commenting    """

@login_required
def reply_Comment(request,id):
        replyes = get_object_or_404(Comment, id=id)
        reply = replyes.reply.all()

        if request.method == 'POST':
            text = request.POST.get('replycoment')
            reply_comment = Comment_reply(text=text, thought=replyes.thought ,comment=replyes, user=request.user)
            reply_comment.save()   
            context = { 'reply': reply , 'id':id}
        return render( request, 'thought_detail.html', context)


@login_required
def thought_detail(request, thought_id):
    thought = get_object_or_404(Thought, pk=thought_id)
    comment = thought.comment.all()
    new_comment = None

    # Like functionality
    likes = Like.objects.filter(thought=thought)
    is_liked = likes.filter(user=request.user).exists()
    like_count = likes.count()

    if request.method == 'POST':
        if 'text' in request.POST:
            # Commenting
            text = request.POST.get('text')
            thought_comment = Comment(text=text, thought=thought, user=request.user)
            thought_comment.save()
            new_comment = thought_comment
        elif 'like_button' in request.POST:
            # Liking
            if not is_liked:
                like = Like(user=request.user, thought=thought)
                like.save()
            else:
                # Unlike if already liked
                likes.filter(user=request.user).delete()
            # Redirect to the same page after handling the like action
            return redirect('thought-detail', thought_id=thought.id)

    context = {
        'thought': thought,
        'likes': likes,
        'is_liked': is_liked,
        'like_count': like_count,
        'new_comment': new_comment,
        'comment': comment,
        'pk': thought_id,
    }

    return render(request, 'thought_detail.html', context)


@login_required
def create_thought(request):
    if request.method == 'POST':
        form = ThoughtForm(request.POST, request.FILES)
        if form.is_valid():
            print("Form Data:", form.cleaned_data)
            thought = form.save(commit=False)
            thought.user = request.user
            # print("request.user: ",type(request.user))
            thought.save()
            return redirect('thought-detail', thought_id=thought.id)
    else:
        form = ThoughtForm()
    return render(request, 'thought.html', {'form': form})



@login_required
def share_thought(request, thought_id):
    thought = get_object_or_404(Thought, pk=thought_id)

    # Check if the thought has already been shared by the user
    if Share.objects.filter(user=request.user, thought=thought).exists():
        # Handle case where the user has already shared this thought
        return JsonResponse({'message': 'You have already shared this thought.'}, status=400)

    # Create a new Share instance
    new_share = Share(user=request.user, thought=thought)
    new_share.save()

    # Optionally, you can perform additional actions here, such as sending notifications or updating counters.

    return JsonResponse({'message': 'Thought shared successfully.'})
