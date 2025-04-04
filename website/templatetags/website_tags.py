from django import template
from blog.models import Post
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('website/from-blog.html')
def latest_posts():
    posts = Post.objects.filter(status=1, published_date__lte = timezone.now()).order_by('-published_date')[:6]
    return {'posts':posts}