from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
# Create your views here.
def blog(request):
    posts = Post.objects.filter(published_date__lte = timezone.now(), status = True).order_by('-published_date')
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    def counting(post):
        post.counted_views += 1
        post.save(update_fields=['counted_views'])
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, id=pid)
    context = {'post':post}
    counting(post)
    return render(request, 'blog/blog-single.html', context)
