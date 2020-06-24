from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def listblogs(request):
    blogs = Blog.objects.all()
    return render(request, './blog/listblogs.html', {"blogs": blogs})

def detailblog(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, './blog/detailblog.html', {"blog": detailblog})
