 
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Thought, Like, Comment, Comment_reply, Share
from .forms import ThoughtForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from django.views.generic.detail import DetailView
from user.models import User
from django.http import JsonResponse


# Create your views here.


class DeleteTHoughts(LoginRequiredMixin, DeleteView):
    model = Thought
    template_name = 'deletethought.html'
    context_object_name = 'delete'
    success_url = reverse_lazy('users_thoughts')


class UsersThoughts(ListView):
    model = Thought
    template_name = 'user/home.html'
    context_object_name = 'thoughts'
   
    def get_queryset(self):
        # Filter thoughts based on the is_private field and the current user
            # self.request.user
            queryset = Thought.objects.filter(is_private=False)
            # print(queryset)
            return queryset
        # else:
        #     Thought.objects.filter(is_private=True)
        #     # print(queryset)
        #     return queryset

"""  this function is use to add repply on the
     comments function will get id of comment 
     for reply "replyes" will store the comment id 
     and thought.id on which person is commenting    """
@login_required
def reply_Comment(request,id):
        replyes = get_object_or_404(Comment, id=id)
        reply = replyes.reply.all()

        if request.method == 'POST':
            text = request.POST.get('reply_coment')
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
            return redirect('thought_detail', thought_id=thought.id)

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
            return redirect('thought_detail', thought_id=thought.id)
    else:
        form = ThoughtForm()
    return render(request, 'thought.html', {'form': form})


# def replyComment(request,id):
#     comments = Comment.objects.get(id=id)
#     replyes = Comment_reply.objects.all( )

#     if request.method == 'POST':
#         user = request.user
#         reply_content = request.POST.get('reply_coment')
#         newReply = Comment_reply(user=user,  thought=comments.thought, comment=comments, text=reply_content)
#         newReply.reply_comment = comments
#         newReply.save()
#         messages.success(request, 'Comment replied!')
#         return redirect('thought_detail',thought_id=comments.thought.id) 
#     context = {
#         'replyes' : replyes
#     }
#     return render(request, 'replycomment.html', context)


# class User_thought(ListView):
#     model = Thought
#     template_name = 'profile.html'
#     context_object_name = 'thought'

#     def get_queryset(self):
#         # Filter thoughts based on the is_private field and the current user
#         if ['is_privste']:
#             queryset = Thought.objects.filter(user = self.request.user)
#             print(queryset)
#             return queryset
        # else:
        #     Thought.objects.filter(is_private=True)
        #     print(queryset)
        #     return queryset

# class Comment_View(CreateView):
#     model = Comment
#     form = CommentForm
#     template_name = 'comment.html'
#     success_url = reverse_lazy('comment_thought')  # Update with your actual URL name
#     fields = '__all__'  

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         form.instance.post = get_object_or_404(Thought, pk=self.kwargs['pk'])
#         print()
#         return super().form_valid(form)


# @login_required
# def like_thought(request, pk):
#     thought = get_object_or_404(Thought, pk=pk)
#     likes = Like.objects.filter(thought=thought)
#     is_liked = likes.filter(user=request.user).exists()

#     if request.method == 'POST':
#         if 'like_button' in request.POST:
#             if not is_liked:
#                 like = Like(user=request.user, thought=thought)
#                 like.save()
#             else:
#                 # Unlike if already liked
#                 likes.filter(user=request.user).delete()

#             # Redirect to the same page after handling the like action
#             # return redirect('thought_detail', thought_id=thought.id)
#     context = {
#         'thought': thought,
#         'likes': likes,
#         'is_liked': is_liked,
#     }

#     return render(request, 'like_thought.html', context)

# @login_required
# def thought_detail(request, thought_id):
#     thought = get_object_or_404(Thought, pk=thought_id)
#     comment = thought.comment.all()
#     new_comment = None
#     # return render(request, 'thought_detail.html', {'thought': thought})

#     if request.method == 'POST':
#         text = request.POST.get('text')
#         # print(f'shoqqqqqqqqqqqq{text}')
#         thought_comment = Comment(text=text, thought=thought, user=request.user)
#         # print(f'printtttttttttttttt{thought_comment}')
#         thought_comment.save()   
#         context = {'new_comment': new_comment, 
#                    'comment': comment, 
#                    'thought': thought, 
#                    'pk':thought_id}
#     return render( request, 'thought_detail.html', context)


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
