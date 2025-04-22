from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Post, Comment
from django.utils import timezone
from blog.forms import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.

def blog(request, cat_name=None, author_username=None, tag_name = None):
    posts = Post.objects.filter(published_date__lte = timezone.now(), status = True).order_by('-published_date')

    if cat_name:
        posts = posts.filter(category__name=cat_name)

    if author_username:
        posts = posts.filter(author__username=author_username)

    if tag_name:
        posts = posts.filter(tags__name = tag_name)

    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    posts = Post.objects.filter(status=1,  published_date__lte=timezone.now())
    post = get_object_or_404(posts, id=pid)
    def counting(post):
        post.counted_views += 1
        post.save(update_fields=['counted_views'])
    counting(post)
    next_post = Post.objects.filter(
        published_date__gt=post.published_date, status=1, published_date__lte = timezone.now()
    ).order_by('published_date').first()

    previous_post = Post.objects.filter(
        published_date__lt=post.published_date, status=1
    ).order_by('-published_date').first()

    comments = Comment.objects.filter(post = post.id,approved=True).order_by('-created_date')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your message sent successfully')
        else:
            messages.add_message(request, messages.ERROR, 'something went wrong')
    
    else:
        form = CommentForm() 
    if post.login_require == False:
        comments = Comment.objects.filter(post = post.id,approved=True)
        form = CommentForm()
        context = {'post':post, 'previous_post':previous_post, 'next_post':next_post, 'comments':comments, 'form':form}
        return render(request, 'blog/blog-single.html', context)
    else:
        return HttpResponseRedirect(reverse('accounts:login'))


def blog_search(request):
    posts = Post.objects.filter(published_date__lte = timezone.now(), status = True).order_by('-published_date')

    if request.method == 'GET':
        if s:= request.GET.get('s'):
            posts = posts.filter(content__contains = s)

    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)


    
