from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, 'blog/blog-home.html')

def blog_single(request):
    return render(request, 'blog/blog-single.html')
