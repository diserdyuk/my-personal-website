from django.shortcuts import render, get_object_or_404
from .models import Blogs


def blogs(request):
    # blog_count = Blogs.objects.count
    my_blogs = Blogs.objects.order_by('-date')
    return render(request, 'blog/blogs.html', {
        'my_blogs': my_blogs, 
        # 'blog_count': blog_count,
        })


def detail(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})



