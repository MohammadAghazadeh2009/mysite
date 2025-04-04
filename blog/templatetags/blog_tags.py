from django import template
from blog.models import Post
from blog.models import Category


register = template.Library()

@register.inclusion_tag('blog/latest-posts.html')
def latest_posts():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:3]
    return {'posts':posts}
 
@register.inclusion_tag('blog/blog-category.html')
def categories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    
    return {'categories':cat_dict}