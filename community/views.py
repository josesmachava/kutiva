from django.shortcuts import render, redirect
from django.utils import timezone

from cms.models import Course
from .models import Post
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from hitcount.views import HitCountDetailView
# Create your views here.
from community.models import Post
from .forms import PostForm


class PostCountHitDetailView(HitCountDetailView):
    model = Post  # your model goes here
    count_hit = True


def post_list(request):
    posts = Post.objects.all().order_by('created_date')
    courses = Course.objects.all()

    return render(request, 'community/post_list.html', {'posts': posts, 'courses': courses})


def ask_question(request):
    courses = Course.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
            # return redirect('post_list', pk=post.pk)
    else:

        form = PostForm()

    return render(request, 'community/ask.html', {'form': form, 'courses': courses})


def post_detail(request, pk):
    template_name = 'community/post_detail.html'
    post = get_object_or_404(Post, pk=pk)
    HitCountDetailView.count_hit = True
    # post = Post.objects.filter(pk=pk).order_by('-hit_count_generic__hits')[:3]
    comments = post.comments.filter(active=True)

    courses = Course.objects.all()
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            new_comment.user = request.user
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'courses': courses})
