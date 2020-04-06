from django.shortcuts import render, redirect
from django.utils import timezone

# Create your views here.
from community.models import Post
from .forms import PostForm

def post_list(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
            #return redirect('post_list', pk=post.pk)
    else:
        posts = Post.objects.all().order_by('created_date')

        form = PostForm()

    return render(request, 'community/post_list.html', {'posts': posts,  'form': form})