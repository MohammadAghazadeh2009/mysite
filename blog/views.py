from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Post
from django.utils import timezone
# Create your views here.

def blog(request, cat_name=None, author_username=None):
    posts = Post.objects.filter(published_date__lte = timezone.now(), status = True).order_by('-published_date')

    if cat_name:
        posts = posts.filter(category__name=cat_name)

    if author_username:
        posts = posts.filter(author__username=author_username)

    posts = Paginator(posts, 4)
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
    
    next_post = Post.objects.filter(
        published_date__gt=post.published_date, status=1, published_date__lte = timezone.now()
    ).order_by('published_date').first()

    previous_post = Post.objects.filter(
        published_date__lt=post.published_date, status=1
    ).order_by('-published_date').first()

    context = {'post':post, 'previous_post':previous_post, 'next_post':next_post}
    counting(post)
    return render(request, 'blog/blog-single.html', context)



def blog_search(request):
    posts = Post.objects.filter(published_date__lte = timezone.now(), status = True).order_by('-published_date')

    if request.method == 'GET':
        if s:= request.GET.get('s'):
            posts = posts.filter(content__contains = s)

    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)


    
